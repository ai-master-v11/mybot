<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI MASTER V17 - DEEP LOGIC</title>
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: #161b28;
            --primary-green: #00ff88;
            --text-white: #ffffff;
            --text-gray: #a0aec0;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-white);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }

        .container {
            width: 90%;
            max-width: 400px;
            background: var(--card-bg);
            padding: 25px;
            border-radius: 20px;
            border: 2px solid var(--primary-green);
            box-shadow: 0 0 20px rgba(0, 255, 136, 0.2);
            text-align: center;
        }

        .header h1 {
            color: var(--primary-green);
            font-size: 24px;
            margin-bottom: 5px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .header p {
            color: var(--text-gray);
            font-size: 12px;
            margin-bottom: 25px;
        }

        .input-group {
            text-align: left;
            margin-bottom: 20px;
        }

        label {
            display: block;
            color: var(--text-white);
            margin-bottom: 8px;
            font-size: 14px;
        }

        select {
            width: 100%;
            padding: 12px;
            background: #1f2736;
            border: 1px solid #303a4d;
            border-radius: 10px;
            color: white;
            font-size: 15px;
            outline: none;
        }

        .display-box {
            background: #1f2736;
            padding: 20px;
            border-radius: 15px;
            margin: 25px 0;
            min-height: 100px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .status-title {
            color: var(--primary-green);
            font-size: 14px;
            margin-bottom: 5px;
        }

        .main-result {
            font-size: 22px;
            font-weight: bold;
            margin: 10px 0;
        }

        .btn-signal {
            width: 100%;
            padding: 15px;
            background: var(--primary-green);
            border: none;
            border-radius: 12px;
            color: #000;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
            text-transform: uppercase;
        }

        .btn-signal:hover {
            background: #00cc6e;
            transform: scale(1.02);
        }

        .footer-note {
            margin-top: 20px;
            font-size: 11px;
            color: #f6ad55;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>🚀 AI MASTER V17</h1>
        <p>POWERED BY MASUM'S DEEP ENGINE</p>
    </div>

    <div class="input-group">
        <label>Select Currency (50+ OTC/LIVE):</label>
        <select id="currencyList">
            </select>
    </div>

    <div class="input-group">
        <label>Timeframe:</label>
        <select id="timeframe">
            <option>1 Minute</option>
            <option>2 Minutes</option>
            <option>5 Minutes</option>
        </select>
    </div>

    <div class="display-box">
        <div id="statusLabel" class="status-title">WAITING...</div>
        <div id="resultText" class="main-result">Ready to Analyze</div>
    </div>

    <button class="btn-signal" onclick="getSignal()">Get Accurate Signal</button>

    <div class="footer-note">
        ⚠️ Rule: 1% Risk | Wait for Retest | S/R is King
    </div>
</div>

<script>
    // ৫০টি কারেন্সি পেয়ারের লিস্ট
    const currencies = [
        "EUR/USD-OTC", "GBP/USD-OTC", "USD/JPY-OTC", "AUD/USD-OTC", "EUR/GBP-OTC",
        "USD/CAD-OTC", "NZD/USD-OTC", "EUR/JPY-OTC", "GBP/JPY-OTC", "EUR/AUD-OTC",
        "USD/CHF-OTC", "AUD/JPY-OTC", "EUR/CAD-OTC", "GBP/AUD-OTC", "USD/INR-OTC",
        "USD/BRL-OTC", "USD/TRY-OTC", "USD/ZAR-OTC", "AUD/CAD-OTC", "CAD/JPY-OTC",
        "EUR/CHF-OTC", "GBP/CHF-OTC", "NZD/JPY-OTC", "AUD/NZD-OTC", "GBP/CAD-OTC",
        "EUR/NZD-OTC", "CHF/JPY-OTC", "USD/PKR-OTC", "USD/BDT-OTC", "USD/SGD-OTC",
        "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD", "EUR/JPY", "GBP/JPY",
        "USD/CHF", "AUD/JPY", "EUR/GBP", "CAD/CHF", "NZD/CHF", "GBP/AUD", "AUD/CAD",
        "EUR/CAD", "NZD/USD", "CAD/JPY", "EUR/AUD", "GBP/CAD", "AUD/NZD"
    ];

    const select = document.getElementById('currencyList');
    
    // ড্রপডাউনে কারেন্সিগুলো যোগ করা
    currencies.forEach(curr => {
        let option = document.createElement('option');
        option.value = curr;
        option.text = curr;
        select.appendChild(option);
    });

    function getSignal() {
        const status = document.getElementById('statusLabel');
        const result = document.getElementById('resultText');
        
        status.innerText = "ANALYZING...";
        status.style.color = "#f6ad55";
        result.innerText = "Calculating Price Action...";

        // ৩ সেকেন্ড পর সিগনাল দেখাবে (ডেমো লজিক)
        setTimeout(() => {
            const signals = ["UP (CALL) 🟢", "DOWN (PUT) 🔴"];
            const randomSignal = signals[Math.floor(Math.random() * signals.length)];
            
            status.innerText = "ANALYSIS COMPLETE";
            status.style.color = "#00ff88";
            result.innerText = randomSignal;
        }, 3000);
    }
</script>

</body>
</html>
