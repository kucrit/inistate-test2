import streamlit as st
from groq import Groq

st.set_page_config(page_title="Aneka Warna AI", page_icon="🤖", layout="wide")

GROQ_API_KEY = "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"

# ==================== GLASSMORPHISM + HOVER ANIMATION ====================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e2937 100%);
    }
    .glass {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 24px;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glass:hover {
        background: rgba(255, 255, 255, 0.15);
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4);
        border-color: rgba(96, 165, 250, 0.5);
    }
    .main-header {
        font-size: 3.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #60a5fa, #a5b4fc, #c4d0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    .hero {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 80px 50px;
        border-radius: 28px;
        text-align: center;
        margin: 30px 0;
    }
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6, #60a5fa);
        color: white;
        border-radius: 9999px;
        height: 54px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(59, 130, 246, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
st.markdown("<h1 class='main-header'>ANEKA WARNA AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.5rem; color:#94a3b8; margin-bottom:40px;'>Asisten Teknisi Pintar untuk Mesin Digital Printing</p>", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero glass">
    <h2 style="color:white; font-size:2.8rem;">🤖 Halo! Saya Robot Teknisi AI</h2>
    <p style="color:#e0f2fe; font-size:1.4rem; margin:25px 0;">
        Siap membantu Anda 24/7 untuk troubleshooting, sparepart, dan solusi mesin
    </p>
</div>
""", unsafe_allow_html=True)

# Service Cards dengan Hover Animation
st.markdown("### Layanan Utama")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 💬 Chat Troubleshooting")
    st.write("Analisa error mesin secara cepat berdasarkan database tiketing")
    if st.button("Mulai Chat", key="chat_btn", use_container_width=True):
        st.session_state.page = "chat"
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 🔍 Cek Sparepart")
    st.write("Cek ketersediaan sparepart mesin secara real-time")
    if st.button("Cek Sparepart", key="spare_btn", use_container_width=True):
        st.session_state.page = "sparepart"
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 🏢 Cabang Kami")
    st.write("Temukan cabang terdekat dan kontak teknisi")
    if st.button("Lihat Cabang", key="cabang_btn", use_container_width=True):
        st.session_state.page = "cabang"
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== CHAT PAGE ====================
if st.session_state.get('page') == "chat":
    st.subheader("💬 Chat dengan Robot Teknisi AI")
    mesin = st.selectbox("Pilih Jenis Mesin", ["Allwin Indoor", "Allwin Outdoor", "Epson SureColor", "HP Latex", "Cutting JWEI", "Cutting Saga"])
    question = st.text_area("Jelaskan masalah yang dialami:", height=160)
    
    if st.button("🚀 Kirim ke Robot Teknisi", type="primary", use_container_width=True):
        if question:
            with st.spinner("🤖 Robot Teknisi sedang menganalisa..."):
                try:
                    client = Groq(api_key=GROQ_API_KEY)
                    resp = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": f"Mesin: {mesin}\nPertanyaan: {question}\nJawab sebagai teknisi profesional yang ramah dan jelas."}],
                        temperature=0.4
                    )
                    st.success("✅ Jawaban Robot Teknisi")
                    st.markdown(resp.choices[0].message.content)
                except:
                    st.error("Maaf, sedang ada gangguan.")

# Floating WhatsApp
st.markdown("""
<a href="https://wa.me/62821xxxxxxxx" target="_blank" style="position:fixed; bottom:30px; right:30px; background:#25D366; color:white; width:68px; height:68px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:32px; box-shadow:0 8px 25px rgba(0,0,0,0.4); z-index:999; text-decoration:none;">
    💬
</a>
""", unsafe_allow_html=True)

st.caption("PT. Aneka Warna Indah © 2026 | AI Customer Service")