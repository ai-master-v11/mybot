import streamlit as st

# ১. পেজ সেটআপ
st.set_page_config(page_title="Quotex | Digital Trading", layout="wide", initial_sidebar_state="collapsed")

# ২. ডুপ্লিকেট ইন্টারফেস তৈরি (HTML/CSS)
st.markdown("""
    <style>
    /* মেইন বডি এবং ব্যাকগ্রাউন্ড */
    .block-container {padding: 0px !important;}
    header, footer {visibility: hidden;}
    body {background-color: #0b121c; color: white; overflow: hidden;}

    .main-wrapper {
        display: grid;
        grid-template-columns: 60px 1fr 280px;
        grid-template-rows: 60px 1fr;
        height: 100vh;
        width: 100vw;
    }

    /* টপ বার (Top Bar) */
    .header {
        grid-column: 1 / 4;
        background: #151d28;
        border-bottom: 1px solid #232d3b;
        display: flex;
        align-items: center;
        padding: 0 20px;
        justify-content: space-between;
    }

    /* বাম পাশের মেনু (Left Sidebar) */
    .sidebar {
        background: #151d28;
        border-right: 1px solid #232d3b;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 20px;
        gap: 25px;
    }

    /* চার্ট এরিয়া (Main Chart) */
    .chart-area {
        position: relative;
        background: #0b121c;
    }

    /* ডান পাশের ট্রেড প্যানেল (Trade Panel) */
    .trade-panel {
        background: #151d28;
        border-left: 1px solid #232d3b;
        padding: 15px;
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    /* বাটন ও ইনপুট ডিজাইন */
    .box { background: #232d3b; border: 1px solid #323e4f; padding: 10px; border-radius: 4px; font-size: 13px; }
    .btn-up { background: #00bb6d; padding: 12px; border-radius: 4px; text-align: center; font-weight: bold; cursor: pointer; }
    .btn-down { background: #ff3b3b; padding: 12px; border-radius: 4px; text-align: center; font-weight: bold; cursor: pointer; }

    /* ১০১ সাইকোলজি সিগন্যাল ফ্লোটিং বক্স */
    .signal-box {
        position: absolute;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(0, 0, 0, 0.85);
        border: 2px solid #00ff88;
        padding: 10px 30px;
        border-radius: 50px;
        z-index: 1000;
        text-align: center;
        box-shadow: 0 0 15px rgba(0,255,136,0.4);
    }
    </style>

    <div class="main-wrapper">
        <div class="header">
            <div style="display:flex; align-items:center; gap:15px;">
                <span style="color:#00ff88; font-weight:bold; font-size:20px;">QUOTEX</span>
                <div style="background:#232d3b; padding:4px 10px; border-radius:4px; font-size:12px;">EUR/USD (OTC) 98%</div>
            </div>
            <div style="display:flex; align-items:center; gap:15px;">
                <div style="text-align:right;">
                    <div style="font-size:14px; font-weight:bold;">$10,000.00</div>
                    <div style="font-size:10px; color:#888;">Demo Account</div>
                </div>
                <div style="background:#00ff88; color:black; padding:6px 15px; border-radius:4px; font-weight:bold; font-size:13px;">Deposit</div>
            </div>
        </div>

        <div class="sidebar">
            <div style="color:#888; font-size:18px;">📊</div>
            <div style="color:#888; font-size:18px;">🕒</div>
            <div style="color:#888; font-size:18px;">🏆</div>
            <div style="color:#888; font-size:18px;">⚙️</div>
        </div>

        <div class="chart-area">
            <div class="signal-box">
                <div style="color:#00ff88; font-size:10px; letter-spacing:1px;">101 DARK PSYCHOLOGY</div>
                <div style="font-size:18px; font-weight:bold;">NEXT CANDLE: UP 🟢</div>
            </div>
            <iframe src="https://s.tradingview.com/widgetembed/?symbol=FX%3AEURUSD&interval=1&theme=dark&style=1" style="width:100%; height:100%; border:none;"></iframe>
        </div>

        <div class="trade-panel">
            <div>
                <div style="color:#888; font-size:11px; margin-bottom:4px;">Time</div>
                <div class="box">00:01:00</div>
            </div>
            <div>
                <div style="color:#888; font-size:11px; margin-bottom:4px;">Investment</div>
                <div class="box">$ 1,000.00</div>
            </div>
            <div class="btn-up">UP</div>
            <div class="btn-down">DOWN</div>
            <div style="margin-top:auto; text-align:center; border-top:1px solid #232d3b; padding-top:10px;">
                <div style="color:#00ff88; font-size:18px; font-weight:bold;">98%</div>
                <div style="color:#888; font-size:11px;">Profit: $1,980.00</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
