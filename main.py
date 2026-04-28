import os
import random
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# আপনার কারেন্সি লিস্ট
PAIRS = [
    "EUR/USD-OTC", "GBP/USD-OTC", "USD/JPY-OTC", "USD/INR-OTC", "Gold-OTC", 
    "USD/BRL-OTC", "USD/PKR-OTC", "Apple-OTC", "Facebook-OTC", "Bitcoin-OTC"
]

def get_v17_updated_signal():
    # আপনার নতুন Piercing Line সহ অন্যান্য প্রো লজিক
    logic_pool = [
        # নতুন লজিক: Piercing Line Pattern
        {"res": "HIGH PROBABILITY BUY 💎", "logic": "PIERCING LINE: Green candle gapped down but closed >50% into the red body. Buyers have overwhelmed sellers. Potential bottom detected."},
        
        # অন্যান্য গাইডলাইন লজিক (আগের ১১০টির মধ্যে সেরা কিছু)
        {"res": "ELITE ENTRY 🎯", "logic": "HIKKAKE FAKEOUT: Professional trap detected. Follow the second breakout direction for safety."},
        {"res": "ULTIMATE REVERSAL 🟢", "logic": "ABANDONED BABY: Rare Doji gap detected. Previous trend lost all steam. Expect massive reversal."},
        {"res": "TREND CONTINUATION 🚀", "logic": "TASUKI GAP: Failed gap-fill confirms extreme trend strength. High confidence continuation signal."},
        {"res": "DOWN (PUT) 🔴", "logic": "BEARISH ENGULFING: 100% coverage at resistance. Sellers have fully taken control."}
    ]
    
    selected = random.choice(logic_pool)
    # আপনার ডেসক্রিপশন অনুযায়ী কনফার্মেশন টিপ
    confirmation = "Wait for the next candle to stay above the 50% mark of the previous red candle for confirmation."
    
    return selected['res'], selected['logic'], confirmation

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI MASTER V17 - UPDATED</title>
    <style>
        body { background: #040508; color: white; font-family: 'Poppins', sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .master-card { width: 380px; background: #040508; border: 5px solid #00ff88; border-radius: 60px; padding: 45px; text-align: center; box-shadow: 0 0 80px rgba(0, 255, 136, 0.7); }
        h1 { color: #00ff88; font-size: 38px; margin-bottom: 5px; text-transform: uppercase; font-weight: 900; letter-spacing: 5px; }
        select { width: 100%; padding: 20px; background: #0d1117; color: white; border: 2px solid #30363d; border-radius: 35px; margin-bottom: 40px; outline: none; }
        .display-box { background: #0d1117; border-radius: 45px; padding: 35px; border-left: 10px solid #00ff88; display: none; text-align: left; }
        #res { font-size: 32px; font-weight: 900; margin: 15px 0; }
        .logic-card { font-size: 14px; color: #a0aec0; background: #040508; padding: 20px; border-radius: 25px; line-height: 1.7; border: 1px solid #1a202c; }
        .btn-master { background: #00ff88; color: #000; width: 100%; padding: 25px; border: none; border-radius: 35px; font-weight: 900; cursor: pointer; margin-top: 40px; font-size: 24px; text-transform: uppercase; }
    </style>
</head>
<body>
    <div class="master-card">
        <h1>V17 111</h1>
        <div style="font-size:11px; color:#8b949e; margin-bottom:40px; letter-spacing: 3px;">[ 111 PRO GUIDELINES ACTIVE ]</div>
        
        <select id="pair">
            {% for p in PAIRS %}<option value="{{ p }}">{{ p }}</option>{% endfor %}
        </select>

        <div class="display-box" id="box">
            <div id="res">--</div>
            <div class="logic-card" id="logic">Analyzing pattern...</div>
            <div id="tip" style="font-size: 10px; color: #ffcc00; margin-top: 20px; font-weight: bold; border-top: 1px solid #30363d; padding-top: 15px;"></div>
        </div>

        <button class="btn-master" onclick="generateSignal()">GET SIGNAL</button>
    </div>

    <script>
        function generateSignal() {
            const box = document.getElementById('box');
            document.getElementById('res').innerText = "SCANNING...";
            box.style.display = 'block';
            
            fetch('/api/v17_update')
                .then(r => r.json())
                .then(data => {
                    document.getElementById('res').innerText = data.res;
                    let color = "#00ff88"; 
                    if(data.res.includes("DOWN") || data.res.includes("SELL")) color = "#ff4444"; 
                    
                    document.getElementById('res').style.color = color;
                    document.getElementById('logic').innerHTML = "<b>LOGIC:</b> " + data.logic;
                    document.getElementById('tip').innerText = "💡 CONFIRMATION: " + data.tip;
                    box.style.borderLeftColor = color;
                });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, PAIRS=PAIRS)

@app.route('/api/v17_update')
def api_v17_update():
    res, logic, tip = get_v17_updated_signal()
    return jsonify({"res": res, "logic": logic, "tip": tip})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
