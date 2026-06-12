import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

GROQ_API_KEY = "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"

# Force Light Theme + Landing Page Style
st.markdown("""
<style>
    body, .stApp {
        background-color: #f8fbff !important;
    }
    .main-header {
        font-size: 3.2rem;
        background: linear-gradient(90deg, #d32f2f, #1976d2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #444;
        text-align: center;
        margin-bottom: 40px;
    }
    .hero-box {
        background: linear-gradient(135deg, #ffffff, #f0f7ff);
        padding: 50px 30px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        margin: 30px 0;
        border: 1px solid #e0f0ff;
    }
    .stButton>button {
        background: linear-gradient(90deg, #d32f2f, #1976d2);
        color: white;
        height: 3.8em;
        border-radius: 15px;
        font-weight: bold;
        font-size: 1.1em;
    }
    @media (max-width: 768px) {
        .main-header {font-size: 2.3rem;}
    }
</style>
""", unsafe_allow_html=True)

# ==================== LANDING PAGE ====================
st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=220)

st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Solusi Digital Printing & Service Mesin Terpercaya</p>", unsafe_allow_html=True)

st.markdown("""
<div class="hero-box">
    <h2>🤖 Selamat Datang di Asisten AI Resmi</h2>
    <h3>Kami siap membantu Anda 24/7 dengan cepat dan profesional</h3>
    <p style="font-size: 1.25rem; margin-top: 20px;">Pilih layanan yang Anda butuhkan di bawah ini</p>
</div>
""", unsafe_allow_html=True)

# Menu Utama
st.markdown("### Pilih Layanan")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔍 Cek Sparepart", use_container_width=True):
        st.session_state.page = "Sparepart"

with col2:
    if st.button("💬 Chat Troubleshooting", use_container_width=True):
        st.session_state.page = "Troubleshooting"

with col3:
    if st.button("🏢 Cabang Kami", use_container_width=True):
        st.session_state.page = "Cabang"

# ==================== HALAMAN LAIN ====================
if st.session_state.get('page') == "Sparepart":
    st.subheader("🔍 Cek Ketersediaan Sparepart")
    st.info("Fitur ini sedang dalam pengembangan.")

if st.session_state.get('page') == "Troubleshooting":
    st.subheader("💬 Chat Troubleshooting Mesin")
    mesin = st.selectbox("Pilih Jenis Mesin", ["Allwin Indoor", "Allwin Outdoor", "Epson SureColor", "HP Latex", "Cutting JWEI", "Cutting Saga"])
    question = st.text_area("Jelaskan masalah yang Anda alami:", height=130)
    if st.button("🚀 Kirim ke Asisten AI", type="primary", use_container_width=True):
        st.info("Asisten AI sedang memproses jawaban...")

if st.session_state.get('page') == "Cabang":
    st.subheader("🏢 Cabang PT. Aneka Warna Indah")
    # (bisa dikembangkan nanti)

# Internal di Sidebar
if st.sidebar.button("🔧 Internal Analisis (Staff Only)"):
    st.session_state.page = "Internal"

if st.session_state.get('page') == "Internal":
    st.header("🔒 Internal Analisis")
    password = st.text_input("Password", type="password")
    if password == "admin123":
        st.success("Akses Diterima")
        # ... internal code

st.caption("PT. Aneka Warna Indah © 2026 | AI Customer Service")