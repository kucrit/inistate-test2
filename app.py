import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

GROQ_API_KEY = "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"

# CSS
st.markdown("""
<style>
    .main-header {font-size: 2.8rem; background: linear-gradient(90deg, #d32f2f, #1976d2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.4rem; color: #444; text-align: center; margin-bottom: 30px;}
    .hero-box {background: linear-gradient(135deg, #f0f7ff, #e3f2fd); padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.1);}
    .stButton>button {height: 3.5em; border-radius: 12px; font-weight: bold;}
    html {scroll-behavior: smooth;}
</style>
""", unsafe_allow_html=True)

# Header
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=120)
with col_title:
    st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Solusi Digital Printing & Service Mesin Terpercaya</p>", unsafe_allow_html=True)

st.markdown("---")

# Hero Section - Robot Teknisi
st.markdown("""
<div class="hero-box">
    <h2>🤖 Halo, saya Robot Teknisi AI</h2>
    <h3>Saya siap membantu Anda menyelesaikan masalah mesin dengan cepat!</h3>
    <p style="font-size: 1.2rem; margin-top: 15px;">Tinggal pilih menu di bawah ini</p>
</div>
""", unsafe_allow_html=True)

# Menu Utama
st.markdown("### Pilih Layanan")
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8, _ = st.columns(3)

with col1:
    if st.button("🔍 Cek Sparepart", use_container_width=True):
        st.session_state.current_page = "Sparepart"
        st.markdown("<script>window.scrollTo({top: document.getElementById('sparepart').offsetTop - 100, behavior: 'smooth'});</script>", unsafe_allow_html=True)

with col2:
    if st.button("💬 Chat Troubleshooting", use_container_width=True):
        st.session_state.current_page = "Troubleshooting"

with col3:
    if st.button("🏢 Cabang Kami", use_container_width=True):
        st.session_state.current_page = "Cabang"

with col4:
    if st.button("📞 Hubungi Sales", use_container_width=True):
        st.session_state.current_page = "Sales"
with col5:
    if st.button("📚 Katalog & Harga", use_container_width=True):
        st.session_state.current_page = "Katalog"
with col6:
    if st.button("🎓 Training & Tutorial", use_container_width=True):
        st.session_state.current_page = "Training"

with col7:
    if st.button("📊 Status Service", use_container_width=True):
        st.session_state.current_page = "Status"
with col8:
    if st.button("⭐ Testimoni Pelanggan", use_container_width=True):
        st.session_state.current_page = "Testimoni"

# ==================== HALAMAN LAIN ====================

if st.session_state.get('current_page') == "Troubleshooting":
    st.subheader("💬 Chat Troubleshooting Mesin")
    st.info("**Analisa troubleshoot berdasarkan rekap dari tiketing service oleh tim teknisi**")
    # ... (kode chat AI tetap sama)

elif st.session_state.get('current_page') == "Sparepart":
    st.subheader("🔍 Cek Ketersediaan Sparepart")
    st.info("Fitur ini sedang dalam pengembangan.")

elif st.session_state.get('current_page') == "Cabang":
    st.subheader("🏢 Cabang PT. Aneka Warna Indah")
    st.info("Fitur ini sedang dalam pengembangan.")

elif st.session_state.get('current_page') in ["Sales", "Katalog", "Training"]:
    st.info("Fitur ini sedang dalam pengembangan.")

elif st.session_state.get('current_page') == "Status":
    st.subheader("📊 Status Service")
    tiket = st.text_input("Masukkan No. Tiket Service Inistate Anda")
    if st.button("Cek Status"):
        st.info("Fitur ini sedang dalam pengembangan.")

elif st.session_state.get('current_page') == "Testimoni":
    st.subheader("⭐ Testimoni Pelanggan")
    st.write("**Apa kata pelanggan kami?**")
    col_r1, col_r2, col_r3 = st.columns(3)
    with col_r1:
        st.success("★★★★★\nSangat puas dengan service cepat!")
    with col_r2:
        st.success("★★★★☆\nTeknisi ramah dan profesional.")
    with col_r3:
        st.success("★★★★★\nMesin kembali normal dalam 1 hari.")

# Internal
if st.sidebar.button("🔧 Internal Analisis (Staff Only)"):
    st.session_state.current_page = "Internal"

if st.session_state.get('current_page') == "Internal":
    st.header("🔒 Internal - Analisis Laporan")
    password = st.text_input("Masukkan Password", type="password")
    if password == "admin123":
        st.success("✅ Akses Diterima")
        uploaded_file = st.file_uploader("Upload Excel Inistate", type=["xlsx", "xls"])
        if uploaded_file:
            df = pd.read_excel(uploaded_file)
            st.success(f"✅ {len(df)} baris data")
            st.dataframe(df.head(10), use_container_width=True)
            if st.button("🚀 Update Knowledge Base"):
                st.session_state.knowledge_base = str(df.head(200).to_string())
                st.success("✅ Knowledge base berhasil diupdate!")
    else:
        st.error("Password salah")

st.caption("PT. Aneka Warna Indah © 2026 | AI Customer Service")