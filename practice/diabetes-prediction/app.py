"""
Diabetes Prediction App (Streamlit)

Deskripsi:
Aplikasi ini digunakan untuk memprediksi potensi diabetes berdasarkan data pasien
menggunakan model Decision Tree yang telah dilatih sebelumnya.

Pipeline:
Input User → Preprocessing (Scaling) → Model Prediction → Output Probabilitas

Catatan:
- Model dan scaler harus konsisten dengan proses training
- Scaling wajib karena digunakan saat training
"""

import streamlit as st
import numpy as np
import joblib
from pathlib import Path


# =========================
# CONFIGURATION
# =========================
# Mengatur konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Prediksi Diabetes",
    page_icon="🩺",
    layout="centered"
)


# =========================
# LOAD MODEL & SCALER
# =========================
# Menentukan path direktori saat ini
BASE_DIR = Path(__file__).resolve().parent

# Folder penyimpanan artifact model
MODEL_DIR = BASE_DIR / "models"

# Load model dan scaler (harus sesuai dengan training pipeline)
model = joblib.load(MODEL_DIR / "decision_tree_model.joblib")
scaler = joblib.load(MODEL_DIR / "scaler.joblib")


# =========================
# USER INTERFACE (HEADER)
# =========================
st.title("🩺 Prediksi Diabetes (Decision Tree)")
st.markdown(
    "Masukkan data pasien untuk memprediksi potensi **diabetes**."
)

st.markdown("---")
st.subheader("📋 Input Data Pasien")


# =========================
# INPUT FORM
# =========================
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input(
        "Jumlah Kehamilan", min_value=0, step=1,
        help="Jumlah kehamilan yang pernah dialami pasien"
    )
    Glucose = st.number_input(
        "Glukosa (mg/dL)", min_value=0.0,
        help="Kadar glukosa darah pasien"
    )
    BloodPressure = st.number_input(
        "Tekanan Darah (mm Hg)", min_value=0.0,
        help="Tekanan darah diastolik"
    )
    SkinThickness = st.number_input(
        "Skin Thickness (mm)", min_value=0.0,
        help="Ketebalan lipatan kulit"
    )

with col2:
    Insulin = st.number_input(
        "Insulin (mu U/mL)", min_value=0.0,
        help="Kadar insulin dalam darah"
    )
    BMI = st.number_input(
        "BMI", min_value=0.0,
        help="Indeks Massa Tubuh"
    )
    DiabetesPedigreeFunction = st.number_input(
        "Diabetes Pedigree", min_value=0.0,
        help="Riwayat diabetes keluarga"
    )
    Age = st.number_input(
        "Usia", min_value=0, step=1,
        help="Usia pasien dalam tahun"
    )


# =========================
# PREDICTION LOGIC
# =========================
st.markdown("---")

if st.button("🔍 Prediksi"):
    # Menggabungkan input user menjadi array
    input_data = np.array([[
        Pregnancies, Glucose, BloodPressure, SkinThickness,
        Insulin, BMI, DiabetesPedigreeFunction, Age
    ]])

    # =========================
    # PREPROCESSING
    # =========================
    # Scaling wajib agar konsisten dengan data training
    input_scaled = scaler.transform(input_data)

    # =========================
    # MODEL INFERENCE
    # =========================
    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    # =========================
    # OUTPUT RESULT
    # =========================
    st.subheader("🧾 Hasil Prediksi")

    if prediction == 1:
        st.error(
            f"Pasien berpotensi diabetes\n\n"
            f"Probabilitas: {prob:.2f}"
        )
    else:
        st.success(
            f"Pasien tidak diabetes\n\n"
            f"Probabilitas: {prob:.2f}"
        )