def get_elite_prediction(status):
    # ডার্ক সাইকোলজি প্রেডিকশন লজিক
    if status == "BULLISH_FLOW":
        return "CALL (UP) 🟢", 94 # ৯৪% কনফিডেন্স
    elif status == "BEARISH_FLOW":
        return "PUT (DOWN) 🔴", 92 # ৯২% কনফিডেন্স
    else:
        return "NEUTRAL ⏳", 0
