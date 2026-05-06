import streamlit as st

# ১. পেজ কনফিগারেশন (মোবাইল ফ্রেন্ডলি)
st.set_page_config(
    page_title="Quotex | Digital Trading",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ২. ডার্ক মোড এবং ইন্টারফেস ফিক্স
st.markdown("""
    <style>
    /* মেইন কন্টেইনার এবং প্যাডিং রিমুভ */
    .main { background-color: #0b121c !important; }
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    header, footer { visibility: hidden !important; }
    
    /* কাস্টম মোবাইল ইউআই */
    .mobile-ui {
        background-color: #0b121c;
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        color: white;
        font-family: sans-serif;
        overflow: hidden;
    }

    /* টপ বার */
    .top-bar {
        height: 50px;
        background: #151d28;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 15px;
        border-bottom: 1px solid #232d3b;
    }

    /* চার্ট এরিয়া */
    .chart-container {
        flex-grow: 1;
        position: relative;
        background: #0b121c;
    }

    /* ফ্লোটিং ১০১ সাইকোলজি সিগন্যাল */
    .ai-signal {
        position: absolute;
        top: 15px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(0, 255, 136, 0.1);
        border: 1px solid #00ff88;
        padding: 8px 20px;
        border-radius: 8px;
        text-align: center;
        z-index: 99;
        backdrop-filter: blur(5px);
    }

    /* বটম ট্রেড প্যানেল (স্যামসাং/মোবাইল স্টাইল) */
    .bottom-panel {
        background: #151d28;
        padding: 15px;
        border-top: 1px solid #232d3b;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .trade-row {
        display: flex;
        gap: 10px;
    }

    .input-box {
        flex: 1;
        background: #232d3b;
        border: 1px solid #323e4f;
        padding: 12px;
        border-radius: 4px;
        font-size: 14px;
        text-align: center;
    }

    .up-btn { background: #00bb6d; flex: 1; padding: 15px; border-radius: 4px; text-align: center; font-weight: bold; }
    .down-btn { background: #ff3b3b; flex: 1; padding: 15px; border-radius: 4px; text-align: center; font-weight: bold; }
    </style>

    <div class="mobile-ui">
        <div class="top-bar">
            <div style="color:#00ff88; font-weight:bold; font-size:18px;">QUOTEX</div>
            <div style="background:#232d3b; padding:5px 12px; border-radius:4px; font-size:12px;">$10,000.00 DEMO</div>
            <div style="background:#00ff88; color:black; padding:5px 12px; border-radius:4px; font-weight:bold; font-size:12px;">Deposit</div>
        </div>

        <div class="chart-container">
            <div class="ai-signal">
                <div style="font-size:10px; color:#00ff88; text-transform:uppercase;">101 Dark Psychology</div>
                <div style="font-size:16px; font-weight:bold; color:white;">Next: CALL 🟢</div>
            </div>
            <iframe src="https://s.tradingview.com/widgetembed/?symbol=FX%3AEURUSD&interval=1&theme=dark" style="width:100%; height:100%; border:none;"></iframe>
        </div>

        <div class="bottom-panel">
            <div class="trade-row">
                <div class="input-box">Time: 01:00</div>
                <div class="input-box">Investment: $10</div>
            </div>
            <div class="trade-row">
                <div class="up-btn">UP (CALL)</div>
                <div class="down-btn">DOWN (PUT)</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
