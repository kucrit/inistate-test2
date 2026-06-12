import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

GROQ_API_KEY = "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"

# CSS Landing Page Profesional + Dark Mode
st.markdown("""
<style>
    .main-header {
        font-size: 3rem; 
        background: linear-gradient(90deg, #d32f2f, #1976d2); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        text-align: center; 
        font-weight: bold;
    }
    .sub-header {font-size: 1.5rem; text-align: center; margin-bottom: 30px;}
    .hero-box {
        background: linear-gradient(135deg, #f8f9fa, #e3f2fd); 
        padding: 50px 30px; 
        border-radius: 25px; 
        text-align: center; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    [data-theme="dark"] .hero-box {
        background: linear-gradient(135deg, #2a2a2a, #1e3a5f);
        color: white;
    }
    .stButton>button {
        height: 3.6em; 
        border-radius: 12px; 
        font-weight: bold;
    }
    @media (max-width: 768px) {
        .main-header {font-size: 2.2rem;}
    }
</style>
""", unsafe_allow_html=True)

# ==================== LANDING PAGE ====================
st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=200)

st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Solusi Digital Printing & Service Mesin Terpercaya sejak 2010</p>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="hero-box">
    <h2>👋 Selamat Datang di Asisten AI Resmi</h2>
    <h3>Kami siap membantu Anda dengan cepat dan profesional</h3>
    <p style="font-size: 1.2rem; margin-top: 15px;">Pilih layanan di bawah ini</p>
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

# ==================== HALAMAN LAINNYA ====================
if st.session_state.get('page') == "Sparepart":
    st.subheader("🔍 Cek Ketersediaan Sparepart")
    st.info("Fitur ini sedang dalam pengembangan.")

if st.session_state.get('page') == "Troubleshooting":
    st.subheader("💬 Chat Troubleshooting Mesin")
    mesin = st.selectbox("Pilih Jenis Mesin", ["Allwin Indoor", "Allwin Outdoor", "Epson SureColor", "HP Latex", "Cutting JWEI", "Cutting Saga"])
    question = st.text_area("Jelaskan masalah Anda:", height=120)
    if st.button("🚀 Kirim ke Asisten AI", type="primary"):
        st.info("Asisten AI sedang memproses... (fitur aktif)")

if st.session_state.get('page') == "Cabang":
    st.subheader("🏢 Cabang PT. Aneka Warna Indah")
    # (bisa dikembangkan lebih lanjut)

# Internal di Sidebar
if st.sidebar.button("🔧 Internal Analisis (Staff Only)"):
    st.session_state.page = "Internal"

if st.session_state.get('page') == "Internal":
    st.header("🔒 Internal - Analisis Laporan")
    password = st.text_input("Masukkan Password", type="password")
    if password == "admin123":
        st.success("Akses Diterima")
        # ... (kode internal tetap sama)

st.caption("PT. Aneka Warna Indah © 2026 | AI Customer Service")