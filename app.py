import streamlit as st
import pandas as pd
from groq import Groq
import os

# ==================== CONFIGURASI ====================
st.set_page_config(
    page_title="PT. Aneka Warna Indah",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API Key Groq (sudah di-hardcode)
os.environ["GROQ_API_KEY"] = "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"

# Custom CSS - Desain Lebih Premium
st.markdown("""
<style>
    .main-header {
        font-size: 3.2rem;
        background: linear-gradient(90deg, #1e88e5, #00c853, #1e88e5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.6rem;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .hero-box {
        background: linear-gradient(135deg, #f0f7ff, #e8f5e9);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    .stButton>button {
        background: linear-gradient(90deg, #1e88e5, #00c853);
        color: white;
        font-size: 1.2em;
        height: 3.5em;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
st.sidebar.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=160)

st.sidebar.markdown("## 🏢 PT. ANEKA WARNA INDAH")
st.sidebar.markdown("**Digital Printing & Service Mesin**")
st.sidebar.markdown("---")

page = st.sidebar.selectbox(
    "📌 Pilih Menu Utama",
    ["🏠 Beranda", "🔧 Internal - Analisis Laporan", "👥 Customer Service"]
)

# ==================== HOMEPAGE (BERANDA) ====================
if page == "🏠 Beranda":
    col_logo, col_title = st.columns([1, 4])
    with col_logo:
        st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=150)
    
    st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Solusi Digital Printing & Service Mesin Profesional</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hero-box">
        <h2>👋 Halo! Selamat Datang</h2>
        <h3>Asisten Customer Service AI</h3>
        <p style="font-size: 1.3rem;">Chat disini, aku siap membantumu</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("💡 **Tips**: Pilih menu **Customer Service** di sebelah kiri untuk mulai chat")

# ==================== INTERNAL ====================
elif page == "🔧 Internal - Analisis Laporan":
    st.header("🔧 Internal - Analisis Laporan Inistate")
    
    uploaded_file = st.file_uploader("Upload Excel dari Inistate", type=["xlsx", "xls"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.success(f"✅ {len(df)} baris data berhasil dibaca")
        st.dataframe(df.head(10), use_container_width=True)
        
        if st.button("🚀 Analisis dengan AI & Update Knowledge Base"):
            with st.spinner("AI sedang menganalisis..."):
                st.session_state.knowledge_base = "Ringkasan dari tim internal:\n" + str(df.head(150).to_string())
                st.success("✅ Rangkuman berhasil dibuat dan siap digunakan oleh Customer Service!")

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
        st.success(f"✅ Anda memilih: **{mesin}**")
        
        st.markdown("### 💬 Chat dengan Asisten AI")
        if "knowledge_base" not in st.session_state:
            st.warning("Tim Internal belum mengupload rangkuman laporan terbaru.")
        else:
            question = st.text_input("Jelaskan masalah yang Anda alami:", 
                                   placeholder="Contoh: Printhead Allwin Indoor sering bermasalah...")
            
            if st.button("Kirim ke Asisten AI", type="primary"):
                if question:
                    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
                    prompt = f"""Kamu adalah asisten customer service PT. Aneka Warna Indah yang ramah, sopan, dan membantu.

Pengetahuan teknisi internal:
{st.session_state.get('knowledge_base', '')}

Pertanyaan customer: {question}

Jawab dengan bahasa yang mudah dipahami, berikan langkah penyelesaian yang jelas."""
                    
                    with st.spinner("Asisten AI sedang memproses jawaban..."):
                        response = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[{"role": "user", "content": prompt}],
                            temperature=0.4,
                        )
                        st.success("✅ Jawaban Asisten AI:")
                        st.markdown(response.choices[0].message.content)

    # Layanan lainnya...
    elif service == "💬 Chat Troubleshooting Mesin":
        st.info("Silakan pilih 'Pilih Jenis Mesin' terlebih dahulu.")

    elif service == "🔍 Cek Ketersediaan Sparepart":
        st.write("Fitur ini sedang dalam pengembangan.")

    elif service == "📍 Kontak Teknisi Daerah":
        st.subheader("Kontak Teknisi Daerah")
        st.write("**Magelang & Sekitarnya**")
        st.write("📞 Hubungi Tim Teknis")

    elif service == "🏢 Profile Perusahaan":
        st.subheader("Profile PT. Aneka Warna Indah")
        st.write("Kami melayani penjualan, service, dan sparepart mesin digital printing.")

st.caption("PT. Aneka Warna Indah © 2026 | AI Customer Service")