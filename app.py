import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

# ==================== API KEY ====================
GROQ_API_KEY = "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"

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 3.2rem; background: linear-gradient(90deg, #1e88e5, #00c853); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.5rem; color: #555; text-align: center; margin-bottom: 30px;}
    .hero-box {background: linear-gradient(135deg, #f0f7ff, #e8f5e9); padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.1);}
    .stButton>button {background: linear-gradient(90deg, #1e88e5, #00c853); color: white; font-size: 1.2em; height: 4em; border-radius: 15px;}
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=130)
with col2:
    st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Solusi Digital Printing & Service Mesin Terpercaya</p>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="hero-box">
    <h2>👋 Halo! Selamat Datang</h2>
    <h3>Asisten Customer Service AI</h3>
    <p style="font-size: 1.3rem;">Chat disini, aku siap membantumu</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Pilih Layanan")

# Menu Utama
col_a, col_b, col_c = st.columns(3)

with col_a:
    if st.button("💬 Chat Troubleshooting Mesin", use_container_width=True):
        st.session_state.page = "Chat"
with col_b:
    if st.button("🛠️ Pilih Jenis Mesin", use_container_width=True):
        st.session_state.page = "Mesin"
with col_c:
    if st.button("🔧 Internal Analisis", use_container_width=True):
        st.session_state.page = "Internal"

# ==================== CHAT PAGE ====================
if st.session_state.get('page') in ["Chat", "Mesin"]:
    st.markdown("### 💬 Chat dengan Asisten AI")
    
    mesin = st.selectbox("Pilih Merk Mesin", [
        "Allwin Indoor", "Allwin Outdoor", "Epson SureColor", 
        "HP Latex", "Cutting JWEI", "Cutting Saga"
    ])
    
    question = st.text_input("Jelaskan masalah yang dialami:", 
                           placeholder="Contoh: Printhead Allwin Indoor mampet...")
    
    if st.button("Kirim Pertanyaan", type="primary"):
        if question:
            with st.spinner("Asisten AI sedang memproses..."):
                client = Groq(api_key=GROQ_API_KEY)
                kb = st.session_state.get('knowledge_base', 'Data teknisi internal.')
                prompt = f"""Kamu adalah asisten customer service PT. Aneka Warna Indah yang ramah dan profesional.

Mesin: {mesin}
Pengetahuan teknisi: {kb}
Pertanyaan: {question}

Jawab dengan bahasa yang mudah dipahami dan langkah demi langkah."""
                
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.4,
                )
                st.success("✅ Jawaban Asisten AI:")
                st.markdown(response.choices[0].message.content)

# ==================== INTERNAL PAGE ====================
elif st.session_state.get('page') == "Internal":
    st.header("🔧 Internal - Analisis Laporan Inistate")
    uploaded_file = st.file_uploader("Upload Excel dari Inistate", type=["xlsx", "xls"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.success(f"✅ Berhasil membaca {len(df)} baris")
        st.dataframe(df.head(10), use_container_width=True)
        
        if st.button("🚀 Analisis & Update Knowledge Base"):
            with st.spinner("Sedang memproses..."):
                st.session_state.knowledge_base = str(df.head(150).to_string())
                st.success("✅ Knowledge base berhasil diupdate!")

st.caption("PT. Aneka Warna Indah © 2026")