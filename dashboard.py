import streamlit as st
import streamlit.components.v1 as components

# পেজ সেটআপ
st.set_page_config(page_title="Project 07 AI", layout="wide", initial_sidebar_state="collapsed")

# মেইন ইন্টারফেস (HTML & CSS)
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background-color: #0b121c; color: white; margin: 0; font-family: sans-serif; overflow: hidden; }
        .header { background: #151d28; height: 50px; display: flex; align-items: center; justify-content: space-between; padding: 0 15px; border-bottom: 1px solid #232d3b; }
        .chart-container { position: relative; height: calc(100vh - 160px); }
        .ai-box { position: absolute; top: 10px; left: 50%; transform: translateX(-50%); background: rgba(0,0,0,0.8); border: 2px solid #00ff88; padding: 8px 25px; border-radius: 5px; z-index: 10; text-align: center; }
        .bottom-panel { background: #151d28; padding: 15px; border-top: 1px solid #232d3b; position: fixed; bottom: 0; width: 100%; }
        .row { display: flex; gap: 10px; margin-bottom: 8px; }
        .box { flex: 1; background: #232d3b; border: 1px solid #323e4f; padding: 10px; border-radius: 4px; text-align: center; font-size: 13px; }
        .up { background: #00bb6d; padding: 15px; border-radius: 4px; flex: 1; text-align: center; font-weight: bold; }
        .down { background: #ff3b3b; padding: 15px; border-radius: 4px; flex: 1; text-align: center; font-weight: bold; }
    </style>
</head>
<body>
    <div class="header">
        <span style="color:#00ff88; font-weight:bold; font-size:18px;">QUOTEX AI</span>
        <div style="background:#00ff88; color:black; padding:4px 10px; border-radius:3px; font-weight:bold; font-size:12px;">DEPOSIT</div>
    </div>
    <div class="chart-container">
        <div class="ai-box">
            <div style="font-size:10px; color:#00ff88;">PROJECT 07 ELITE</div>
            <div style="font-size:16px; font-weight:bold;">SIGNAL: CALL (UP) 🟢</div>
        </div>
        <iframe src="https://s.tradingview.com/widgetembed/?symbol=FX%3AEURUSD&interval=1&theme=dark" style="width:100%; height:100%; border:none;"></iframe>
    </div>
    <div class="bottom-panel">
        <div class="row">
            <div class="box">Time: 01:00</div>
            <div class="box">Invest: $1,000.00</div>
        </div>
        <div class="row">
            <div class="up">UP</div>
            <div class="down">DOWN</div>
        </div>
    </div>
</body>
</html>
"""
components.html(html_code, height=2000, scrolling=False)
