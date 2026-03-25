import os
import random
from flask import Flask, render_template_string, jsonify, request
from datetime import datetime

app = Flask(__name__)

last_signal = {"minute": -1, "direction": "", "pair": ""}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI MASTER CLOUD V11</title>
    <style>
        :root { --neon: #00ffcc; --bg: #05070a; --red: #ff4d4d; --green: #00ff88; }
        body { font-family: sans-serif; background: var(--bg); color: white; text-align: center; margin: 0; }
        .container { max-width: 400px; margin: auto; padding: 20px; }
        #chart { width: 100%; height: 300px; border-radius: 15px; background: #000; margin: 15px 0; }
        .signal-card { background: #0d1117; padding: 20px; border-radius: 20px; border: 1px solid #333; }
        .btn { background: var(--neon); color: #000; padding: 15px; width: 100%; border-radius: 10px; font-weight: bold; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h2 style="color: var(--neon);">🚀 AI MASTER CLOUD V11</h2>
        <div id="chart"></div>
        <div id="result" class="signal-card"><p>সার্ভার কানেক্টেড। সিগন্যাল নিন।</p></div>
        <button class="btn" style="margin-top:20px;" onclick="fetchSignal()">GET INSTANT SIGNAL</button>
    </div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
        new TradingView.widget({"autosize": true, "symbol": "FX:EURUSD", "interval": "1", "theme": "dark", "container_id": "chart"});
        async function fetchSignal() {
            const res = await fetch('/api/get_signal?pair=EURUSD');
            const data = await res.json();
            const resDiv = document.getElementById('result');
            const isUp = data.dir.includes("UP");
            resDiv.innerHTML = `<h3>${data.pair}</h3><div style="font-size:40px; color:${isUp ? '#00ff88' : '#ff4d4d'}">${data.dir}</div><small>টার্গেট: ${data.target_min}</small>`;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/get_signal')
def get_signal():
    global last_signal
    now = datetime.now()
    current_min = now.minute
    pair = request.args.get('pair', 'EUR/USD (OTC)')
    if last_signal["minute"] == current_min:
        return jsonify({"dir": last_signal["direction"], "target_min": f"{now.hour}:{current_min + 1}", "pair": pair})
    new_dir = random.choice(["UP (CALL)", "DOWN (PUT)"])
    last_signal = {"minute": current_min, "direction": new_dir, "pair": pair}
    return jsonify({"dir": new_dir, "target_min": f"{now.hour}:{current_min + 1}", "pair": pair})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
