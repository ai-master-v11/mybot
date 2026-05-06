def hijack_broker_logic(trend_strength):
    # ব্রোকারের ফেক ট্রেন্ড লজিক হাইজ্যাক করা
    if trend_strength > 0.95: # অতিরিক্ত কনফিডেন্স মানেই ট্র্যাপ
        return "REVERSE SIGNAL 🔄", "Algorithm Hijack Success"
    return "Normal Flow", "Safe"
