import pandas_ta as ta

def apply_elite_logic(df):
    # RSI এবং EMA ব্যবহার করে ট্র্যাপ ডিটেকশন
    df['RSI'] = ta.rsi(df['Close'], length=14)
    df['EMA_20'] = ta.ema(df['Close'], length=20)
    
    last_row = df.iloc[-1]
    # লজিক: যদি RSI খুব বেশি হয় আর দাম EMA-র ওপরে থাকে, তবে সেল (PUT) সিগন্যাল
    if last_row['RSI'] > 70 and last_row['Close'] > last_row['EMA_20']:
        return "DOWN (PUT) 🔴", "High - Trap Detected"
    elif last_row['RSI'] < 30 and last_row['Close'] < last_row['EMA_20']:
        return "UP (CALL) 🟢", "High - Support Bounce"
    else:
        return "WAIT ⏳", "Market Neutral"
