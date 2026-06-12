import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

GROQ_API_KEY = "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"

# CSS + Typewriter Effect
st.markdown("""
<style>
    .main-header {font-size: 2.8rem; background: linear-gradient(90deg, #d32f2f, #1976d2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.4rem; color: #444; text-align: center; margin-bottom: 30px;}
    .hero-box {background: linear-gradient(135deg, #f0f7ff, #e3f2fd); padding: 45px; border-radius: 25px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1);}
    .typewriter {font-size: 1.3rem; color: #1e40af; min-height: 80px;}
    .stButton>button {height: 3.6em; border-radius: 12px; font-weight: bold;}
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

# Hero Section dengan Robot + Typewriter Effect
st.markdown("""
<div class="hero-box">
    <h2>🤖 Halo! Saya Robot Teknisi AI</h2>
    <p class="typewriter" id="typewriter"></p>
</div>

<script>
    const text = "Saya siap membantu Anda menyelesaikan masalah mesin dengan cepat dan akurat. Silakan pilih layanan di bawah ini 👇";
    let i = 0;
    const speed = 30;
    function typeWriter() {
        if (i < text.length) {
            document.getElementById("typewriter").innerHTML += text.charAt(i);
            i++;
            setTimeout(typeWriter, speed);
        }
    }
    typeWriter();
</script>
""", unsafe_allow_html=True)

# Menu Utama
st.markdown("### Pilih Layanan")
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8, _ = st.columns(3)

with col1:
    if st.button("🔍 Cek Sparepart", use_container_width=True, key="spare"):
        st.session_state.current_page = "Sparepart"
        st.markdown('<script>document.getElementById("section_spare").scrollIntoView({behavior: "smooth"});</script>', unsafe_allow_html=True)

with col2:
    if st.button("💬 Chat Troubleshooting", use_container_width=True, key="chat"):
        st.session_state.current_page = "Troubleshooting"

with col3:
    if st.button("🏢 Cabang Kami", use_container_width=True, key="cabang"):
        st.session_state.current_page = "Cabang"

with col4:
    if st.button("📞 Hubungi Sales", use_container_width=True, key="sales"):
        st.session_state.current_page = "Sales"
with col5:
    if st.button("📚 Katalog & Harga", use_container_width=True, key="katalog"):
        st.session_state.current_page = "Katalog"
with col6:
    if st.button("🎓 Training & Tutorial", use_container_width=True, key="training"):
        st.session_state.current_page = "Training"

with col7:
    if st.button("📊 Status Service", use_container_width=True, key="status"):
        st.session_state.current_page = "Status"
with col8:
    if st.button("⭐ Testimoni Pelanggan", use_container_width=True, key="testi"):
        st.session_state.current_page = "Testimoni"

# ==================== HALAMAN DENGAN ANCHOR ====================

if st.session_state.get('current_page') == "Troubleshooting":
    st.subheader("💬 Chat Troubleshooting Mesin")
    st.info("**Analisa troubleshoot berdasarkan rekap dari tiketing service oleh tim teknisi**")
    mesin = st.selectbox("Pilih Jenis Mesin", ["Allwin Indoor", "Allwin Outdoor", "Epson SureColor", "HP Latex", "Cutting JWEI", "Cutting Saga"])
    question = st.text_area("Jelaskan masalah yang Anda alami:", height=130)
    if st.button("🚀 Kirim ke Asisten AI", type="primary", use_container_width=True):
        st.info("Asisten AI sedang memproses jawaban...")

elif st.session_state.get('current_page') == "Sparepart":
    st.subheader("🔍 Cek Ketersediaan Sparepart", anchor="section_spare")
    st.info("Fitur ini sedang dalam pengembangan.")

# ... (menu lain tetap sama seperti sebelumnya)

st.caption("PT. Aneka Warna Indah © 2026 | AI Customer Service")