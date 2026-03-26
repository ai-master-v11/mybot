import os
from flask import Flask, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

OTC_PAIRS = [
    "EUR/USD-OTC", "GBP/USD-OTC", "USD/JPY-OTC", "AUD/USD-OTC", "USD/CAD-OTC",
    "EUR/JPY-OTC", "GBP/JPY-OTC", "EUR/GBP-OTC", "NZD/USD-OTC", "USD/CHF-OTC",
    "AUD/JPY-OTC", "CAD/JPY-OTC", "EUR/AUD-OTC", "GBP/AUD-OTC", "EUR/CAD-OTC",
    "GBP/CAD-OTC", "AUD/CAD-OTC", "NZD/JPY-OTC", "AUD/NZD-OTC", "EUR/NZD-OTC",
    "CHF/JPY-OTC", "EUR/CHF-OTC", "GBP/CHF-OTC", "CAD/CHF-OTC", "USD/INR-OTC",
    "USD/BRL-OTC", "USD/TRY-OTC", "USD/ZAR-OTC", "USD/MXN-OTC", "USD/SGD-OTC",
    "EUR/TRY-OTC", "GBP/TRY-OTC", "AUD/CHF-OTC", "NZD/CHF-OTC", "USD/RUB-OTC",
    "EUR/RUB-OTC", "GBP/NZD-OTC", "NZD/CAD-OTC", "AUD/SGD-OTC", "USD/CNH-OTC",
    "EUR/HKD-OTC", "GBP/SEK-OTC", "USD/PLN-OTC", "USD/NOK-OTC", "USD/SEK-OTC",
    "Apple-OTC", "Facebook-OTC", "Google-OTC", "Microsoft-OTC", "Amazon-OTC"
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI MASTER BINARY OTC V12</title>
    <style>
        body { background-color: #0d1117; color: white; font-family: Arial; text-align: center; padding: 20px; }
        .container { max-width: 500px; margin: auto; border: 2px solid #00ff88; border-radius: 15px; padding: 20px; background: #161b22; }
        h1 { color: #00ff88; text-shadow: 0 0 10px #00ff88; }
        select { width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; background: #0d1117; color: white; border: 1px solid #00ff88; }
        .signal-box { margin-top: 20px; padding: 20px; border-radius: 10px; background: #21262d; }
        .up { color: #00ff88; font-size: 30px; font-weight: bold; }
        .down { color: #ff4444; font-size: 30px; font-weight: bold; }
        .btn { background: #00ff88; color: #0d1117; padding: 15px 30px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; width: 100%; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 AI MASTER OTC V12</h1>
        <label>Select Currency (OTC):</label>
        <select id="pair">{% for pair in pairs %}<option value="{{ pair }}">{{ pair }}</option>{% endfor %}</select>
        <label>Select Timeframe:</label>
        <select id="timeframe"><option value="1">1 Minute</option><option value="5">5 Minutes</option></select>
        <div class="signal-box">
            <div id="pair-display" style="font-size: 18px; color: #8b949e;">READY</div>
            <div id="signal-result">--</div>
            <div id="target-time" style="font-size: 14px; color: #8b949e;"></div>
        </div>
        <button class="btn" onclick="generateSignal()">GET SIGNAL</button>
    </div>
    <script>
        function generateSignal() {
            const pair = document.getElementById('pair').value;
            const tf = parseInt(document.getElementById('timeframe').value);
            const res = Math.random() > 0.5 ? "UP (CALL) 🟢" : "DOWN (PUT) 🔴";
            document.getElementById('pair-display').innerText = pair;
            document.getElementById('signal-result').innerText = res;
            document.getElementById('signal-result').className = res.includes("UP") ? "up" : "down";
            let now = new Date();
            now.setMinutes(now.getMinutes() + tf);
            document.getElementById('target-time').innerText = "Target: " + now.getHours() + ":" + (now.getMinutes()<10?'0':'') + now.getMinutes();
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, pairs=OTC_PAIRS)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
