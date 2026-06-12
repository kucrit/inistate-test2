import streamlit as st
import pandas as pd
from groq import Groq
import os

st.set_page_config(page_title="AI Troubleshooting Inistate", layout="wide")
st.title("🤖 AI Troubleshooting Mesin - Inistate")
st.markdown("**Aplikasi bantu teknisi analisis error dari laporan Inistate**")

# Sidebar
with st.sidebar:
    st.header("Pengaturan AI")
    api_key = st.text_input("Masukkan Groq API Key", type="password", 
                           value=os.getenv("GROQ_API_KEY", ""))
    
    if st.button("Simpan API Key"):
        os.environ["GROQ_API_KEY"] = api_key
        st.success("API Key tersimpan! ✅")
    
    st.divider()
    st.info("Dapatkan API Key gratis di: https://console.groq.com/keys")

# Fungsi utama - VERSI RINGAN
def summarize_errors(df):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    # Batasi hanya 150 baris pertama + bersihkan data
    df_sample = df.head(150).fillna("").astype(str)
    text_data = df_sample.apply(lambda row: ' | '.join(row), axis=1).tolist()
    combined = "\n".join(text_data)
    
    prompt = f"""
    Kamu adalah expert teknisi mesin. Analisis ringkasan laporan error dari sistem Inistate berikut:

    {combined}

    Buatkan ringkasan profesional dalam Bahasa Indonesia dengan format ini:

    **1. Error yang Paling Sering Muncul:**
    (list error teratas beserta jumlah kasus jika ada, penyebab utama, dan solusi terbaik)

    **2. Kategori Masalah:**
    - Mekanik: ...
    - Elektrik: ...
    - Software / Sensor: ...
    - Operator / Penggunaan: ...

    **3. Rekomendasi Pencegahan Umum:**
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=1000
    )
    return response.choices[0].message.content

# Main App
tab1, tab2 = st.tabs(["📊 Upload & Rangkum", "💬 Chat dengan AI"])

with tab1:
    uploaded_file = st.file_uploader("Upload file Excel dari Inistate", type=["xlsx", "xls"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.success(f"✅ Berhasil membaca {len(df)} baris laporan!")
        st.dataframe(df.head(10), use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            num_rows = st.slider("Jumlah baris yang dianalisis", 50, 300, 150)
        
        if st.button("🚀 Rangkum Semua Error dengan AI", type="primary"):
            if not os.environ.get("GROQ_API_KEY"):
                st.error("Masukkan Groq API Key di sidebar dulu!")
            else:
                with st.spinner("AI sedang menganalisis..."):
                    df_limited = df.head(num_rows)
                    summary = summarize_errors(df_limited)
                    st.subheader("📋 Ringkasan AI")
                    st.markdown(summary)
                    
                    if "knowledge_base" not in st.session_state:
                        st.session_state.knowledge_base = summary

with tab2:
    st.subheader("💬 Tanya AI Troubleshooting")
    
    if "knowledge_base" not in st.session_state:
        st.warning("Silakan upload Excel dan rangkum dulu di tab pertama.")
    else:
        question = st.text_input("Ketik error atau masalah yang dialami teknisi:")
        
        if st.button("Kirim Pertanyaan"):
            if question:
                client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
                prompt = f"""
                Kamu adalah asisten teknisi mesin yang sangat membantu.
                Jawab berdasarkan pengetahuan dari laporan Inistate kantor kita.

                Pengetahuan:
                {st.session_state.knowledge_base}

                Pertanyaan: {question}

                Jawab langkah demi langkah, jelas, dan mudah dipahami.
                """
                with st.spinner("AI sedang berpikir..."):
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.4,
                    )
                    st.success("✅ Jawaban AI:")
                    st.markdown(response.choices[0].message.content)

st.caption("AI Troubleshooting Inistate | Dibuat untuk tim teknisi")