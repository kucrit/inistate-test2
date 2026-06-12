import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

GROQ_API_KEY = "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"

# CSS Khusus Mobile Friendly
st.markdown("""
<style>
    .main-header {font-size: 2.4rem; background: linear-gradient(90deg, #d32f2f, #1976d2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.3rem; color: #555; text-align: center;}
    .hero-box {background: linear-gradient(135deg, #fff0f0, #f0f7ff); padding: 25px; border-radius: 15px; text-align: center; margin: 15px 0;}
    .stButton>button {height: 3.4em; border-radius: 12px; font-size: 1.05em;}
    @media (max-width: 768px) {
        .main-header {font-size: 2rem;}
        .stButton>button {height: 3em;}
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

tab1, tab2 = st.tabs(["🔍 Cek Sparepart", "💬 Chat Troubleshooting"])

# ==================== TAB SPAREPART ====================
with tab1:
    st.subheader("🔍 Cek Ketersediaan Sparepart")
    st.info("Fitur ini sedang dalam pengembangan.\nKami akan segera menghubungkan ke website resmi.")

# ==================== TAB CHAT TROUBLESHOOTING ====================
with tab2:
    st.subheader("💬 Chat Troubleshooting Mesin")
    
    mesin = st.selectbox("Pilih Jenis Mesin", [
        "Allwin Indoor", "Allwin Outdoor", "Epson SureColor", 
        "HP Latex", "Cutting JWEI", "Cutting Saga"
    ])
    
    st.markdown("### 🤖 Asisten AI Siap Membantu")
    
    question = st.text_area("Jelaskan masalah yang Anda alami:", 
                          placeholder="Contoh: Printhead sering mampet pada Allwin Indoor...", height=130)
    
    if st.button("🚀 Kirim ke Asisten AI", type="primary", use_container_width=True):
        if question:
            with st.spinner("Asisten AI sedang memproses jawaban..."):
                try:
                    client = Groq(api_key=GROQ_API_KEY)
                    kb = st.session_state.get('knowledge_base', 'Saya teknisi PT. Aneka Warna Indah.')
                    prompt = f"""Mesin: {mesin}
Pengetahuan: {kb[:6000]}

Pertanyaan: {question}

Jawab ramah, jelas, dan langkah demi langkah."""

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.4,
                        max_tokens=700
                    )
                    st.success("✅ Jawaban Asisten AI:")
                    st.markdown(response.choices[0].message.content)
                except:
                    st.error("Maaf, AI sedang sibuk. Coba lagi sebentar.")

# ==================== INTERNAL (Sidebar) ====================
if st.sidebar.button("🔧 Internal Analisis (Staff Only)"):
    st.session_state.page = "Internal"

if st.session_state.get('page') == "Internal":
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