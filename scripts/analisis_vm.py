import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import re

# --- 1. Konfigurasi & Load Data ---
file_path = 'VM_Run1.csv' 

try:
    df = pd.read_csv(file_path, skipinitialspace=True)
except FileNotFoundError:
    print(f"Error: File '{file_path}' tidak ditemukan.")
    exit()

# --- 2. Cleaning Data ---
def clean_col_name(col):
    col = col.replace('"', '') 
    col = re.sub(r'\\\\.*?\\', '', col) 
    return col

df.columns = [clean_col_name(c) for c in df.columns]
df.rename(columns={df.columns[0]: 'Time'}, inplace=True)
df['Time'] = pd.to_datetime(df['Time'])

cols_numeric = [
    'Memory\\Page Faults/sec', 
    'Memory\\Available MBytes', 
    'Memory\\% Committed Bytes In Use', 
    'Paging File(_Total)\\% Usage'
]

for col in cols_numeric:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

df.dropna(subset=cols_numeric, inplace=True)

# Setting Style
sns.set_style("whitegrid")
date_fmt = mdates.DateFormatter('%H:%M:%S')

# ========================================================
# FIGURE 1: Page Faults vs Available RAM
# ========================================================
plt.figure(figsize=(12, 7))
ax1 = plt.gca()

# Data
time_series = df['Time']
pf_series = df['Memory\\Page Faults/sec']
ram_series = df['Memory\\Available MBytes']

# Hitung nilai max untuk mengatur batas atas grafik
max_pf = pf_series.max()

# Plot 1 (Page Fault - Merah)
line1 = ax1.plot(time_series, pf_series, color='#d62728', label='Page Faults/sec', linewidth=2)
ax1.set_ylabel('Page Faults / sec', color='#d62728', fontweight='bold', fontsize=12)
ax1.tick_params(axis='y', labelcolor='#d62728')
ax1.set_xlabel('Waktu (Jam:Menit:Detik)', fontweight='bold')

# PERBAIKAN UTAMA DI SINI:
# Tambahkan ruang kosong 40% di atas grafik agar teks tidak kepotong
ax1.set_ylim(0, max_pf * 1.4) 

# Plot 2 (Available RAM - Area Biru)
ax2 = ax1.twinx()
ax2.fill_between(time_series, ram_series, color='#1f77b4', alpha=0.2, label='Available RAM')
ax2.set_ylabel('Available RAM (MBytes)', color='#1f77b4', fontweight='bold', fontsize=12)
ax2.tick_params(axis='y', labelcolor='#1f77b4')

# Anotasi Puncak Page Fault
max_pf_idx = pf_series.idxmax()
max_pf_val = pf_series.max()
max_pf_time = df.loc[max_pf_idx, 'Time']

ax1.annotate(f'PUNCAK PAGE FAULT\n({max_pf_val:.0f} Faults/s)', 
             xy=(max_pf_time, max_pf_val), 
             xytext=(max_pf_time, max_pf_val + (max_pf_val * 0.2)), # Text digeser lebih aman
             arrowprops=dict(facecolor='black', shrink=0.05, width=2),
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=1.0),
             ha='center', fontweight='bold')

plt.title('ANALISIS 1: Page Faults & Sisa RAM\n(Indikator "Thrashing" atau Loading Berat)', fontsize=14, pad=20)
ax1.xaxis.set_major_formatter(date_fmt)
plt.grid(True, linestyle='--', alpha=0.5)

# Simpan File 1
plt.savefig('1_Analisis_PageFault.png', dpi=300, bbox_inches='tight')
print("Gambar 1 tersimpan: 1_Analisis_PageFault.png")
plt.close()


# ========================================================
# FIGURE 2: Swap Usage vs Committed Bytes
# ========================================================
plt.figure(figsize=(12, 7))
ax3 = plt.gca()

# Data
commit_series = df['Memory\\% Committed Bytes In Use']
swap_series = df['Paging File(_Total)\\% Usage']

# Plot 1 (Committed Bytes - Hijau)
ax3.plot(time_series, commit_series, color='#2ca02c', label='% Committed Bytes', linewidth=2)
ax3.set_ylabel('% Committed Bytes (Total Beban)', color='#2ca02c', fontweight='bold', fontsize=12)
ax3.tick_params(axis='y', labelcolor='#2ca02c')
ax3.set_xlabel('Waktu (Jam:Menit:Detik)', fontweight='bold')

# Plot 2 (Swap Usage - Ungu Putus-putus)
ax4 = ax3.twinx()
ax4.plot(time_series, swap_series, color='#9467bd', linestyle='--', label='Swap Usage', linewidth=2.5)
ax4.set_ylabel('Swap / Paging File % Usage', color='#9467bd', fontweight='bold', fontsize=12)
ax4.tick_params(axis='y', labelcolor='#9467bd')

# Anotasi Kenaikan Swap
start_swap = swap_series.iloc[0]
rise_point = df[df['Paging File(_Total)\\% Usage'] > start_swap + 0.5]

if not rise_point.empty:
    rise_time = rise_point.iloc[0]['Time']
    rise_val = rise_point.iloc[0]['Paging File(_Total)\\% Usage']
    
    ax4.annotate('Swap Mulai Naik\n(Persiapan Page Out)', 
                 xy=(rise_time, rise_val), 
                 xytext=(rise_time, rise_val + 5), 
                 arrowprops=dict(facecolor='#9467bd', shrink=0.05),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", edgecolor='#9467bd'),
                 color='#9467bd', fontweight='bold')

plt.title('ANALISIS 2: Swap Usage vs Total Load\n(Indikator Virtual Memory Activity)', fontsize=14, pad=20)
ax3.xaxis.set_major_formatter(date_fmt)
plt.grid(True, linestyle='--', alpha=0.5)

# Simpan File 2
plt.savefig('2_Analisis_Swap.png', dpi=300, bbox_inches='tight')
print("Gambar 2 tersimpan: 2_Analisis_Swap.png")

plt.close()
