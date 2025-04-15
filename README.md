# Clustering Mahasiswa Berdasarkan Karakter & Minat Belajar Menggunakan Kohonen (SOM)

## 📚 Deskripsi Proyek

Aplikasi ini digunakan untuk mengelompokkan mahasiswa berdasarkan karakter dan minat belajar mereka menggunakan metode **Self-Organizing Map (SOM)** dari jaringan syaraf tiruan Kohonen. Proyek ini dibangun menggunakan **Streamlit** untuk antarmuka web interaktif, serta memanfaatkan beberapa library populer seperti Pandas, Scikit-Learn, dan Plotly.

Mahasiswa cukup menjawab beberapa pertanyaan Ya/Tidak terkait minat mereka dalam bidang tertentu, dan sistem akan melakukan normalisasi, pelatihan SOM, serta memetakan ke klaster tertentu.

---

## 🎯 Tujuan Tugas

> Carilah sebuah kasus yang dapat diselesaikan dengan metode Kohonen, buat penyelesaiannya menggunakan sebuah pemrograman dengan bahasa apa saja, dan buatlah pembahasan dari kasus yang Anda pilih dalam bentuk presentasi (PPT).

> Tugas dikerjakan secara **berkelompok**, masing-masing kelompok terdiri dari **5 orang mahasiswa**, dan **siap dipresentasikan**.

---

## 🧠 Metode yang Digunakan

- **Self-Organizing Map (SOM)** dari library `MiniSom`
- Normalisasi data menggunakan `MinMaxScaler` dari Scikit-Learn
- Visualisasi distribusi dan peta klaster menggunakan `matplotlib` dan `plotly`

---

## 💻 Fitur Aplikasi

- Input karakter mahasiswa berdasarkan pertanyaan Ya/Tidak
- Visualisasi karakter sebagai donut chart
- Training model SOM berdasarkan dataset CSV
- Menampilkan posisi mahasiswa baru pada peta SOM
- Menyimpan data ke file `dataset.csv` (nama, jawaban, klaster)
- Tabel data semua mahasiswa + klasternya
- Donut chart distribusi klaster mahasiswa
- Tombol **simpan** & **refresh**

---

## 📦 Teknologi & Dependensi

Berikut adalah dependensi utama yang digunakan:

```text
streamlit==1.32.0
pandas==2.2.1
numpy==1.26.4
matplotlib==3.8.3
scikit-learn==1.4.1
plotly==5.20.0
minisom==2.3.0
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
├── app.py                # File utama Streamlit
├── dataset.csv           # Dataset mahasiswa (akan dibuat otomatis)
├── requirements.txt      # Daftar dependensi
├── pages/
│   └── home.py           # Halaman utama aplikasi
└── README.md             # Dokumentasi ini
```

## 📊 Contoh Pertanyaan Karakter Mahasiswa

- Suka memecahkan masalah logika?

- Suka menulis kode program?

- Tertarik pada desain visual?

- Tertarik membangun bisnis?

- Senang berorganisasi?

- Lebih suka praktik daripada teori?

## 🧾 Catatan Tambahan

- Dataset akan otomatis diperbarui saat data baru disimpan

- Model SOM dilatih ulang setiap kali aplikasi dijalankan

- Untuk presentasi, pembahasan akan dijelaskan dalam file PPT terpisah

## 👥 Kelompok 5 - Kecerdasan Buatan

| Status   | Name                | NIM           | University          | Media                                                                       | GitHub                                        |
| -------- | ------------------- | ------------- | ------------------- | --------------------------------------------------------------------------- | --------------------------------------------- |
| `Active` | Riyan Fazri Rahman  | `C2255201005` | STMIK Palangka Raya | [LinkedIn](https://www.linkedin.com/in/riyan-fazri-rahman/)                 | [GitHub](https://github.com/riyanfazrirahman) |
| `Active` | Alif Rahmatullah L. | `C2255201029` | STMIK Palangka Raya | [LinkedIn](https://www.linkedin.com/in/alif-rahmatullah-lesmana-565028311/) | [GitHub](https://github.com/Peparrepair)      |
| `Active` | Rif'ad Amin Jayadi  | `C2255201018` | STMIK Palangka Raya | -                                                                           | [GitHub](https://github.com/)                 |
| `Active` | Oga Luisca MIka S.  | `C2255201016` | STMIK Palangka Raya | -                                                                           | [GitHub](https://github.com/)                 |

---
