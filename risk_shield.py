def check_risk_level(volatility_score):
    # রিস্ক ম্যানেজমেন্ট লজিক
    if volatility_score > 0.05:
        return "HIGH RISK ⚠️", "Skip This Trade"
    return "SAFE ✅", "Ready to Execute"
