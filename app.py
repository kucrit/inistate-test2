import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah", page_icon="🔧", layout="wide")

# API Key Groq
GROQ_API_KEY = "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"

# Custom CSS - Warna Merah Elegan + Biru
st.markdown("""
<style>
    .main-header {font-size: 3rem; background: linear-gradient(90deg, #d32f2f, #1976d2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.5rem; color: #555; text-align: center;}
    .hero-box {background: linear-gradient(135deg, #fff0f0, #f0f7ff); padding: 35px; border-radius: 20px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);}
    .stButton>button {background: linear-gradient(90deg, #d32f2f, #1976d2); color: white; font-size: 1.15em; height: 3.8em; border-radius: 12px;}
    .logo {max-width: 180px; width: 100%; height: auto;}
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
st.sidebar.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=160, use_column_width=True)
st.sidebar.markdown("## 🏢 PT. ANEKA WARNA INDAH")

page = st.sidebar.selectbox("Pilih Menu", ["🏠 Beranda", "🔧 Internal Analisis", "👥 Customer Service"])

# ==================== BERANDA ====================
if page == "🏠 Beranda":
    st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", use_column_width=True)
    
    st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Solusi Digital Printing & Service Mesin Terpercaya</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hero-box">
        <h2>👋 Selamat Datang di Asisten AI Kami</h2>
        <h3>Chat disini, aku siap membantumu dengan cepat</h3>
    </div>
    """, unsafe_allow_html=True)

# ==================== INTERNAL (Password Protected) ====================
elif page == "🔧 Internal Analisis":
    st.header("🔒 Internal - Analisis Laporan Inistate")
    
    password = st.text_input("Masukkan Password Internal", type="password")
    
    if password == "admin123":   # Ganti password ini sesuai keinginanmu
        st.success("✅ Akses Diterima")
        uploaded_file = st.file_uploader("Upload Excel dari Inistate", type=["xlsx", "xls"])
        
        if uploaded_file:
            df = pd.read_excel(uploaded_file)
            st.success(f"✅ Berhasil membaca {len(df)} baris data")
            st.dataframe(df.head(10), use_container_width=True)
            
            if st.button("🚀 Analisis & Update Knowledge Base"):
                with st.spinner("AI sedang menganalisis..."):
                    st.session_state.knowledge_base = str(df.head(200).to_string())
                    st.success("✅ Knowledge base berhasil diupdate untuk Customer Service!")
    else:
        st.error("❌ Password salah. Hanya tim internal yang boleh masuk.")

# ==================== CUSTOMER SERVICE ====================
elif page == "👥 Customer Service":
    st.markdown("<h1 class='main-header' style='font-size:2.5rem;'>👥 Customer Service</h1>", unsafe_allow_html=True)
    
    service = st.selectbox("Pilih Layanan", [
        "🔍 Cek Ketersediaan Sparepart",
        "💬 Chat Troubleshooting Mesin"
    ])

    if service == "🔍 Cek Ketersediaan Sparepart":
        st.subheader("🔍 Cek Ketersediaan Sparepart")
        st.info("Fitur ini sedang dalam pengembangan. Kami akan segera menghubungkan ke website resmi.")
        st.button("Kunjungi Website Sparepart", disabled=True)

    elif service == "💬 Chat Troubleshooting Mesin":
        st.subheader("💬 Chat Troubleshooting Mesin")
        
        mesin = st.selectbox("Pilih Jenis Mesin", [
            "Allwin Indoor", "Allwin Outdoor", "Epson SureColor", 
            "HP Latex", "Cutting JWEI", "Cutting Saga"
        ])
        
        st.markdown("### 💬 Tanya Asisten AI")
        
        if "knowledge_base" not in st.session_state:
            st.warning("Tim Internal belum mengupdate rangkuman laporan terbaru.")
        else:
            question = st.text_input("Jelaskan masalah yang Anda alami:", 
                                   placeholder="Contoh: Printhead sering mampet pada Allwin Indoor...")
            
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

st.caption("PT. Aneka Warna Indah © 2026 | AI Customer Service")