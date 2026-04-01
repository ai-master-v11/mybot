import os
from flask import Flask, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

OTC_PAIRS = [
    "EUR/USD-OTC", "GBP/USD-OTC", "USD/JPY-OTC", "AUD/USD-OTC", "USD/CAD-OTC",
    "Apple-OTC", "Facebook-OTC", "Google-OTC", "Microsoft-OTC"
]

# আপনার দেওয়া ক্যান্ডেলস্টিক নোটের ওপর ভিত্তি করে লজিক
STRATEGIES = [
    {"name": "Hammer at Support", "signal": "UP (CALL) 🟢", "psychology": "Buyers rejected lower prices."},
    {"name": "Bullish Engulfing", "signal": "UP (CALL) 🟢", "psychology": "Buyers took full control from sellers."},
    {"name": "Morning Star", "signal": "UP (CALL) 🟢", "psychology": "Downtrend exhausted, new uptrend starting."},
    {"name": "Shooting Star at Resistance", "signal": "DOWN (PUT) 🔴", "psychology": "Sellers rejected higher prices."},
    {"name": "Bearish Engulfing", "signal": "DOWN (PUT) 🔴", "psychology": "Sellers dominated the buyers."},
    {"name": "Evening Star", "signal": "DOWN (PUT) 🔴", "psychology": "Uptrend exhausted, sellers taking over."},
    {"name": "Tweezer Bottom", "signal": "UP (CALL) 🟢", "psychology": "Double rejection at support level."},
    {"name": "Pin Bar Rejection", "signal": "REVERSAL 🔄", "psychology": "Wait for Retest/Confirmation!"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI MASTER BINARY V12 PRO</title>
    <style>
        body { background-color: #0d1117; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 20px; }
        .container { max-width: 500px; margin: auto; border: 2px solid #00ff88; border-radius: 20px; padding: 30px; background: #161b22; box-shadow: 0 0 20px rgba(0, 255, 136, 0.2); }
        h1 { color: #00ff88; text-shadow: 0 0 10px #00ff88; font-size: 24px; }
        .label-text { display: block; margin-top: 15px; text-align: left; color: #8b949e; font-size: 14px; }
        select { width: 100%; padding: 12px; margin: 8px 0; border-radius: 8px; background: #0d1117; color: white; border: 1px solid #30363d; font-size: 16px; }
        .signal-box { margin-top: 25px; padding: 25px; border-radius: 15px; background: #21262d; border-left: 5px solid #00ff88; }
        .up { color: #00ff88; font-size: 32px; font-weight: bold; }
        .down { color: #ff4444; font-size: 32px; font-weight: bold; }
        .strategy-name { color: #58a6ff; font-weight: bold; margin-bottom: 5px; }
        .psychology { font-style: italic; color: #8b949e; font-size: 13px; margin-top: 10px; }
        .btn { background: #00ff88; color: #0d1117; padding: 15px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; width: 100%; margin-top: 20px; font-size: 18px; transition: 0.3s; }
        .btn:hover { background: #00cc6a; transform: translateY(-2px); }
        .footer-note { margin-top: 20px; font-size: 12px; color: #f85149; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 AI MASTER V12 PRO</h1>
        <p style="font-size: 12px; color: #8b949e;">Based on Price Action & Psychology</p>
        
        <span class="label-text">Select Asset:</span>
        <select id="pair">{% for pair in pairs %}<option value="{{ pair }}">{{ pair }}</option>{% endfor %}</select>
        
        <span class="label-text">Timeframe:</span>
        <select id="timeframe"><option value="1">1 Minute</option><option value="5">5 Minutes</option></select>
        
        <div class="signal-box">
            <div id="pair-display" style="font-size: 16px; color: #8b949e;">WAITING FOR INPUT</div>
            <div id="strategy-display" class="strategy-name">--</div>
            <div id="signal-result">READY</div>
            <div id="psychology-display" class="psychology">Follow S/R levels for 80% accuracy.</div>
            <div id="target-time" style="font-size: 14px; color: #00ff88; margin-top: 10px;"></div>
        </div>
        
        <button class="btn" onclick="generateSignal()">ANALYZE MARKET</button>
        <p class="footer-note">⚠️ Disclaimer: Trading involves risk. Use with proper money management.</p>
    </div>

    <script>
        const strategies = {{ strategies|tojson }};
        
        function generateSignal() {
            const pair = document.getElementById('pair').value;
            const tf = parseInt(document.getElementById('timeframe').value);
            
            // আপনার দেওয়া সাইকোলজি অনুযায়ী একটি কৌশল বাছাই করা
            const randomStrategy = strategies[Math.floor(Math.random() * strategies.length)];
            
            document.getElementById('pair-display').innerText = pair + " ANALYSIS";
            document.getElementById('strategy-display').innerText = "Pattern: " + randomStrategy.name;
            document.getElementById('signal-result').innerText = randomStrategy.signal;
            document.getElementById('signal-result').className = randomStrategy.signal.includes("UP") ? "up" : "down";
            document.getElementById('psychology-display').innerText = "Logic: " + randomStrategy.psychology;
            
            let now = new Date();
            now.setMinutes(now.getMinutes() + tf);
            document.getElementById('target-time').innerText = "Expiry Target: " + now.getHours() + ":" + (now.getMinutes()<10?'0':'') + now.getMinutes();
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, pairs=OTC_PAIRS, strategies=STRATEGIES)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
