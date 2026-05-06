import streamlit as st
import time

# ১. ফুল স্ক্রিন ও ডার্ক মোড সেটিংস
st.set_page_config(page_title="Quotex | Digital Trading", layout="wide", initial_sidebar_state="collapsed")

# ২. কটেক্সের ডিটো কপি ইন্টারফেসের জন্য সিএসএস
st.markdown("""
    <style>
    .block-container {padding: 0px !important;}
    header, footer {visibility: hidden;}
    body {background-color: #0b121c; color: #fff; font-family: 'Open Sans', sans-serif;}

    .container {
        display: grid;
        grid-template-columns: 60px 1fr 280px;
        grid-template-rows: 60px 1fr;
        height: 100vh;
    }

    .header {
        grid-column: 1 / 4;
        background: #151d28;
        border-bottom: 1px solid #232d3b;
        display: flex;
        align-items: center;
        padding: 0 20px;
        justify-content: space-between;
    }

    .sidebar {
        background: #151d28;
        border-right: 1px solid #232d3b;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 20px;
        gap: 30px;
    }

    .trade-panel {
        background: #151d28;
        border-left: 1px solid #232d3b;
        padding: 20px;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .up-btn { background: #00bb6d; padding: 15px; border-radius: 4px; text-align: center; font-weight: bold; cursor: pointer; }
    .down-btn { background: #ff3b3b; padding: 15px; border-radius: 4px; text-align: center; font-weight: bold; cursor: pointer; }
    .input-box { background: #232d3b; border: 1px solid #323e4f; padding: 10px; border-radius: 4px; font-size: 14px; }
    
    /* সাইকোলজি সিগন্যাল বক্স */
    .psychology-alert {
        position: absolute;
        top: 20px;
        right: 20px;
        background: rgba(13, 18, 28, 0.9);
        border: 1px solid #00ff88;
        padding: 10px;
        border-radius: 5px;
        font-size: 11px;
        color: #00ff88;
        z-index: 100;
        width: 180px;
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. ইন্টারফেস লেআউট
st.markdown("""
    <div class="container">
        <div class="header">
            <div style="display:flex; align-items:center; gap:20px;">
                <span style="color:#00ff88; font-weight:bold; font-size:22px;">QUOTEX</span>
                <div style="background:#232d3b; padding:5px 15px; border-radius:4px; font-size:13px;">EUR/USD (OTC) 98%</div>
            </div>
            <div style="display:flex; align-items:center; gap:15px;">
                <div style="text-align:right;">
                    <div style="font-size:14px; font-weight:bold;">$10,000.00</div>
                    <div style="font-size:10px; color:#888;">Demo Account</div>
                </div>
                <button style="background:#00ff88; border:none; padding:8px 20px; border-radius:4px; font-weight:bold;">Deposit</button>
            </div>
        </div>

        <div class="sidebar">
            <div style="color:#888; font-size:20px;">📊</div>
            <div style="color:#888; font-size:20px;">🕒</div>
            <div style="color:#888; font-size:20px;">🏆</div>
            <div style="color:#888; font-size:20px;">⚙️</div>
        </div>

        <div style="position:relative; background:#0b121c;">
            <div class="psychology-alert">
                <b>101 DARK PSYCHOLOGY MODE: ON</b><br>
                Status: Leading 1-Min Candle<br>
                Logic: Trap Detection Active
            </div>

            <iframe src="https://s.tradingview.com/widgetembed/?symbol=FX%3AEURUSD&interval=1&theme=dark&style=1" style="width:100%; height:100%; border:none;"></iframe>
            
            <div style="position:absolute; bottom:50px; left:50%; transform:translateX(-50%); background:rgba(0,0,0,0.8); border:2px solid #00ff88; padding:15px 50px; border-radius:50px; z-index:10; color:#00ff88; font-weight:bold; font-size:20px;">
                NEXT: CALL (GREEN) 🟢
            </div>
        </div>

        <div class="trade-panel">
            <div>
                <div style="color:#888; font-size:12px; margin-bottom:5px;">Time</div>
                <div class="input-box">00:01:00</div>
            </div>
            <div>
                <div style="color:#888; font-size:12px; margin-bottom:5px;">Investment</div>
                <div class="input-box">$ 1,000.00</div>
            </div>
            <div class="up-btn">UP</div>
            <div class="down-btn">DOWN</div>
            <div style="margin-top:auto; text-align:center; border-top:1px solid #232d3b; padding-top:20px;">
                <div style="color:#00ff88; font-size:20px; font-weight:bold;">98%</div>
                <div style="color:#888; font-size:12px;">Profit $1,980.00</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
