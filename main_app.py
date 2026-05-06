import streamlit as st
from market_watcher import fetch_live_feed
from engine_core import process_market_flow
from secret_signals import get_elite_prediction
from visual_master import load_master_ui

# মাস্টার ইউআই লোড
load_master_ui()
st.title("Project 07: Invisible Elite")

# ডাটা এবং লজিক কানেকশন
try:
    live_data = fetch_live_feed()
    status = process_market_flow(live_data)
    prediction, confidence = get_elite_prediction(status)

    st.markdown(f"<div class='signal-alert'><h3>NEXT CANDLE: {prediction}</h3><p>Confidence: {confidence}%</p></div>", unsafe_allow_html=True)
except:
    st.write("Connecting to Market...")
