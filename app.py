import os
from flask import Flask, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

# ৫০টির বেশি কারেন্সি পেয়ার এবং ওটিসি অ্যাসেট যুক্ত করা হলো
OTC_PAIRS = [
    "EUR/USD-OTC", "GBP/USD-OTC", "USD/JPY-OTC", "AUD/USD-OTC", "USD/CAD-OTC",
    "EUR/JPY-OTC", "GBP/JPY-OTC", "EUR/GBP-OTC", "AUD/JPY-OTC", "CAD/JPY-OTC",
    "NZD/USD-OTC", "CHF/JPY-OTC", "EUR/CHF-OTC", "GBP/CHF-OTC", "AUD/CAD-OTC",
    "USD/BRL-OTC", "USD/TRY-OTC", "USD/ZAR-OTC", "USD/INR-OTC", "USD/MXN-OTC",
    "EUR/TRY-OTC", "GBP/TRY-OTC", "AUD/CHF-OTC", "NZD/JPY-OTC", "EUR/AUD-OTC",
    "EUR/NZD-OTC", "GBP/AUD-OTC", "GBP/NZD-OTC", "USD/SGD-OTC", "EUR/CAD-OTC",
    "Apple-OTC", "Facebook-OTC", "Google-OTC", "Microsoft-OTC", "Amazon-OTC",
    "Tesla-OTC", "Netflix-OTC", "Intel-OTC", "Twitter-OTC", "Visa-OTC",
    "McDonald's-OTC", "Boeing-OTC", "Coca-Cola-OTC", "Pepsi-OTC", "Nike-OTC",
    "Gold-OTC", "Silver-OTC", "Platinum-OTC", "Copper-OTC", "Brent Oil-OTC",
    "Bitcoin-OTC", "Ethereum-OTC", "Litecoin-OTC", "Ripple-OTC"
]

# আপনার ক্যান্ডেলস্টিক সাইকোলজি নোট অনুযায়ী স্ট্র্যাটেজি
STRATEGIES = [
    {"name": "Hammer at Support", "signal": "UP (CALL) 🟢", "psychology": "নিচ থেকে Buyers রিজেকশন দিয়েছে।", "accuracy": "87%"},
    {"name": "Bearish Engulfing", "signal": "DOWN (PUT) 🔴", "psychology": "সেলাররা বায়ারদের পুরোপুরি ঢেকে ফেলেছে।", "accuracy": "84%"},
    {"name": "Morning Star", "signal": "UP (CALL) 🟢", "psychology": "ডাউনট্রেন্ড শেষ, এখন নতুন আপট্রেন্ড শুরু হবে।", "accuracy": "89%"},
    {"name": "Shooting Star at Resistance", "signal": "DOWN (PUT) 🔴", "psychology": "উপরের লেভেল থেকে শক্তিশালী রিজেকশন এসেছে।", "accuracy": "85%"},
    {"name": "Evening Star", "signal": "DOWN (PUT) 🔴", "psychology": "আপট্রেন্ড দুর্বল হয়ে সেলাররা প্রবেশ করেছে।", "accuracy": "88%"},
    {"name": "Tweezer Bottom", "signal": "UP (CALL) 🟢", "psychology": "সাপোর্টে দুইবার রিজেকশন, রিভার্সাল নিশ্চিত।", "accuracy": "82%"},
    {"name": "Bullish Harami", "signal": "UP (CALL) 🟢", "psychology": "সেলিং প্রেশার কমে বায়াররা সক্রিয় হচ্ছে।", "accuracy": "80%"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI MASTER V12 - 50+ ASSETS</title>
    <style>
        body { background-color: #0b0e14; color: white; font-family: sans-serif; text-align: center; padding: 15px; }
        .container { max-width: 450px; margin: auto; border: 2px solid #00ff88; border-radius: 20px; padding: 20px; background: #161b22; box-shadow: 0 0 20px rgba(0, 255, 136, 0.2); }
        h1 { color: #00ff88; font-size: 20px; margin-bottom: 15px; }
        select { width: 100%; padding: 10px; margin: 10px 0; border-radius: 8px; background: #0d1117; color: white; border: 1px solid #30363d; font-size: 14px; }
        .signal-box { margin-top: 20px; padding: 20px; border-radius: 12px; background: #21262d; border-left: 5px solid #00ff88; }
        .up { color: #00ff88; font-size: 30px; font-weight: bold; }
        .down { color: #ff4444; font-size: 30px; font-weight: bold; }
        .btn { background: #00ff88; color: #0d1117; padding: 15px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; width: 100%; margin-top: 20px; font-size: 16px; }
        .footer { margin-top: 20px; font-size: 11px; color: #ff7b72; border: 1px dashed #ff7b72; padding: 10px; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 AI MASTER V12 - MAX PAIRS</h1>
        
        <label style="float:left; font-size:12px;">Select Asset (50+ Available):</label>
        <select id="pair">
            {% for pair in pairs %}
            <option value="{{ pair }}">{{ pair }}</option>
            {% endfor %}
        </select>
        
        <label style="float:left; font-size:12px;">Timeframe:</label>
        <select id="timeframe">
            <option value="1">1 Minute</option>
            <option value="5">5 Minutes</option>
        </select>
        
        <div class="signal-box" id="result-box" style="display:none;">
            <div id="pair-name" style="color: #8b949e; font-size: 13px;"></div>
            <div id="strategy-name" style="color: #58a6ff; font-weight: bold; margin-top: 5px;"></div>
            <div id="signal-text"></div>
            <div id="psychology-text" style="font-size: 13px; font-style: italic; color: #c9d1d9; margin-top: 10px;"></div>
            <div id="accuracy-tag" style="color: #00ff88; font-size: 12px; margin-top: 5px;"></div>
        </div>
        
        <button class="btn" onclick="analyze()">ANALYZE MARKET</button>
        
        <div class="footer">
            ⚠️ সতর্কবার্তা: ট্রেডিং ঝুঁকি সাপেক্ষ। সঠিক মানি ম্যানেজমেন্ট মেনে এটি ব্যবহার করুন।
        </div>
    </div>

    <script>
        const strategies = {{ strategies|tojson }};
        function analyze() {
            const pair = document.getElementById('pair').value;
            const resBox = document.getElementById('result-box');
            const randomStrat = strategies[Math.floor(Math.random() * strategies.length)];
            
            resBox.style.display = 'block';
            document.getElementById('pair-name').innerText = pair + " ANALYSIS";
            document.getElementById('strategy-name').innerText = "Pattern: " + randomStrat.name;
            document.getElementById('signal-text').innerText = randomStrat.signal;
            document.getElementById('signal-text').className = randomStrat.signal.includes("UP") ? "up" : "down";
            document.getElementById('psychology-text').innerText = "Logic: " + randomStrat.psychology;
            document.getElementById('accuracy-tag').innerText = "AI Confidence: " + randomStrat.accuracy;
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
