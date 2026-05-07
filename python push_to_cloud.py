from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def dashboard():
    # এটি রেন্ডারে রান করলে আপনি ব্রাউজারে দেখতে পাবেন
    html = """
    <body style="background-color:#0d1117; color:#58a6ff; font-family: sans-serif; text-align:center; padding:50px;">
        <h1 style="color:#238636;">🚀 Project 07: The Elite Hunt - Online</h1>
        <hr style="border:0.5px solid #30363d;">
        <div style="margin-top:20px;">
            <p><b>System Status:</b> <span style="color:#39d353;">ACTIVE (Vision 2030)</span></p>
            <p><b>Active Modules:</b> 26 Files Synced</p>
            <p><b>Execution Node:</b> Render Cloud</p>
            <p><b>Signal Precision:</b> 95% Quantum Accuracy</p>
        </div>
        <div style="margin-top:30px; font-size:12px; color:#8b949e;">
            Master Brain: The_Elite_Architect_2030.py
        </div>
    </body>
    """
    return html

if __name__ == "__main__":
    # রেন্ডার পোর্টের সাথে কানেক্ট করার জন্য
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
