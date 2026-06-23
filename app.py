```python
import streamlit as st
import pandas as pd
import pickle

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Harga Beras Nasional",
    page_icon="🌾",
    layout="centered"
)

# Load model
model = pickle.load(open("model_beras.pkl", "rb"))

# Judul
st.title("🌾 Prediksi Harga Beras Nasional")
st.write(
    """
    Aplikasi ini memprediksi harga beras nasional menggunakan algoritma
    Random Forest berdasarkan harga cabai rawit merah, bawang merah,
    telur ayam ras, dan nilai tukar rupiah.
    """
)

st.subheader("Masukkan Data")

# Input pengguna
cabai = st.number_input(
    "Harga Cabai Rawit Merah (Rp/kg)",
    min_value=0.0,
    value=70000.0,
    step=1000.0
)

bawang = st.number_input(
    "Harga Bawang Merah (Rp/kg)",
    min_value=0.0,
    value=35000.0,
    step=1000.0
)

telur = st.number_input(
    "Harga Telur Ayam Ras (Rp/kg)",
    min_value=0.0,
    value=30000.0,
    step=1000.0
)

usd_idr = st.number_input(
    "Nilai Tukar Rupiah (USD/IDR)",
    min_value=0.0,
    value=16500.0,
    step=100.0
)

# Tombol prediksi
if st.button("Prediksi Harga Beras"):

    data_baru = pd.DataFrame({
        'Cabai': [cabai],
        'Bawang': [bawang],
        'Telur': [telur],
        'USD_IDR': [usd_idr]
    })

    hasil_prediksi = model.predict(data_baru)

    st.success(
        f"Prediksi Harga Beras Nasional = Rp {hasil_prediksi[0]:,.2f} per kg"
    )

# Footer
st.markdown("---")
st.caption(
    "Machine Learning Project - Random Forest untuk Prediksi Harga Beras Nasional"
)
```
