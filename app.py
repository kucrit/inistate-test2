import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

GROQ_API_KEY = "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"

# CSS Responsif Mobile
st.markdown("""
<style>
    .main-header {font-size: 2.6rem; background: linear-gradient(90deg, #d32f2f, #1976d2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.3rem; color: #555; text-align: center;}
    .hero-box {background: linear-gradient(135deg, #fff0f0, #f0f7ff); padding: 25px; border-radius: 15px; text-align: center;}
    .stButton>button {background: linear-gradient(90deg, #d32f2f, #1976d2); color: white; font-size: 1.1em; height: 3.5em; border-radius: 12px;}
    @media (max-width: 768px) {
        .main-header {font-size: 2.1rem;}
        .stButton>button {height: 3em; font-size: 1em;}
    }
</style>
""", unsafe_allow_html=True)

# Header
st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", use_column_width=True)

st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Solusi Digital Printing & Service Mesin Terpercaya</p>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="hero-box">
    <h3>👋 Selamat Datang di Asisten AI</h3>
    <p>Chat disini, aku siap membantumu dengan cepat</p>
</div>
""", unsafe_allow_html=True)

# Menu Utama
st.markdown("### Pilih Layanan")
col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Cek Sparepart", use_container_width=True):
        st.session_state.page = "Sparepart"

with col2:
    if st.button("💬 Chat Troubleshooting", use_container_width=True):
        st.session_state.page = "Troubleshooting"

# ==================== SPAREPART ====================
if st.session_state.get('page') == "Sparepart":
    st.subheader("🔍 Cek Ketersediaan Sparepart")
    st.info("Fitur ini sedang dalam pengembangan.\nKami akan segera menghubungkan ke website resmi.")

# ==================== CHAT TROUBLESHOOTING (Mobile Friendly) ====================
if st.session_state.get('page') == "Troubleshooting":
    st.subheader("💬 Chat Troubleshooting Mesin")
    
    mesin = st.selectbox("Pilih Jenis Mesin", [
        "Allwin Indoor", "Allwin Outdoor", "Epson SureColor", 
        "HP Latex", "Cutting JWEI", "Cutting Saga"
    ], key="mesin_key")
    
    st.markdown("### 🤖 Asisten AI Siap Membantu")
    
    if "knowledge_base" not in st.session_state:
        st.warning("⚠️ Tim Internal belum mengupdate rangkuman laporan. Silakan hubungi tim internal.")
    else:
        question = st.text_area("Jelaskan masalah yang Anda alami:", 
                              placeholder="Contoh: Printhead sering mampet...", height=120)
        
        if st.button("🚀 Kirim ke Asisten AI", type="primary", use_container_width=True):
            if question:
                try:
                    with st.spinner("Asisten AI sedang memproses..."):
                        client = Groq(api_key=GROQ_API_KEY)
                        prompt = f"""Mesin: {mesin}
Pengetahuan teknisi: {st.session_state.get('knowledge_base', '')[:7000]}

Pertanyaan: {question}

Jawab singkat, jelas, langkah demi langkah, dan ramah."""

                        response = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[{"role": "user", "content": prompt}],
                            temperature=0.4,
                            max_tokens=700
                        )
                        st.success("✅ Jawaban Asisten AI:")
                        st.markdown(response.choices[0].message.content)
                except:
                    st.error("Maaf, sedang sibuk. Coba lagi sebentar.")

# ==================== INTERNAL (Sidebar) ====================
if st.sidebar.button("🔧 Internal Analisis (Staff Only)"):
    st.session_state.page = "Internal"

if st.session_state.get('page') == "Internal":
    st.header("🔒 Internal - Analisis Laporan")
    password