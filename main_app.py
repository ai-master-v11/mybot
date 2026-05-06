import streamlit as st
import pandas as pd
from market_watcher import fetch_live_feed
from engine_core import process_market_flow
from secret_signals import get_elite_prediction
from visual_master import load_master_ui

# মাস্টার ইউআই লোড
load_master_ui()
st.title("Project 07: Invisible Elite")

# ডাটা এবং লজিক কানেকশন
try:
    # ডাটা আনার চেষ্টা
    live_data = fetch_live_feed()
    
    if live_data is not None and not live_data.empty:
        status = process_market_flow(live_data)
        prediction, confidence = get_elite_prediction(status)

        st.markdown(f"""
            <div style='background: #111827; padding: 20px; border-radius: 10px; border-left: 5px solid #00ff88;'>
                <h3 style='color: white;'>NEXT SIGNAL: {prediction}</h3>
                <p style='color: #00ff88;'>Confidence Score: {confidence}%</p>
                <p style='color: gray; font-size: 12px;'>Engine Status: 25 Files Active 07</p>
            </div>
        """, unsafe_allow_html=True)
        
        # চার্ট দেখানোর জন্য ফ্রেম
        st.components.v1.iframe("https://s.tradingview.com/widgetembed/?symbol=FX%3AEURUSD&interval=1&theme=dark", height=500)
    else:
        st.warning("Market Data is temporarily unavailable. Retrying...")
        
except Exception as e:
    st.error(f"Engine Error: {e}")
    st.write("Checking connection to 25 Layer Architecture...")

