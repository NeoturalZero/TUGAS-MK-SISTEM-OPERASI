# TUGAS-MK-SISTEM-OPERASI
Repository Analisis & Simulasi **"Memori vs Storage di Kehidupan Nyata"**

## Deskripsi
Repository ini berisi hasil **investigasi dan eksperimen** penggunaan **Virtual Memory** dan **Mass Storage (SSD vs HDD)** pada sistem operasi modern. Eksperimen dilakukan menggunakan tools sistem nyata untuk mengamati bagaimana konsep teori **Sistem Operasi** bekerja dalam praktik sehari-hari.

Repository ini merupakan gabungan tugas:
- **Fase 2: Investigasi & Eksperimen**
- **Fase 3: Laporan & Presentasi (Storytelling Teknis)**

Pendekatan yang digunakan tidak hanya berfokus pada teori, tetapi juga pada **fenomena nyata yang teramati**, serta bagaimana teori sistem operasi menjelaskan perilaku sistem tersebut.

---

## 🎯 Tujuan Eksperimen

Tujuan dari eksperimen ini adalah:
1. Menganalisis perbedaan penggunaan **memori fisik (RAM)** dan **memori virtual** pada sistem operasi.
2. Mengamati terjadinya **page fault** dan perilaku **swap usage** saat sistem berada pada kondisi beban tinggi.
3. Membandingkan performa **media penyimpanan SSD dan HDD** berdasarkan hasil uji baca/tulis.
4. Mengaitkan hasil eksperimen dengan konsep:
   - Demand Paging  
   - Page Fault  
   - Virtual Memory  
   - Disk Scheduling Algorithms (FCFS, SSTF, SCAN, C-SCAN)
5. Menyajikan hasil analisis dalam bentuk laporan dan presentasi berbasis **investigasi nyata**, bukan hanya teori.

---

## 🧰 Tools dan Lingkungan Eksperimen

### Sistem Operasi
- Windows 11

### Tools Monitoring & Benchmark
- **Task Manager** (Monitoring RAM & Disk)
- **Resource Monitor** (Detail Memory & Disk Activity)
- **Performance Monitor (PerfMon)**  
  - Page Faults/sec  
  - Available MBytes  
  - Committed Bytes
- **CrystalDiskMark** (Uji performa SSD dan HDD)

### Perangkat Keras
- RAM: (diisi sesuai perangkat)
- Storage:
  - SSD (NVMe / SATA)
  - HDD (jika tersedia)

---

## 🧪 Metodologi Eksperimen

### A. Virtual Memory
Eksperimen Virtual Memory dilakukan dengan cara:
1. Memantau penggunaan memori fisik dan virtual menggunakan Task Manager dan Resource Monitor.
2. Menjalankan beban kerja berat, seperti:
   - Membuka 50+ tab browser
   - Menjalankan video streaming
   - Menjalankan aplikasi berat (IDE, emulator, atau VM)
3. Mencatat perubahan:
   - Penggunaan RAM
   - Page Fault
   - Committed Memory
   - Respons sistem (lag, delay, atau penurunan performa)
4. Menyimpan hasil monitoring berupa screenshot dan log PerfMon.

### B. Mass Storage
Eksperimen Mass Storage dilakukan dengan:
1. Menjalankan benchmark baca/tulis menggunakan CrystalDiskMark.
2. Menguji performa:
   - Sequential Read/Write
   - Random Read/Write
3. Membandingkan hasil antara SSD dan HDD.
4. Menganalisis hasil uji dalam konteks **disk scheduling algorithms**.

---

## 🎥 Video Presentasi

Video presentasi ini menjelaskan proses investigasi, hasil eksperimen, serta analisis fenomena yang diamati selama eksperimen **Virtual Memory** dan **Mass Storage**. Fokus presentasi tidak hanya pada hasil akhir, tetapi juga pada **alur berpikir dan keterkaitan antara teori sistem operasi dan praktik nyata di sistem**.

Isi utama video presentasi:
- Latar belakang dan tujuan eksperimen
- Demonstrasi monitoring Virtual Memory (page fault & swap usage)
- Perbandingan performa SSD dan HDD
- Analisis disk scheduling algorithms
- Kesimpulan dan insight eksperimen

File video dan slide presentasi dapat diakses pada folder:

