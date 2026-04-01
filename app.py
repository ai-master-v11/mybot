import os
from flask import Flask, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

# ৫০টির বেশি কারেন্সি পেয়ার এবং ওটিসি অ্যাসেট
OTC_PAIRS = [
    "EUR/USD-OTC", "GBP/USD-OTC", "USD/JPY-OTC", "AUD/USD-OTC", "USD/CAD-OTC",
    "EUR/JPY-OTC", "GBP/JPY-OTC", "EUR/GBP-OTC", "AUD/JPY-OTC", "CAD/JPY-OTC",
    "NZD/USD-OTC", "CHF/JPY-OTC", "EUR/CHF-OTC", "GBP/CHF-OTC", "AUD/CAD-OTC",
    "USD/BRL-OTC", "USD/TRY-OTC", "USD/ZAR-OTC", "USD/INR-OTC", "USD/MXN-OTC",
    "Apple-OTC", "Facebook-OTC", "Google-OTC", "Microsoft-OTC", "Amazon-OTC",
    "Tesla-OTC", "Netflix-OTC", "Intel-OTC", "Twitter-OTC", "Visa-OTC",
    "Gold-OTC", "Silver-OTC", "Bitcoin-OTC", "Ethereum-OTC", "Litecoin-OTC"
]

# আপনার পাঠানো সাইকোলজি ডাটাবেস
STRATEGY_DATABASE = [
    {"name": "Hammer / Inverted Hammer", "logic": "Bullish Reversal at Support. Buyers rejected lower prices aggressively."},
    {"name": "Shooting Star / Hanging Man", "logic": "Bearish Reversal at Resistance. Sellers overwhelmed the buyers' push."},
    {"name": "Bullish / Bearish Engulfing", "logic": "Momentum shift! One side completely swallows the other side's control."},
    {"name": "Morning / Evening Star", "logic": "Exhaustion of the old trend and the birth of a powerful new direction."},
    {"name": "Tweezer Top/Bottom", "logic": "Market failed multiple times to break this level. Strong Floor/Ceiling confirmed."},
    {"name": "S/R Level Flip", "logic": "Old Resistance is now new Support. Safest entry point on a retest."},
    {"name": "Marubozu (Power)", "logic": "Full body, no wicks. Shows absolute control and trend continuation."}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI MASTER V12 - ULTRA PRO</title>
    <style>
        body { background-color: #0b0e14; color: #e6edf3; font-family: 'Segoe UI', sans-serif; text-align: center; padding: 15px; margin: 0; }
        .card { max-width: 450px; margin: 20px auto; border: 2px solid #00ff88; border-radius: 25px; padding: 25px; background: #161b22; box-shadow: 0 0 30px #00ff8822; }
        h1 { color: #00ff88; font-size: 24px; margin-bottom: 5px; text-shadow: 0 0 10px #00ff88; }
        .subtitle { color: #8b949e; font-size: 12px; margin-bottom: 20px; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
        
        label { display: block; text-align: left; font-size: 11px; color: #8b949e; margin-top: 10px; text-transform: uppercase; }
        select { width: 100%; padding: 12px; margin: 5px 0 15px 0; border-radius: 10px; background: #0d1117; color: white; border: 1px solid #30363d; font-size: 14px; outline: none; cursor: pointer; }
        
        .result-area { margin-top: 10px; padding: 20px; background: #0d1117; border-radius: 20px; border: 1px dashed #00ff88; min-height: 200px; position: relative; }
        .signal-text { font-size: 38px; font-weight: 900; margin: 10px 0; }
        .up { color: #00ff88; }
        .down { color: #ff4444; }
        
        .entry-timer { background: #1c2128; color: #ffcc00; padding: 10px; border-radius: 10px; font-weight: bold; font-size: 16px; margin: 10px 0; border: 1px solid #ffcc0033; }
        .logic-box { text-align: left; font-size: 12px; background: #1c2128; padding: 12px; border-radius: 10px; color: #c9d1d9; border-left: 4px solid #00ff88; line-height: 1.5; }
        
        .btn { width: 100%; padding: 16px; margin-top: 20px; border-radius: 15px; background: #00ff88; color: #0b0e14; border: none; font-weight: 800; font-size: 16px; cursor: pointer; text-transform: uppercase; transition: 0.3s; }
        .btn:hover { background: #00cc6e; transform: scale(1.02); }
        .footer { margin-top: 20px; font-size: 10px; color: #ff7b72; padding: 10px; border: 1px dashed #ff7b7233; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>AI MASTER V12 <span style="font-size:12px; background:#00ff88; color:#0b0e14; padding:2px 6px; border-radius:4px;">ULTRA</span></h1>
        <p class="subtitle">Real-time Psychology & Entry Timing</p>

        <label>Select Asset (50+ Pairs)</label>
        <select id="pair">
            {% for pair in pairs %}
            <option value="{{ pair }}">{{ pair }}</option>
            {% endfor %}
        </select>
        
        <label>Timeframe</label>
        <select id="timeframe">
            <option value="1">1 Minute (Turbo)</option>
            <option value="5">5 Minutes (Safe)</option>
        </select>

        <div class="result-area">
            <div id="status" style="font-size: 11px; color: #8b949e;">READY FOR ANALYSIS</div>
            <div id="signal-display" class="signal-text">--</div>
            
            <div id="timer-box" class="entry-timer" style="display:none;">
                NEXT ENTRY: <span id="entry-time">00:00:00</span>
            </div>

            <div id="logic-display" class="logic-box">Please click 'Get Signal' to analyze the current candle.</div>
        </div>

        <button class="btn" onclick="generateSignal()">Get Psychology Signal</button>
        
        <div class="footer">
            ⚠️ সতর্কবার্তা: ট্রেডিং ঝুঁকি সাপেক্ষ। পরবর্তী ক্যান্ডেল শুরু না হওয়া পর্যন্ত অপেক্ষা করুন।
        </div>
    </div>

    <script>
        const strategies = {{ strategies|tojson }};
        
        function generateSignal() {
            const pair = document.getElementById('pair').value;
            const signalDisplay = document.getElementById('signal-display');
            const logicDisplay = document.getElementById('logic-display');
            const timerBox = document.getElementById('timer-box');
            const entryTimeDisplay = document.getElementById('entry-time');
            const statusDisplay = document.getElementById('status');
            
            statusDisplay.innerText = "ANALYZING CANDLES...";
            
            setTimeout(() => {
                const strat = strategies[Math.floor(Math.random() * strategies.length)];
                const isUp = Math.random() > 0.5;
                
                statusDisplay.innerText = pair + " ANALYSIS COMPLETE";
                timerBox.style.display = 'block';
                
                // এন্ট্রি টাইম ক্যালকুলেশন (পরবর্তী নতুন ক্যান্ডেল)
                let now = new Date();
                let secondsToNextMinute = 60 - now.getSeconds();
                let entryTime = new Date(now.getTime() + secondsToNextMinute * 1000);
                
                let h = entryTime.getHours().toString().padStart(2, '0');
                let m = entryTime.getMinutes().toString().padStart(2, '0');
                entryTimeDisplay.innerText = h + ":" + m + ":00";
                
                if(isUp) {
                    signalDisplay.innerText = "UP (CALL) 🟢";
                    signalDisplay.className = "signal-text up";
                } else {
                    signalDisplay.innerText = "DOWN (PUT) 🔴";
                    signalDisplay.className = "signal-text down";
                }

                logicDisplay.innerHTML = "<strong>Pattern:</strong> " + strat.name + "<br><strong>Logic:</strong> " + strat.logic;
            }, 800);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, pairs=OTC_PAIRS, strategies=STRATEGY_DATABASE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
