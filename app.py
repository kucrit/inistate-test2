import streamlit as st
from groq import Groq

st.set_page_config(page_title="PT. Aneka Warna Indah | AI Service", page_icon="🤖", layout="wide")

GROQ_API_KEY = "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"

# ==================== CSS PROFESSIONAL ====================
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(90deg, #1e3a8a, #3b82f6, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 900;
        margin-bottom: 10px;
    }
    .hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e40af 100%);
        color: white;
        padding: 90px 40px;
        border-radius: 30px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 25px 50px rgba(30, 64, 175, 0.4);
    }
    .card {
        background: white;
        padding: 35px 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
        transition: all 0.3s;
        height: 100%;
    }
    .card:hover {
        transform: translateY(-15px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    .floating-wa {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: #25D366;
        color: white;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        z-index: 1000;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

# ==================== HERO SECTION ====================
st.image("https://media.licdn.com/dms/image/v2/C510BAQHcojTX5TbUtw/company-logo_200_200/company-logo_200_200/0/1631413078233/pt_aneka_warna_indah_logo?e=1782950400&v=beta&t=R3cTJRYznNlYl9qY6De1ROyosLZpwYzxumuG4faVXMA", width=180)

st.markdown("<h1 class='main-header'>PT. ANEKA WARNA INDAH</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#475569;'>AI Service Assistant untuk Mesin Digital Printing</h3>", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h2>🤖 Halo! Saya Robot Teknisi AI Anda</h2>
    <p style="font-size:1.5rem; margin:25px 0;">
        Siap membantu 24/7 untuk troubleshooting, sparepart, dan konsultasi mesin Anda
    </p>
</div>
""", unsafe_allow_html=True)

# ==================== MENU UTAMA ====================
st.markdown("### Pilih Layanan yang Anda Butuhkan")

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

# Chat Section
if st.session_state.get('page') == "chat":
    st.subheader("💬 Chat dengan Robot Teknisi AI")
    st.caption("Analisa berdasarkan pengalaman tiketing service tim teknisi")
    
    mesin = st.selectbox("Pilih Jenis Mesin", [
        "Allwin Indoor", "Allwin Outdoor", "Epson SureColor", 
        "HP Latex", "Cutting JWEI", "Cutting Saga"
    ])
    
    question = st.text_area("Jelaskan masalah mesin yang dialami:", height=150, placeholder="Contoh: Printhead tidak keluar tinta, error code E12...")
    
    if st.button("🚀 Kirim Pertanyaan ke AI", type="primary", use_container_width=True):
        if question:
            with st.spinner("🤖 Robot Teknisi sedang menganalisa..."):
                try:
                    client = Groq(api_key=GROQ_API_KEY)
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": f"""Anda adalah robot teknisi profesional PT. Aneka Warna Indah.
Mesin: {mesin}
Pertanyaan: {question}
Jawab dengan ramah, jelas, dan berikan langkah penyelesaian yang mudah diikuti."""}],
                        temperature=0.4,
                        max_tokens=800
                    )
                    st.success("✅ Jawaban Robot Teknisi AI")
                    st.markdown(response.choices[0].message.content)
                except:
                    st.error("Maaf, AI sedang sibuk. Coba lagi sebentar.")

# Placeholder untuk menu lain
elif st.session_state.get('page') in ["sparepart", "cabang", "sales"]:
    st.info("🔧 Fitur ini sedang dalam pengembangan. Segera hadir!")

# Internal
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
    else:
        st.error("Password salah")

# Floating WhatsApp
st.markdown("""
<a href="https://wa.me/62821xxxxxxxx" target="_blank" class="floating-wa">
    💬
</a>
""", unsafe_allow_html=True)

st.caption("PT. Aneka Warna Indah © 2026 | AI Customer Service Assistant")