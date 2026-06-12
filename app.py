import streamlit as st
import pandas as pd
from groq import Groq
import os

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 2.8rem; background: linear-gradient(90deg, #1e88e5, #00c853); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center;}
    .customer-header {font-size: 2.4rem; color: #1e88e5; text-align: center;}
    .stButton>button {background: linear-gradient(90deg, #1e88e5, #00c853); color: white; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

# Navigation
page = st.sidebar.selectbox("Pilih Menu", 
    ["🏠 Beranda", "🔧 Internal - Analisis Laporan", "👥 Customer Service"])

# ==================== BERANDA ====================
if page == "🏠 Beranda":
    st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=180)
    
    st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
    st.markdown("### Solusi Digital Printing & Service Mesin Terpercaya")
    
    st.info("**Asisten Customer** - Chat disini aku bisa membantumu 💬")
    
    st.markdown("---")
    st.write("Silakan pilih **Customer Service** di sidebar untuk mendapatkan bantuan.")

# ==================== INTERNAL ====================
elif page == "🔧 Internal - Analisis Laporan":
    st.header("🔧 Internal - Analisis Laporan Inistate")
    
    api_key = st.text_input("Groq API Key", type="password", value=os.getenv("GROQ_API_KEY", ""))
    if st.button("Simpan API Key"):
        os.environ["GROQ_API_KEY"] = api_key
        st.success("✅ API Key tersimpan")

    uploaded_file = st.file_uploader("Upload Excel dari Inistate", type=["xlsx", "xls"])
    
    if uploaded_file and os.environ.get("GROQ_API_KEY"):
        df = pd.read_excel(uploaded_file)
        st.success(f"✅ {len(df)} baris data berhasil dibaca")
        st.dataframe(df.head(10), use_container_width=True)
        
        if st.button("🚀 Analisis dengan AI"):
            with st.spinner("AI sedang menganalisis semua laporan..."):
                # Simpan knowledge base untuk customer
                st.session_state.knowledge_base = "Ringkasan dari tim internal: " + str(df.head(100).to_string())
                st.success("✅ Knowledge base berhasil dibuat dan siap digunakan di Customer Service!")

# ==================== CUSTOMER SERVICE ====================
elif page == "👥 Customer Service":
    st.markdown("<h1 class='customer-header'>🤖 Asisten Customer Service</h1>", unsafe_allow_html=True)
    
    service = st.selectbox("Pilih Layanan", [
        "💬 Chat Troubleshooting Mesin",
        "🛠️ Pilih Jenis Mesin",
        "🔍 Cek Ketersediaan Sparepart",
        "📍 Kontak Teknisi Daerah",
        "🏢 Profile Perusahaan"
    ])

    if service == "🛠️ Pilih Jenis Mesin":
        mesin = st.selectbox("Pilih Merk Mesin", [
            "Allwin Indoor", "Allwin Outdoor", "Epson SureColor", 
            "HP Latex", "Cutting JWEI", "Cutting Saga"
        ])
        st.success(f"Anda memilih: **{mesin}**")
        st.info("Silakan lanjut ke Chat Troubleshooting di bawah ini.")

        # ==================== CHAT AI UNTUK CUSTOMER ====================
        st.markdown("### 💬 Chat dengan Asisten AI")
        if "knowledge_base" not in st.session_state:
            st.warning("Tim Internal belum membuat rangkuman laporan. Silakan hubungi tim internal.")
        else:
            question = st.text_input("Jelaskan masalah mesin Anda:", 
                                   placeholder="Contoh: Printhead Allwin Indoor clogink...")
            
            if st.button("Kirim ke Asisten AI"):
                if question:
                    client = Groq(api_key=os.environ.get("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"))
                    prompt = f"""Kamu adalah asisten customer service PT. Aneka Warna Indah yang ramah dan profesional.

Pengetahuan dari tim teknisi internal:
{st.session_state.get('knowledge_base', '')}

Pertanyaan customer: {question}

Jawab dengan bahasa yang mudah dipahami, langkah demi langkah, dan sopan."""
                    
                    with st.spinner("Asisten AI sedang memproses..."):
                        response = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[{"role": "user", "content": prompt}],
                            temperature=0.4,
                        )
                        st.success("✅ Jawaban Asisten AI:")
                        st.markdown(response.choices[0].message.content)

    # Layanan lain (bisa dikembangkan)
    elif service == "💬 Chat Troubleshooting Mesin":
        st.info("Silakan pilih 'Pilih Jenis Mesin' terlebih dahulu untuk mengaktifkan chat AI.")

    elif service == "🔍 Cek Ketersediaan Sparepart":
        st.write("Fitur ini sedang dalam pengembangan.")

    elif service == "📍 Kontak Teknisi Daerah":
        st.write("**Teknisi Jawa Tengah & Sekitarnya**")
        st.write("📞 Hubungi: 08xx-xxxx-xxxx")
        st.write("📍 Yogyakarta, Jawa Tengah")

    elif service == "🏢 Profile Perusahaan":
        st.write("PT. Aneka Warna Indah adalah perusahaan spesialis mesin digital printing.")

st.caption("PT. Aneka Warna Indah - Customer Service & Internal Tool © 2026")