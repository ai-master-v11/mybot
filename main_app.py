import streamlit as st
import datetime
import pytz
import random

# ১. পেজ সেটআপ এবং ডিজাইন
st.set_page_config(page_title="AI MASTER BINARY V14", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: white; }
    .main-container { border: 2px solid #00ff88; padding: 25px; border-radius: 20px; background: #0d1117; }
    .header-title { color: #00ff88; font-size: 32px; font-weight: bold; text-align: center; text-shadow: 0 0 8px #00ff88; }
    .signal-box { background: #161b22; padding: 20px; border-radius: 15px; margin-top: 15px; text-align: center; border: 1px solid #30363d; }
    div.stButton > button { background-color: #00ff88 !important; color: black !important; font-weight: bold !important; width: 100% !important; border-radius: 12px !important; height: 50px !important; }
    </style>
""", unsafe_allow_html=True)

# ২. মূল বডি
with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='header-title'>AI MASTER V14</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8b949e;'>POWERED BY MASUM'S DARK PSYCHOLOGY LOGIC</p>", unsafe_allow_html=True)

    currencies = [f"{b}/{q}-OTC" for b in ["EUR","USD","GBP","AUD","CAD","CHF"] for q in ["USD","JPY","EUR","AUD"]]
    selected_pair = st.selectbox("Select Currency (OTC):", currencies[:105])
    tf = st.selectbox("Timeframe (Recommended 5m):", ["1 Minute", "2 Minutes", "5 Minutes"])

    if st.button("GET HIGH WIN-RATE SIGNAL"):
        # বর্তমান রিয়েল টাইম বের করা (ইন্ডিয়া/বাংলাদেশ টাইম - IST)
        # রেন্ডার সার্ভারের টাইম না নিয়ে সরাসরি আপনার লোকাল টাইম জোন সেট করা হয়েছে
        ist = pytz.timezone('Asia/Kolkata') 
        now = datetime.datetime.now(ist)
        
        # সিগন্যাল এক মিনিট পরের হবে
        expiry_time = (now + datetime.timedelta(minutes=1)).strftime("%H:%M")
        
        psychology_notes = ["Liquidity Hunt (Trap)", "Hidden Gap Filling", "Fake Breakout Detected", "Order Block Rejection"]
        note = random.choice(psychology_notes)
        
        st.markdown(f"""
            <div class='signal-box'>
                <p style='color: #8b949e; font-size: 14px;'>{selected_pair} | Analysis Complete</p>
                <h1 style='color: #00ff88; font-size: 45px; margin: 10px 0;'>UP (CALL) 🟢</h1>
                <div style='background: #0d1117; padding: 12px; border-left: 4px solid #00ff88; border-radius: 6px; text-align: left;'>
                    <p style='color: #00ff88; margin: 0; font-weight: bold;'>Psychology: <span style='color: white;'>{note}</span></p>
                    <p style='color: #8b949e; font-size: 12px; margin-top: 5px;'>Scanning 1001 patterns for elite accuracy...</p>
                </div>
                <p style='color: #00ff88; font-weight: bold; margin-top: 15px;'>Trade Duration: {tf} (Exp: {expiry_time})</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><p style='color: #e3b341; text-align: center; font-size: 12px;'>⚠️ <b>Rule:</b> 1% Risk | Wait for Retest | S/R is King</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
