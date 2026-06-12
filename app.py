import streamlit as st
import pandas as pd
from groq import Groq
import os

# Konfigurasi Tampilan Modern
st.set_page_config(
    page_title="AI Inistate Troubleshooting",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Desain Lebih Keren
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(90deg, #00c853, #0288d1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 1.4rem;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00c853, #0288d1);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        height: 3.2em;
        font-size: 1.1em;
    }
    .success-box {
        background-color: #e8f5e9;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #00c853;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>🤖 AI TROUBLESHOOTING INISTATE</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Asisten Cerdas untuk Tim Teknis Mesin • Lebih Cepat • Lebih Akurat</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/repair.png", width=90)
    st.header("⚙️ Pengaturan AI")
    api_key = st.text_input("Groq API Key", type="password", value=os.getenv("GROQ_API_KEY", ""))
    
    if st.button("💾 Simpan API Key"):
        os.environ["GROQ_API_KEY"] = api_key
        st.success("✅ API Key tersimpan!")

    st.divider()
    st.info("🔧 Aplikasi ini membantu teknisi mengatasi error lebih cepat")

# Fungsi Analisis
def summarize_errors(df):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    df_clean = df.head(150).fillna("").astype(str)
    text_data = df_clean.apply(lambda row: ' | '.join(row), axis=1).tolist()
    combined = "\n".join(text_data)
    
    prompt = f"""Kamu adalah teknisi mesin senior berpengalaman. Analisis laporan error berikut dan buat ringkasan yang jelas dalam Bahasa Indonesia:

{combined}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=1000
    )
    return response.choices[0].message.content

# Tabs
tab1, tab2 = st.tabs(["📊 ANALISIS LAPORAN", "💬 CHAT TROUBLESHOOTING"])

with tab1:
    uploaded_file = st.file_uploader("Upload File Excel dari Inistate", type=["xlsx", "xls"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.success(f"✅ Berhasil memuat {len(df)} baris laporan")
        st.dataframe(df.head(10), use_container_width=True)
        
        num_rows = st.slider("Jumlah baris yang dianalisis", 50, 300, 120)
        
        if st.button("🚀 Mulai Analisis dengan AI", type="primary"):
            if not os.environ.get("GROQ_API_KEY"):
                st.error("❌ Masukkan Groq API Key terlebih dahulu!")
            else:
                with st.spinner("AI sedang menganalisis semua error..."):
                    summary = summarize_errors(df.head(num_rows))
                    st.subheader("📋 Hasil Ringkasan AI")
                    st.markdown(summary)
                    
                    if "knowledge_base" not in st.session_state:
                        st.session_state.knowledge_base = summary

with tab2:
    st.subheader("💬 Tanya AI Troubleshooting")
    if "knowledge_base" not in st.session_state:
        st.warning("Upload Excel dan lakukan analisis dulu di tab pertama.")
    else:
        question = st.text_input("Ketik masalah/error yang dialami:", 
                               placeholder="Contoh: Motor tidak berputar, error code E01...")
        
        if st.button("Kirim ke AI"):
            if question:
                client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
                prompt = f"""Jawab sebagai teknisi senior yang ramah.

Pengetahuan dari data Inistate:
{st.session_state.knowledge_base}

Pertanyaan: {question}

Berikan jawaban langkah demi langkah yang mudah dipahami teknisi lapangan."""

                with st.spinner("AI sedang memproses jawaban..."):
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.4,
                    )
                    st.success("✅ Jawaban AI")
                    st.markdown(response.choices[0].message.content)

st.caption("AI Troubleshooting Inistate © 2026 • Versi Desain Modern")