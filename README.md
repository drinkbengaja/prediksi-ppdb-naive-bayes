# 🎓 Sistem Prediksi PPDB SDN Karamat Randu Menggunakan Naive Bayes

Proyek ini merupakan aplikasi berbasis **Artificial Intelligence** yang menerapkan
algoritma **Naive Bayes** untuk memprediksi peluang kelulusan calon siswa
dalam proses **Penerimaan Peserta Didik Baru (PPDB)** Sekolah Dasar Negeri (SDN).

Aplikasi ini dibuat sebagai **Proyek Akhir UAS Mata Kuliah Artificial Intelligence**
Universitas Muhammadiyah Sukabumi.

---

## 🧠 Metode yang Digunakan
- Simple Learning / Prediction
- Algoritma: **Naive Bayes (GaussianNB)**

---

## 📊 Data yang Digunakan
Data latih berupa data dummy PPDB tahun sebelumnya yang mencakup:
- Rata-rata nilai siswa
- Jarak rumah ke sekolah
- Status kelulusan (Lolos / Gagal)

Data digunakan untuk melatih model Naive Bayes agar dapat memprediksi
peluang kelulusan siswa baru.

---

## 🖥️ Teknologi yang Digunakan
- Python 3.12
- Streamlit
- Pandas
- Scikit-learn

---

## 🚀 Cara Menjalankan Aplikasi

### 1. Clone Repository
```bash
git clone https://github.com/USERNAME_GITHUB/prediksi-ppdb-naive-bayes.git
cd prediksi-ppdb-naive-bayes
### 2. Install Dependencies
python -m pip install streamlit pandas scikit-learn

### 3. Jalankan Aplikasi
python -m streamlit run app.py



