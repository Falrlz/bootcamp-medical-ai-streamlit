"""
BMI Calculator - Streamlit Application

Deskripsi:
Aplikasi ini digunakan untuk menghitung Body Mass Index (BMI) berdasarkan
tinggi badan (cm) dan berat badan (kg), serta memberikan interpretasi kategori BMI.

Fitur:
- Input nama pengguna
- Input tinggi dan berat badan
- Perhitungan BMI otomatis
- Klasifikasi BMI berdasarkan standar WHO
- Feedback dinamis berbasis kategori BMI
"""

import streamlit as st


# =========================
# CONFIGURATION
# =========================
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚕️",
    layout="centered"
)


# =========================
# CORE FUNCTIONS
# =========================
def hitung_bmi(berat: float, tinggi_cm: float) -> float:
    """
    Menghitung nilai Body Mass Index (BMI).

    Formula:
        BMI = berat (kg) / (tinggi (m))^2

    Parameters:
        berat (float): Berat badan dalam kilogram
        tinggi_cm (float): Tinggi badan dalam centimeter

    Returns:
        float: Nilai BMI

    Raises:
        ZeroDivisionError: Jika tinggi = 0
    """
    tinggi_m = tinggi_cm / 100
    return berat / (tinggi_m ** 2)


def kategori_bmi(bmi: float) -> tuple[str, str]:
    """
    Menentukan kategori BMI berdasarkan standar WHO.

    Kategori:
        - < 18.5        : Underweight
        - 18.5 - 24.9   : Normal
        - 25 - 29.9     : Overweight
        - >= 30         : Obese

    Parameters:
        bmi (float): Nilai BMI

    Returns:
        tuple[str, str]:
            - kategori (str): Nama kategori BMI
            - status_ui (str): Tipe notifikasi Streamlit (success, warning, error)
    """
    if bmi < 18.5:
        return "Underweight", "warning"
    elif 18.5 <= bmi < 25:
        return "Normal", "success"
    elif 25 <= bmi < 30:
        return "Overweight", "warning"
    else:
        return "Obese", "error"


# =========================
# USER INTERFACE (UI)
# =========================
st.title("⚖️ BMI Calculator")
st.caption("Hitung Body Mass Index berdasarkan tinggi dan berat badan")

# Container utama untuk input user
with st.container():
    # Input nama
    nama = st.text_input(
        "Nama",
        placeholder="Masukkan nama Anda"
    )

    # Layout 2 kolom untuk input numerik
    col1, col2 = st.columns(2)

    with col1:
        tinggi = st.number_input(
            "Tinggi (cm)",
            min_value=0.0,
            max_value=300.0,
            step=0.1,
            help="Masukkan tinggi badan dalam centimeter"
        )

    with col2:
        berat = st.number_input(
            "Berat (kg)",
            min_value=0.0,
            max_value=300.0,
            step=0.1,
            help="Masukkan berat badan dalam kilogram"
        )

    # Tombol eksekusi
    hitung = st.button(
        "Hitung BMI",
        use_container_width=True
    )


# =========================
# BUSINESS LOGIC
# =========================
if hitung:
    # Validasi nama
    if not nama.strip():
        st.warning("Nama tidak boleh kosong")
        st.stop()  # menghentikan eksekusi lebih lanjut

    # Validasi input numerik
    if tinggi <= 0 or berat <= 0:
        st.error("Tinggi dan berat harus lebih dari 0")
        st.stop()

    # Perhitungan BMI
    bmi = hitung_bmi(berat, tinggi)

    # Klasifikasi BMI
    kategori, status = kategori_bmi(bmi)

    # =========================
    # OUTPUT / RESULT
    # =========================
    st.divider()
    st.subheader("Hasil Perhitungan")

    # Menampilkan nilai BMI dalam bentuk metrik
    st.metric(
        label="Nilai BMI",
        value=f"{bmi:.2f}"
    )

    # Menampilkan kategori BMI
    st.write(f"**{nama}**, kategori BMI Anda adalah: **{kategori}**")

    # Mapping pesan berdasarkan kategori
    pesan = {
        "Underweight": "Berat badan Anda kurang. Perhatikan asupan nutrisi.",
        "Normal": "Berat badan Anda ideal. Pertahankan gaya hidup sehat.",
        "Overweight": "Berat badan Anda berlebih. Mulai perbaiki pola makan dan aktivitas fisik.",
        "Obese": "Anda termasuk obesitas. Disarankan konsultasi dengan tenaga medis."
    }

    # Menampilkan feedback dinamis menggunakan Streamlit API
    getattr(st, status)(pesan[kategori])