import streamlit as st

def load_master_ui():
    # কটেক্স ডার্ক থিম ইনজেকশন
    st.markdown("""
        <style>
        .stApp { background-color: #06090f; }
        .signal-alert {
            padding: 20px;
            border-left: 5px solid #00ff88;
            background: #111827;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
