import streamlit as st

# ১. পেজ সেটিংস (একদম ক্লিন এবং ফুল স্ক্রিন করার জন্য)
st.set_page_config(
    page_title="Quotex | Innovation in Trading", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ২. কটেক্স লুক দেওয়ার জন্য ডার্ক থিম সিএসএস (CSS)
st.markdown("""
    <style>
    /* মেনু এবং হেডার লুকিয়ে ফেলা */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0rem; max-width: 100%;}
    
    /* কটেক্সের ডার্ক ব্যাকগ্রাউন্ড */
    .stApp {
        background-color: #141923;
    }
    
    /* সিগন্যাল বক্সের ডিজাইন (চার্টের ওপর ভাসবে) */
    .signal-box {
        position: fixed;
        top: 80px;
        right: 30px;
        width: 180px;
        background: rgba(26, 33, 48, 0.95);
        border: 1px solid #293449;
        border-radius: 8px;
        padding: 15px;
        z-index: 9999;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. কটেক্সের রিয়েল-টাইম ইন্টারফেস ইনজেকশন (HTML/JS)
# এখানে আমি ট্রেডিংভিউ ব্যবহার করছি কারণ এটি কটেক্সের চার্টের সাথে ডিটো মিলে যায়
st.components.v1.html("""
    <div style="position: relative; width: 100%; height: 100vh; background-color: #141923;">
        
        <div style="height: 50px; background: #1a2130; border-bottom: 1px solid #293449; display: flex; align-items: center; padding: 0 20px;">
            <span style="color: #00ff88; font-weight: bold; font-size: 20px;">QUOTEX</span>
            <div style="margin-left: auto; color: white; background: #293449; padding: 5px 15px; border-radius: 4px;">
                $10,000.00 <span style="color: #888; font-size: 10px;">DEMO</span>
            </div>
        </div>

        <div id="tv_chart_container" style="height: calc(100% - 50px); width: 100%;"></div>
        
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({
          "autosize": true,
          "symbol": "FX:EURUSD",
          "interval": "1",
          "timezone": "Etc/UTC",
          "theme": "dark",
          "style": "1",
          "locale": "en",
          "toolbar_bg": "#1a2130",
          "enable_publishing": false,
          "hide_side_toolbar": false,
          "allow_symbol_change": true,
          "details": true,
          "container_id": "tv_chart_container"
        });
        </script>

        <div id="signal" style="position: absolute; top: 70px; right: 20px; width: 200px; background: #1a2130; border: 2px solid #00ff88; border-radius: 10px; padding: 15px; color: white; text-align: center; font-family: sans-serif;">
            <p style="margin: 0; color: #888; font-size: 12px;">PROJECT 07 AI</p>
            <h2 style="margin: 10px 0; color: #00ff88;">CALL 🟢</h2>
            <div style="background: #293449; padding: 5px; border-radius: 4px;">
                Next Candle: <span style="font-weight: bold;">UP</span>
            </div>
            <p style="margin-top: 10px; font-size: 10px; color: #555;">Confidence: 96%</p>
        </div>
    </div>
""", height=900)
