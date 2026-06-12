import streamlit as st
import pandas as pd
from groq import Groq
import os

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 2.8rem; background: linear-gradient(90deg, #1e88e5, #00c853); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center;}
    .customer-header {font-size: 2.5rem; color: #1e88e5; text-align: center;}
</style>
""", unsafe_allow_html=True)

# Navigation
page = st.sidebar.selectbox("Pilih Menu", 
    ["🏠 Beranda", "🔧 Internal - Analisis Laporan", "👥 Customer Service"])

# ==================== BERANDA ====================
if page == "🏠 Beranda":
    st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
    st.markdown("### Solusi Digital Printing & Teknologi Mesin Terbaik")
    st.image("https://img.icons8.com/fluency/400/000000/print.png", width=150)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Internal Staff** → Gunakan menu **Internal - Analisis Laporan**")
    with col2:
        st.info("**Customer** → Gunakan menu **Customer Service**")

# ==================== INTERNAL (Analisis Laporan) ====================
elif page == "🔧 Internal - Analisis Laporan":
    st.header("🔧 Internal - Analisis Laporan Inistate")
    
    api_key = st.text_input("Groq API Key", type="password", value=os.getenv("GROQ_API_KEY", ""))
    if st.button("Simpan API Key"):
        os.environ["GROQ_API_KEY"] = api_key
        st.success("✅ Tersimpan")

    uploaded_file = st.file_uploader("Upload Excel dari Inistate", type=["xlsx", "xls"])
    
    if uploaded_file and os.environ.get("GROQ_API_KEY"):
        df = pd.read_excel(uploaded_file)
        st.success(f"✅ {len(df)} baris data berhasil dibaca")
        st.dataframe(df.head(10), use_container_width=True)
        
        if st.button("🚀 Analisis dengan AI"):
            with st.spinner("AI sedang menganalisis..."):
                # (fungsi summarize_errors bisa ditambahkan lagi)
                st.info("Fitur analisis lengkap sedang diproses...")

# ==================== CUSTOMER SERVICE ====================
elif page == "👥 Customer Service":
    st.markdown("<h1 class='customer-header'>🤖 Customer Service - PT. Aneka Warna Indah</h1>", unsafe_allow_html=True)
    st.markdown("### Selamat datang! Silakan pilih bantuan yang Anda butuhkan")

    service = st.selectbox("Pilih Layanan", [
        "💬 Chat Troubleshooting Mesin",
        "🔍 Cek Ketersediaan Sparepart",
        "📍 Kontak Teknisi Daerah",
        "🏢 Profile Perusahaan",
        "🛠️ Pilih Jenis Mesin"
    ])

    if service == "💬 Chat Troubleshooting Mesin":
        st.subheader("Chat Troubleshooting")
        question = st.text_input("Jelaskan masalah mesin Anda:")
        if st.button("Kirim"):
            st.success("✅ Teknisi AI sedang memproses jawaban... (fitur ini masih menggunakan knowledge base)")

    elif service == "🔍 Cek Ketersediaan Sparepart":
        st.subheader("Cek Ketersediaan Sparepart")
        part = st.text_input("Masukkan nama sparepart (contoh: Printhead Allwin)")
        if st.button("Cek"):
            st.info("Fitur ini masih dalam pengembangan. Silakan hubungi admin.")

    elif service == "📍 Kontak Teknisi Daerah":
        st.subheader("Kontak Teknisi Daerah")
        st.write("**Teknisi Jawa Tengah & Sekitarnya:**")
        st.write("📞 08xx-xxxx-xxxx (Ayu / Tim Teknis)")
        st.write("📍 Magelang, Jawa Tengah")

    elif service == "🏢 Profile Perusahaan":
        st.subheader("Profile PT. Aneka Warna Indah")
        st.write("Kami adalah perusahaan spesialis mesin digital printing dengan pengalaman lebih dari 20 tahun.")
        st.write("Layanan: Penjualan, Service, Sparepart, Training.")

    elif service == "🛠️ Pilih Jenis Mesin":
        mesin = st.selectbox("Pilih Merk Mesin", [
            "Allwin Indoor", "Allwin Outdoor", "Epson SureColor", 
            "HP Latex", "Cutting JWEI", "Cutting Saga"
        ])
        st.success(f"Anda memilih: **{mesin}**")
        st.info("Silakan lanjut ke Chat Troubleshooting untuk masalah mesin ini.")

st.caption("PT. Aneka Warna Indah - Customer Service & Internal Tool © 2026")