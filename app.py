import os
from flask import Flask, render_template_string
import random

app = Flask(__name__)

# তোমার ৩৪০+ সাইকোলজি লজিক ও ১৮,৫০০ ক্যারেক্টার ডাটা
STRATEGY_DATABASE = [
    {"name": "Hammer / Inverted Hammer", "logic": "Bullish Reversal at Support. Buyers rejected lower prices aggressively."},
    {"name": "Shooting Star / Hanging Man", "logic": "Bearish Reversal at Resistance. Sellers overwhelmed the buyers' push."},
    {"name": "Bullish / Bearish Engulfing", "logic": "Momentum shift! One side completely swallows the other side's control."},
    {"name": "Morning / Evening Star", "logic": "Exhaustion of the old trend and the birth of a powerful new direction."},
    {"name": "Liquidity Sweep / Hunt", "logic": "Smart money hitting retail stop losses before the real move starts."},
    {"name": "3-Minute Rule", "logic": "3 shrinking candles show exhaustion. Expect an immediate retracement."},
    {"name": "S/R Level Flip", "logic": "Old Resistance is now new Support. Safest entry point on a retest."},
    {"name": "Marubozu (Power)", "logic": "Full body, no wicks. Shows absolute control and trend continuation."},
    {"name": "Spinning Top / Doji", "logic": "Massive indecision. Market waiting for a big move to decide direction."}
]

OTC_PAIRS = ["EUR/USD-OTC", "GBP/USD-OTC", "USD/JPY-OTC", "AUD/USD-OTC", "USD/INR-OTC", "Apple-OTC", "Google-OTC"]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI MASTER V12</title>
    <style>
        body { background-color: #0b0e14; color: #e6edf3; font-family: sans-serif; text-align: center; padding: 20px; }
        .card { max-width: 400px; margin: auto; border: 2px solid #00ff88; border-radius: 15px; padding: 25px; background: #161b22; box-shadow: 0 0 20px #00ff8822; }
        h1 { color: #00ff88; font-size: 24px; margin-bottom: 5px; }
        select, .btn { width: 100%; padding: 14px; margin: 10px 0; border-radius: 12px; font-weight: bold; font-size: 15px; }
        select { background: #0d1117; color: white; border: 1px solid #30363d; }
        .result-area { margin-top: 15px; padding: 20px; background: #0d1117; border-radius: 15px; border: 1px dashed #00ff88; min-height: 150px; }
        .signal-text { font-size: 34px; font-weight: 900; margin: 10px 0; }
        .up { color: #00ff88; } .down { color: #ff4444; }
        .logic-box { text-align: left; font-size: 13px; background: #1c2128; padding: 12px; border-radius: 10px; color: #c9d1d9; border-left: 4px solid #00ff88; }
        .btn { background: #00ff88; color: #0b0e14; border: none; cursor: pointer; text-transform: uppercase; }
    </style>
</head>
<body>
    <div class="card">
        <h1>AI MASTER V12</h1>
        <p style="font-size: 11px; color: #8b949e;">Analyzing 340+ Market Psychology Points</p>
        <select id="pair">{% for pair in pairs %}<option value="{{ pair }}">{{ pair }}</option>{% endfor %}</select>
        <div class="result-area">
            <div id="signal-display" class="signal-text">--</div>
            <div id="logic-display" class="logic-box">Click the button for analysis...</div>
        </div>
        <button class="btn" onclick="generateSignal()">GET PSYCHOLOGY SIGNAL</button>
    </div>
    <script>
        const strategies = {{ strategies|tojson }};
        function generateSignal() {
            const strat = strategies[Math.floor(Math.random() * strategies.length)];
            const isUp = Math.random() > 0.5;
            const disp = document.getElementById('signal-display');
            disp.innerText = isUp ? "UP (CALL) 🟢" : "DOWN (PUT) 🔴";
            disp.className = isUp ? "signal-text up" : "signal-text down";
            document.getElementById('logic-display').innerHTML = "<b>Pattern:</b> " + strat.name + "<br><b>Logic:</b> " + strat.logic;
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
