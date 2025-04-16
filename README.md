# 🧠 Clustering Mahasiswa Berdasarkan Nilai Menggunakan Self-Organizing Map (SOM)

## 📚 Deskripsi Proyek

Aplikasi ini digunakan untuk mengelompokkan mahasiswa berdasarkan nilai atau data numerik lain menggunakan metode Self-Organizing Map (SOM). Proyek ini dibangun dengan Streamlit untuk antarmuka web interaktif, serta memanfaatkan library seperti Pandas dan Numpy.

Pengguna cukup mengupload file CSV yang berisi data numerik mahasiswa (misalnya nilai X1, X2, X3...), memilih kolom fitur, lalu sistem akan menormalkan data, melatih model SOM, dan menetapkan masing-masing mahasiswa ke dalam klaster tertentu.

---

## 🎯 Tujuan Tugas

> Carilah sebuah kasus yang dapat diselesaikan dengan metode Kohonen, buat penyelesaiannya menggunakan sebuah pemrograman dengan bahasa apa saja, dan buatlah pembahasan dari kasus yang Anda pilih dalam bentuk presentasi (PPT).

> Tugas dikerjakan secara **berkelompok**, masing-masing kelompok terdiri dari **5 orang mahasiswa**, dan **siap dipresentasikan**.

---

## 🧠 Metode yang Digunakan

- Self-Organizing Map (SOM) diimplementasikan secara manual (tanpa library eksternal)
- Normalisasi data numerik dengan normalisasi maksimum
- Proses pelatihan bobot neuron dan penentuan klaster berdasarkan jarak Euclidean

---

## 💻 Fitur Aplikasi

- Upload file CSV yang berisi data mahasiswa
- Pilih kolom-kolom numerik untuk dijadikan fitur SOM
- Normalisasi otomatis terhadap data fitur
- Proses pelatihan SOM berdasarkan parameter:
  - Jumlah neuron (cluster)
  - Learning rate
  - Jumlah epoch
- Menampilkan:
  - Data asli
  - Data setelah normalisasi
  - Bobot awal dan akhir neuron
  - Hasil klasterisasi akhir (dapat di-download)
- Fitur tambahan: Tampilkan langkah-langkah perhitungan manual SOM

---

## 📦 Teknologi & Dependensi

Berikut adalah dependensi utama yang digunakan:

```text
streamlit==1.32.0
pandas==2.2.1
numpy==1.26.4
```

> Semua dependensi ini sudah dituliskan di file `requirements.txt`. Anda bisa menginstall-nya dengan:

```sh
pip install -r requirements.txt
```

## ▶️ Cara Menjalankan

1. Pastikan Python 3.10+ sudah terinstall

2. Install semua library:

```sh
pip install -r requirements.txt
```

3. Jalankan aplikasi Streamlit:

```sh
streamlit run app.py
```

## 🗂️ Struktur Proyek

```sh
.
├── pages/
│   └── home.py           # Halaman utama aplikasi
│   └── manual_hitung.py  # Fungsi perhitungan manual
├── app.py                # File utama Streamlit
├── README.md             # Dokumentasi ini
└── requirements.txt      # Daftar dependensi
```

## 🧾 Catatan Tambahan

- Proses pelatihan SOM ditulis manual.
- Perhitungan manual sangat cocok untuk kebutuhan presentasi edukatif atau pembelajaran konsep SOM.
- File CSV bebas, asalkan memuat kolom-kolom numerik.

## 👥 Kelompok 5 - Kecerdasan Buatan

| Status   | Name                | NIM           | University          | Media                                                                       | GitHub                                        |
| -------- | ------------------- | ------------- | ------------------- | --------------------------------------------------------------------------- | --------------------------------------------- |
| `Active` | Riyan Fazri Rahman  | `C2255201005` | STMIK Palangka Raya | [LinkedIn](https://www.linkedin.com/in/riyan-fazri-rahman/)                 | [GitHub](https://github.com/riyanfazrirahman) |
| `Active` | Alif Rahmatullah L. | `C2255201029` | STMIK Palangka Raya | [LinkedIn](https://www.linkedin.com/in/alif-rahmatullah-lesmana-565028311/) | [GitHub](https://github.com/Peparrepair)      |
| `Active` | Rif'ad Amin Jayadi  | `C2255201018` | STMIK Palangka Raya | -                                                                           | [GitHub](https://github.com/)                 |
| `Active` | Oga Luisca MIka S.  | `C2255201016` | STMIK Palangka Raya | -                                                                           | [GitHub](https://github.com/)                 |

---
