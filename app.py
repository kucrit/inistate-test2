import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

GROQ_API_KEY = "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"

# CSS Modern Mirip Barantum
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f0f7ff 0%, #e3f2fd 100%);
    }
    .main-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #334155;
        text-align: center;
        margin-bottom: 40px;
    }
    .hero-box {
        background: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
        margin: 30px 0;
    }
    .stButton>button {
        background: linear-gradient(90deg, #1e40af, #3b82f6);
        color: white;
        height: 3.8em;
        border-radius: 50px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ==================== LANDING PAGE ====================
st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Asisten AI Service Mesin Digital Printing 24/7</p>", unsafe_allow_html=True)

col_left, col_right = st.columns([5,4])

with col_left:
    st.markdown("""
    <div class="hero-box">
        <h2>Layani Pelanggan 24/7</h2>
        <h3>Tanpa Beban Tambahan dengan AI Service</h3>
        <p style="font-size:1.2rem; margin:20px 0;">
            Bukan sekadar chatbot — AI kami membantu teknisi dan pelanggan lebih cepat, 
            lebih akurat, dan lebih puas.
        </p>
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

with col_right:
    st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=300)

# ==================== HALAMAN LAIN ====================
if st.session_state.get('page') == "Sparepart":
    st.subheader("🔍 Cek Ketersediaan Sparepart")
    st.info("Fitur ini sedang dalam pengembangan.")

if st.session_state.get('page') == "Troubleshooting":
    st.subheader("💬 Chat Troubleshooting Mesin")
    mesin = st.selectbox("Pilih Jenis Mesin", ["Allwin Indoor", "Allwin Outdoor", "Epson SureColor", "HP Latex", "Cutting JWEI", "Cutting Saga"])
    question = st.text_area("Jelaskan masalah yang Anda alami:", height=120)
    if st.button("🚀 Kirim ke Asisten AI", type="primary"):
        st.info("Asisten AI sedang memproses jawaban...")

if st.session_state.get('page') == "Cabang":
    st.subheader("🏢 Cabang PT. Aneka Warna Indah")
    # (bisa dikembangkan)

# Internal
if st.sidebar.button("🔧 Internal Analisis (Staff Only)"):
    st.session_state.page = "Internal"

if st.session_state.get('page') == "Internal":
    st.header("🔒 Internal - Analisis Laporan")
    password = st.text_input("Masukkan Password", type="password")
    if password == "admin123":
        st.success("✅ Akses Diterima")
        # ... (kode internal)

st.caption("PT. Aneka Warna Indah © 2026 | AI Customer Service")