import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

GROQ_API_KEY = "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"

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 3rem; background: linear-gradient(90deg, #d32f2f, #1976d2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.5rem; color: #555; text-align: center; margin-bottom: 20px;}
    .hero-box {background: linear-gradient(135deg, #fff0f0, #f0f7ff); padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.1);}
    .stButton>button {background: linear-gradient(90deg, #d32f2f, #1976d2); color: white; font-size: 1.2em; height: 3.8em; border-radius: 12px; margin: 8px 0;}
    .logo {max-width: 180px; width: 100%; height: auto;}
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", use_column_width=True)
with col2:
    st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Solusi Digital Printing & Service Mesin Terpercaya</p>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="hero-box">
    <h2>👋 Selamat Datang di Asisten AI Kami</h2>
    <h3>Chat disini, aku siap membantumu dengan cepat</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("### Pilih Layanan")

# Menu Utama di Beranda
col_a, col_b = st.columns(2)

with col_a:
    if st.button("🔍 Cek Ketersediaan Sparepart", use_container_width=True):
        st.session_state.page = "Sparepart"

with col_b:
    if st.button("💬 Chat Troubleshooting Mesin", use_container_width=True):
        st.session_state.page = "Troubleshooting"

# ==================== SPAREPART ====================
if st.session_state.get('page') == "Sparepart":
    st.subheader("🔍 Cek Ketersediaan Sparepart")
    st.info("Fitur ini sedang dalam pengembangan. Kami akan segera menghubungkan ke website resmi sparepart.")
    st.button("Kunjungi Website Sparepart", disabled=True)

# ==================== CHAT TROUBLESHOOTING ====================
elif st.session_state.get('page') == "Troubleshooting":
    st.subheader("💬 Chat Troubleshooting Mesin")
    
    mesin = st.selectbox("Pilih Jenis Mesin", [
        "Allwin Indoor", "Allwin Outdoor", "Epson SureColor", 
        "HP Latex", "Cutting JWEI", "Cutting Saga"
    ])
    
    st.markdown("### 🤖 Asisten AI Siap Membantu")
    
    if "knowledge_base" not in st.session_state:
        st.warning("⚠️ Tim Internal belum mengupdate rangkuman laporan. Silakan hubungi tim internal.")
    else:
        question = st.text_input("Jelaskan masalah yang Anda alami:", 
                               placeholder="Contoh: Printhead sering mampet, tinta tidak keluar...")
        
        if st.button("Kirim ke Asisten AI", type="primary"):
            if question:
                with st.spinner("Asisten AI sedang memproses jawaban..."):
                    client = Groq(api_key=GROQ_API_KEY)
                    prompt = f"""Kamu adalah asisten customer service PT. Aneka Warna Indah yang ramah dan profesional.

Mesin: {mesin}
Pengetahuan teknisi internal: {st.session_state.get('knowledge_base', '')}

Pertanyaan customer: {question}

Jawab dengan bahasa yang mudah dipahami, sopan, dan berikan langkah penyelesaian yang jelas."""
                    
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.4,
                    )
                    st.success("✅ Jawaban Asisten AI:")
                    st.markdown(response.choices[0].message.content)

# ==================== INTERNAL MENU (di Sidebar) ====================
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