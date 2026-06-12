import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

GROQ_API_KEY = "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"

# CSS Profesional + Dark Mode Support
st.markdown("""
<style>
    .main-header {font-size: 2.8rem; background: linear-gradient(90deg, #d32f2f, #1976d2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.4rem; color: #666; text-align: center;}
    .hero-box {background: linear-gradient(135deg, #f8f9fa, #e3f2fd); padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.08);}
    .stButton>button {height: 3.6em; border-radius: 12px; font-weight: bold;}
    @media (max-width: 768px) {
        .main-header {font-size: 2.1rem;}
    }
    /* Dark Mode Support */
    [data-theme="dark"] .hero-box {background: linear-gradient(135deg, #2a2a2a, #1e3a5f);}
    [data-theme="dark"] .sub-header {color: #ccc;}
</style>
""", unsafe_allow_html=True)

# Header & Landing Page Profesional
st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", use_column_width=True)

st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Solusi Digital Printing & Service Mesin Terpercaya sejak 2010</p>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="hero-box">
    <h2>👋 Selamat Datang di Asisten AI Resmi</h2>
    <h3>Kami siap membantu Anda dengan cepat dan profesional</h3>
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

# ==================== CABANG ====================
if st.session_state.get('page') == "Cabang":
    st.subheader("🏢 Pilih Cabang PT. Aneka Warna Indah")
    
    cabang = st.selectbox("Pilih Cabang", [
        "Jakarta", "Jawa Barat", "Jawa Tengah", "Jawa Timur",
        "Pontianak", "Pekanbaru", "Medan"
    ])
    
    wa_numbers = {
        "Jakarta": "0821xxx",
        "Jawa Barat": "0821xxx",
        "Jawa Tengah": "0821xxx",
        "Jawa Timur": "0821xxx",
        "Pontianak": "0821xxx",
        "Pekanbaru": "0821xxx",
        "Medan": "0821xxx"
    }
    
    st.success(f"**Cabang {cabang}**")
    st.write(f"📞 Service Center: **{wa_numbers[cabang]}**")
    
    if st.button("💬 Hubungi via WhatsApp", type="primary", use_container_width=True):
        st.success("📲 Silakan hubungi nomor di atas melalui WhatsApp")

# ==================== SPAREPART ====================
if st.session_state.get('page') == "Sparepart":
    st.subheader("🔍 Cek Ketersediaan Sparepart")
    st.info("Fitur ini sedang dalam pengembangan.\nKami akan segera menghubungkan ke website resmi.")

# ==================== CHAT TROUBLESHOOTING ====================
if st.session_state.get('page') == "Troubleshooting":
    st.subheader("💬 Chat Troubleshooting Mesin")
    
    mesin = st.selectbox("Pilih Jenis Mesin", [
        "Allwin Indoor", "Allwin Outdoor", "Epson SureColor", 
        "HP Latex", "Cutting JWEI", "Cutting Saga"
    ])
    
    st.markdown("### 🤖 Asisten AI Siap Membantu")
    
    question = st.text_area("Jelaskan masalah yang Anda alami:", 
                          placeholder="Contoh: Printhead sering mampet...", height=130)
    
    if st.button("🚀 Kirim ke Asisten AI", type="primary", use_container_width=True):
        if question:
            with st.spinner("Asisten AI sedang memproses..."):
                try:
                    client = Groq(api_key=GROQ_API_KEY)
                    kb = st.session_state.get('knowledge_base', 'Saya teknisi berpengalaman PT. Aneka Warna Indah.')
                    prompt = f"""Mesin: {mesin}
Pengetahuan teknisi: {kb[:7000]}

Pertanyaan: {question}

Jawab dengan ramah, jelas, dan langkah demi langkah."""
                    
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

# ==================== INTERNAL ====================
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