import streamlit as st
import pandas as pd
from groq import Groq
from datetime import datetime

st.set_page_config(
    page_title="PT. Aneka Warna Indah | AI Service",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

GROQ_API_KEY = "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"

# ==================== CSS PROFESSIONAL ====================
st.markdown("""
<style>
    .main-header {
        font-size: 3.2rem;
        background: linear-gradient(90deg, #1e3a8a, #3b82f6, #1e40af);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 800;
        margin-bottom: 10px;
    }
    .tagline {
        font-size: 1.6rem;
        color: #475569;
        text-align: center;
        margin-bottom: 40px;
    }
    .hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e40af 100%);
        color: white;
        padding: 80px 40px;
        border-radius: 30px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 20px 40px rgba(30, 64, 175, 0.3);
    }
    .service-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        text-align: center;
        transition: all 0.3s;
    }
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    .stButton>button {
        height: 3.8em;
        border-radius: 50px;
        font-weight: bold;
        font-size: 1.1em;
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=180)

st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
st.markdown("<p class='tagline'>AI Service Assistant • Bantu Anda 24/7</p>", unsafe_allow_html=True)

# ==================== HERO SECTION ====================
st.markdown("""
<div class="hero">
    <h2 style="color:white; font-size:2.8rem;">🤖 Halo, Saya Robot Teknisi AI</h2>
    <p style="font-size:1.4rem; margin:20px 0; color:#e0f2fe;">
        Saya siap membantu Anda mengatasi segala masalah mesin digital printing.<br>
        Dari troubleshooting sampai rekomendasi sparepart.
    </p>
    <p style="font-size:1.1rem; color:#bae6fd;">Pilih layanan di bawah ini</p>
</div>
""", unsafe_allow_html=True)

# Menu Utama
st.markdown("### 🚀 Layanan Kami")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💬 Chat Troubleshooting", use_container_width=True):
        st.session_state.page = "chat"

with col2:
    if st.button("🔍 Cek Sparepart", use_container_width=True):
        st.session_state.page = "sparepart"

with col3:
    if st.button("🏢 Cabang Kami", use_container_width=True):
        st.session_state.page = "cabang"

with col4:
    if st.button("📞 Hubungi Sales", use_container_width=True):
        st.session_state.page = "sales"

# ==================== CHAT PAGE ====================
if st.session_state.get('page') == "chat":
    st.subheader("💬 Chat Troubleshooting Mesin")
    st.caption("🤖 Analisa berdasarkan database tiketing service tim teknisi")

    mesin = st.selectbox("Pilih Mesin", [
        "Allwin Indoor", "Allwin Outdoor", "Epson SureColor", 
        "HP Latex", "Cutting JWEI", "Cutting Saga"
    ])

    question = st.text_area("Jelaskan masalah yang dialami mesin Anda:", height=150)

    if st.button("🚀 Kirim ke Robot Teknisi", type="primary", use_container_width=True):
        if question:
            with st.spinner("Robot Teknisi sedang menganalisa..."):
                try:
                    client = Groq(api_key=GROQ_API_KEY)
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": f"""Anda adalah robot teknisi profesional PT. Aneka Warna Indah.
Mesin: {mesin}
Pertanyaan customer: {question}
Jawab dengan ramah, jelas, langkah demi langkah, dan mudah dipahami."""}],
                        temperature=0.4,
                        max_tokens=800
                    )
                    st.success("✅ Jawaban Robot Teknisi AI")
                    st.markdown(response.choices[0].message.content)
                except:
                    st.error("Maaf, sedang ada gangguan. Coba lagi sebentar.")

# ==================== HALAMAN LAIN ====================
elif st.session_state.get('page') == "sparepart":
    st.subheader("🔍 Cek Ketersediaan Sparepart")
    st.info("Fitur ini sedang dalam pengembangan.")

elif st.session_state.get('page') == "cabang":
    st.subheader("🏢 Cabang PT. Aneka Warna Indah")
    st.info("Fitur ini sedang dalam pengembangan.")

elif st.session_state.get('page') == "sales":
    st.subheader("📞 Hubungi Sales")
    st.info("Fitur ini sedang dalam pengembangan.")

# ==================== INTERNAL ====================
if st.sidebar.button("🔧 Internal Analisis (Staff Only)"):
    st.session_state.page = "internal"

if st.session_state.get('page') == "internal":
    st.header("🔒 Internal - Analisis Laporan")
    password = st.text_input("Masukkan Password", type="password")
    if password == "admin123":
        st.success("✅ Akses Diterima")
        uploaded_file = st.file_uploader("Upload Excel Inistate", type=["xlsx", "xls"])
        if uploaded_file:
            df = pd.read_excel(uploaded_file)
            st.success(f"✅ Berhasil membaca {len(df)} baris")
            st.dataframe(df.head(10), use_container_width=True)
            if st.button("Update Knowledge Base"):
                st.session_state.knowledge_base = str(df.head(200).to_string())
                st.success("✅ Knowledge base berhasil diupdate!")
    else:
        st.error("Password salah")

st.caption("PT. Aneka Warna Indah © 2026 | AI Customer Service Assistant")