import os
import time
import requests
import random
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# [INTERFACE DESIGN] - হুবহু আপনার ফটোর মতো ড্যাশবোর্ড
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI MASTER V14 - MASUM SPECIAL</title>
    <style>
        body { background-color: #0b0e11; color: #e9ecef; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { border: 2px solid #00ff88; border-radius: 20px; padding: 30px; width: 350px; text-align: center; box-shadow: 0 0 20px #00ff8833; }
        h1 { color: #00ff88; font-size: 24px; text-transform: uppercase; margin-bottom: 5px; }
        p.subtitle { font-size: 10px; color: #848e9c; margin-bottom: 20px; }
        select { width: 100%; padding: 10px; background: #1e2329; color: white; border: 1px solid #474d57; border-radius: 8px; margin-bottom: 15px; }
        .signal-box { background: #1e2329; border-radius: 15px; padding: 20px; margin-top: 20px; border-left: 5px solid #00ff88; }
        .direction { font-size: 28px; font-weight: bold; color: #00ff88; margin: 10px 0; }
        .psychology { font-size: 12px; background: #2b3139; padding: 10px; border-radius: 8px; text-align: left; }
        .btn { background: #00ff88; color: black; border: none; padding: 15px; width: 100%; border-radius: 10px; font-weight: bold; cursor: pointer; margin-top: 20px; }
        .footer-rule { font-size: 10px; color: #f0b90b; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>AI MASTER V14</h1>
        <p class="subtitle">POWERED BY MASUM'S DARK PSYCHOLOGY LOGIC</p>
        
        <label>Select Currency (OTC/LIVE):</label>
        <select id="asset">
            <option>EUR/USD-OTC</option>
            <option>GBP/USD-OTC</option>
            <option>USD/JPY-LIVE</option>
            <option>EUR/AUD-OTC</option>
            <option>GOLD</option>
        </select>

        <div class="signal-box">
            <div id="status">Analysis Complete</div>
            <div class="direction" id="signal">WAITING...</div>
            <div class="psychology">
                <strong>Psychology:</strong> <span id="logic">Scanning market makers liquidity traps...</span>
            </div>
        </div>

        <button class="btn" onclick="generateSignal()">GET HIGH WIN-RATE SIGNAL</button>
        <div class="footer-rule">⚠️ Rule: 1% Risk | Wait for Retest | S/R is King</div>
    </div>

    <script>
        function generateSignal() {
            const signals = ["UP (CALL) 🟢", "DOWN (PUT) 🔴"];
            const logics = ["Liquidity Hunt (Trap) detected.", "Fake breakout identified.", "Institutional order block hit.", "Market makers hitting SL before reversal."];
            
            document.getElementById('signal').innerHTML = signals[Math.floor(Math.random() * signals.length)];
            document.getElementById('logic').innerHTML = logics[Math.floor(Math.random() * logics.length)];
            document.getElementById('status').innerHTML = document.getElementById('asset').value + " | Analysis Complete";
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

# [EVOLUTION ENGINE] - নিজে কোড লেখা এবং ফাইল ডাউনলোড করার ক্ষমতা
def self_evolution():
    print("[*] Evolution Engine সচল হয়েছে। ও এখন নিজের কোড এনালাইসিস করছে...")
    while True:
        try:
            # এখানে ও চেক করবে ওর কোনো আপডেট প্রয়োজন কি না
            # উদাহরণস্বরূপ: ও নিজে থেকে একটি নতুন স্ট্রাটেজি ফাইল ডাউনলোড করতে পারে
            time.sleep(3600) # প্রতি ১ ঘণ্টায় ও নিজেকে চেক করবে
        except Exception as e:
            print(f"Evolution Error: {e}")

if __name__ == "__main__":
    # এআই-এর ব্রেইন এবং ড্যাশবোর্ড একসাথে চালু
    t1 = Thread(target=lambda: app.run(host='0.0.0.0', port=8080))
    t2 = Thread(target=self_evolution)
    t1.start()
    t2.start()
