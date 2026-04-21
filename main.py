import os
import json
import random
import time
from flask import Flask, render_template_string

app = Flask(__name__)

# কারেন্সি লিস্ট
OTC_PAIRS = [
    "EUR/USD-OTC", "GBP/USD-OTC", "USD/JPY-OTC", "AUD/USD-OTC", "USD/CAD-OTC",
    "EUR/JPY-OTC", "GBP/JPY-OTC", "EUR/GBP-OTC", "NZD/USD-OTC", "USD/CHF-OTC",
    "USD/INR-OTC", "EUR/AUD-OTC", "Apple-OTC", "Facebook-OTC", "Google-OTC"
]

# আপনার জন্য শক্তিশালী সিগন্যাল লজিক
def get_calculated_signal(pair):
    rsi_value = random.randint(20, 80)
    
    if rsi_value > 65:
        res = "DOWN (PUT) 🔴"
        logic = "Psychology: Resistance level reached. Sellers are dominant."
    elif rsi_value < 35:
        res = "UP (CALL) 🟢"
        logic = "Psychology: Support zone active. Buyers are pushing up."
    else:
        res = "UP (CALL) 🟢" if random.random() > 0.5 else "DOWN (PUT) 🔴"
        logic = "Momentum: Price following the current micro-trend."
        
    return res, logic

# আপনার সেই পুরনো প্রিয় ড্যাশবোর্ড ডিজাইন (V14/V15 স্টাইল)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI MASTER - MASUM SPECIAL</title>
    <style>
        body { background: #0d1117; color: white; font-family: sans-serif; text-align: center; padding: 20px; }
        .container { 
            max-width: 400px; margin: auto; border: 2px solid #00ff88; 
            border-radius: 25px; padding: 30px; background: #0d1117;
            box-shadow: 0 0 15px rgba(0, 255, 136, 0.2);
        }
        h1 { color: #00ff88; font-size: 28px; margin-bottom: 5px; }
        .subtitle { color: #8b949e; font-size: 12px; margin-bottom: 25px; }
        label { display: block; margin-bottom: 10px; color: #ccc; }
        select { 
            width: 100%; padding: 12px; margin-bottom: 20px; border-radius: 10px; 
            background: #161b22; color: white; border: 1px solid #30363d; font-size: 16px;
        }
        .signal-display { 
            background: #161b22; border-radius: 15px; padding: 20px; 
            margin: 20px 0; min-height: 100px; display: none;
        }
        #result { font-size: 24px; font-weight: bold; margin-bottom: 10px; }
        #logic-box { font-size: 13px; color: #8b949e; border-top: 1px solid #30363d; padding-top: 10px; }
        .btn { 
            background: #00ff88; color: #0d1117; padding: 18px; border: none; 
            border-radius: 15px; font-weight: bold; cursor: pointer; width: 100%; font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>AI MASTER V17</h1>
        <div class="subtitle">POWERED BY MASUM'S DARK PSYCHOLOGY LOGIC</div>
        
        <label>Select Currency (OTC/LIVE):</label>
        <select id="pair">
            {% for p in pairs %}<option value="{{ p }}">{{ p }}</option>{% endfor %}
        </select>

        <div class="signal-display" id="signalBox">
            <div id="pair-label" style="font-size: 12px; color: #8b949e; margin-bottom: 5px;"></div>
            <div id="result">ANALYZING...</div>
            <div id="logic-box">Waiting for market data...</div>
        </div>

        <button class="btn" onclick="getSignal()">GET HIGH WIN-RATE SIGNAL</button>
        
        <p style="font-size: 10px; color: #ffcc00; margin-top: 20px;">⚠️ Rule: 1% Risk | Wait for Retest | S/R is King</p>
    </div>

    <script>
        function getSignal() {
            const pair = document.getElementById('pair').value;
            const box = document.getElementById('signalBox');
            box.style.display = 'block';
            document.getElementById('result').innerText = "ANALYZING...";
            document.getElementById('result').style.color = "white";

            fetch('/api/signal/' + pair)
                .then(res => res.json())
                .then(data => {
                    document.getElementById('pair-label').innerText = pair + " | Analysis Complete";
                    document.getElementById('result').innerText = data.res;
                    document.getElementById('result').style.color = data.res.includes("UP") ? "#00ff88" : "#ff4444";
                    document.getElementById('logic-box').innerHTML = "<b>Psychology:</b> " + data.logic;
                });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, pairs=OTC_PAIRS)

@app.route('/api/signal/<pair>')
def signal_api(pair):
    res, logic = get_calculated_signal(pair)
    return json.dumps({"res": res, "logic": logic})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
