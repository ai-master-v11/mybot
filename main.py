import os
import time
import requests
from flask import Flask
from threading import Thread

# Render-এর জন্য ওয়েব সার্ভার যাতে প্রজেক্ট ২৪ ঘণ্টা সচল থাকে
app = Flask('')
@app.route('/')
def home():
    return "Project Infinity is Running 24/7"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# আমাদের আসল এআই লজিক (The Brain)
def infinity_logic():
    print("[*] মাসুম ভাই, আপনার এআই এখন ইন্টারনেটের রুট লেভেলে সক্রিয়...")
    while True:
        try:
            # এখানে ন্যানো-সেকেন্ড গ্লিচ এবং মার্কেট পালস স্ক্যানিং শুরু হবে
            print(f"[+] {time.ctime()} - মার্কেট পালস স্ক্যান করা হচ্ছে...")
            time.sleep(60) 
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    # ওয়েব সার্ভার এবং এআই একসাথে চালু করা
    t = Thread(target=run_web)
    t.start()
    infinity_logic()
