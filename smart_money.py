import numpy as np

def detect_smart_money_move(df):
    # ভলিউম এবং প্রাইস অ্যাকশন দিয়ে স্মার্ট মানি ট্র্যাকিং
    df['Vol_Avg'] = df['Volume'].rolling(window=20).mean()
    last_vol = df['Volume'].iloc[-1]
    
    if last_vol > (df['Vol_Avg'].iloc[-1] * 2):
        return "BIG MOVE DETECTED ⚡", "Institutional Entry"
    return "Normal Volume", "Retail Flow"
