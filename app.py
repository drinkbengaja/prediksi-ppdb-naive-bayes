import streamlit as st
import pandas as pd
from sklearn.naive_bayes import GaussianNB

st.set_page_config(
    page_title="Sistem Prediksi PPDB SDN Karamat Randu",
    page_icon="🏫",
    layout="centered"
)

st.title("🏫 Sistem Prediksi PPDB SDN Karamat Randu")
st.write(
    "Aplikasi ini merupakan **simulasi fitur AI** pada website resmi "
    "**SDN Karamat Randu** untuk membantu orang tua dan calon siswa "
    "memahami peluang kelulusan PPDB berdasarkan data historis."
)

st.info(
    "⚠️ **Disclaimer:** Hasil prediksi ini bersifat simulasi dan "
    "bukan merupakan keputusan resmi dari pihak sekolah."
)

st.write("---")
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
        "Lolos", "Tidak Lolos", "Lolos", "Lolos", "Tidak Lolos",
        "Lolos", "Tidak Lolos", "Lolos", "Tidak Lolos", "Lolos",
        "Lolos", "Tidak Lolos", "Tidak Lolos", "Lolos", "Tidak Lolos",
        "Lolos", "Tidak Lolos", "Lolos", "Tidak Lolos", "Lolos"
    ]
}

df = pd.DataFrame(data_latih)
X = df[["nilai_rata2", "jarak_km"]]
y = df["status"]

model = GaussianNB()
model.fit(X, y)
st.sidebar.header("📋 Input Data Calon Siswa")

input_nilai = st.sidebar.slider(
    "Nilai Rapor Calon Siswa",
    min_value=0,
    max_value=100,
    value=80
)

input_jarak = st.sidebar.number_input(
    "Jarak Rumah ke SDN Karamat Randu (KM)",
    min_value=0.0,
    max_value=20.0,
    value=1.5
)

st.subheader("📊 Data yang Dimasukkan")
st.write(f"- **Nilai Rapor:** {input_nilai}")
st.write(f"- **Jarak Rumah ke Sekolah:** {input_jarak} km")
if st.button("🔍 Cek Prediksi PPDB"):
    input_df = pd.DataFrame(
        [[input_nilai, input_jarak]],
        columns=["nilai_rata2", "jarak_km"]
    )

    hasil_prediksi = model.predict(input_df)[0]
    probabilitas = model.predict_proba(input_df)[0]
    tingkat_keyakinan = max(probabilitas) * 100

    if hasil_prediksi == "Lolos":
        st.success(
            f"✅ **HASIL PREDIKSI: LOLOS**\n\n"
            f"Tingkat keyakinan sistem: **{tingkat_keyakinan:.1f}%**"
        )
    else:
        st.error(
            f"❌ **HASIL PREDIKSI: TIDAK LOLOS / WAITING LIST**\n\n"
            f"Tingkat keyakinan sistem: **{tingkat_keyakinan:.1f}%**"
        )
        st.info(
            "💡 **Saran:** Pertimbangkan sekolah dengan jarak zonasi "
            "yang lebih dekat dari tempat tinggal."
        )

    st.caption(
        "Hasil prediksi ini digunakan sebagai **alat bantu informasi awal** "
        "dan tidak menggantikan keputusan resmi panitia PPDB."
    )
    
with st.expander("📁 Lihat Data Historis PPDB (Simulasi)"):
    st.dataframe(df)
