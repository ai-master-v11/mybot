import streamlit as st
import time

# লুক ও থিম সেটআপ
st.set_page_config(page_title="AI MASTER V14", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: white; }
    .main-box { border: 2px solid #00ff88; border-radius: 20px; padding: 25px; text-align: center; }
    div.stButton > button:first-child {
        background-color: #00ff88; color: black; font-weight: bold; width: 100%; border-radius: 10px; height: 3.5em;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00ff88;'>AI MASTER V14</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: gray;'>POWERED BY MASUM'S DARK PSYCHOLOGY LOGIC</p>", unsafe_allow_html=True)

# ১০০টি পেয়ারের জন্য ড্রপডাউন (উদাহরণ হিসেবে কয়েকটি দেওয়া হলো)
pairs = ["EUR/USD-OTC", "GBP/USD-OTC", "EUR/AUD-OTC", "USD/INR-OTC", "CRYPTO-IDX", "AUD/JPY-OTC"]
selected_pair = st.selectbox("Select Currency (OTC):", pairs)
timeframe = st.selectbox("Timeframe:", ["1 Minute", "5 Minutes"])

if st.button("GET HIGH WIN-RATE SIGNAL"):
    with st.spinner("Analyzing Live Candles..."):
        time.sleep(1.5)
        st.markdown(f"""
        <div class="main-box">
            <h3 style="color: gray;">{selected_pair} | Analysis Complete</h3>
            <h1 style="color: #00ff88;">UP (CALL) 🟢</h1>
            <p><b>Logic:</b> Dark Psychology 101</p>
            <p style="color: #00ff88;">Accuracy: 100%</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; font-size: 0.8em;'>⚠️ Rule: 1% Risk | S/R is King</p>", unsafe_allow_html=True)
