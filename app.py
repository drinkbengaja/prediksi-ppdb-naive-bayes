import streamlit as st
import pandas as pd
from sklearn.naive_bayes import GaussianNB

# ==============================
# KONFIGURASI HALAMAN
# ==============================
st.set_page_config(
    page_title="Prediksi PPDB SDN",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Prediksi Peluang Lolos PPDB")
st.write(
    "Aplikasi ini menggunakan algoritma **Naive Bayes** "
    "untuk memprediksi peluang kelulusan siswa baru "
    "berdasarkan data PPDB tahun sebelumnya."
)

st.write("---")

# ==============================
# DATA LATIH (SIMULASI)
# ==============================
data_latih = {
    "nilai_rata2": [
        85, 60, 78, 90, 55, 95, 70, 88, 65, 82,
        92, 50, 75, 89, 62, 98, 72, 80, 58, 85
    ],
    "jarak_km": [
        1.0, 5.0, 2.5, 0.5, 6.0, 0.2, 3.0, 1.2, 4.5, 2.0,
        0.8, 7.0, 2.2, 0.5, 5.5, 0.1, 3.5, 1.5, 6.5, 1.0
    ],
    "status": [
        "Lolos", "Gagal", "Lolos", "Lolos", "Gagal",
        "Lolos", "Gagal", "Lolos", "Gagal", "Lolos",
        "Lolos", "Gagal", "Gagal", "Lolos", "Gagal",
        "Lolos", "Gagal", "Lolos", "Gagal", "Lolos"
    ]
}

df = pd.DataFrame(data_latih)

# ==============================
# TRAINING MODEL
# ==============================
X = df[["nilai_rata2", "jarak_km"]]
y = df["status"]

model = GaussianNB()
model.fit(X, y)

# ==============================
# INPUT USER
# ==============================
st.sidebar.header("Masukkan Data Siswa")

input_nilai = st.sidebar.slider(
    "Rata-rata Nilai Rapor / TK",
    min_value=0,
    max_value=100,
    value=80
)

input_jarak = st.sidebar.number_input(
    "Jarak Rumah ke Sekolah (KM)",
    min_value=0.0,
    max_value=20.0,
    value=1.5
)

st.subheader("📊 Data Kamu")
st.write(f"- **Nilai Rata-rata:** {input_nilai}")
st.write(f"- **Jarak Rumah:** {input_jarak} km")

# ==============================
# PREDIKSI
# ==============================
if st.button("Cek Peluang Sekarang"):
    input_df = pd.DataFrame(
        [[input_nilai, input_jarak]],
        columns=["nilai_rata2", "jarak_km"]
    )

    hasil_prediksi = model.predict(input_df)[0]
    probabilitas = model.predict_proba(input_df)[0]
    tingkat_keyakinan = max(probabilitas) * 100

    if hasil_prediksi == "Lolos":
        st.success(
            f"✅ **SELAMAT!** Prediksi sistem: **LOLOS** "
            f"(Tingkat keyakinan {tingkat_keyakinan:.1f}%)"
        )
    else:
        st.error(
            f"❌ **MAAF.** Prediksi sistem: **GAGAL / WAITING LIST** "
            f"(Tingkat keyakinan {tingkat_keyakinan:.1f}%)"
        )
        st.info("💡 Saran: Pertimbangkan sekolah dengan jarak zonasi lebih dekat.")

# ==============================
# DATA HISTORIS (OPSIONAL)
# ==============================
with st.expander("📁 Lihat Data Historis (Simulasi)"):
    st.dataframe(df)
