def analyze_trader_psychology(rsi_value):
    # ট্রেডারদের মানসিক অবস্থা এনালাইসিস
    if rsi_value > 80:
        return "GREED PEAK 📉", "Expecting Reversal"
    elif rsi_value < 20:
        return "FEAR PEAK 📈", "Expecting Bounce"
    return "Neutral Sentiment", "No Emotion Bias"
