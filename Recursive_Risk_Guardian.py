# Module 6: Recursive Risk Guardian
# Purpose: Dynamic Capital Protection & Circuit Breaker System
# Standard: Vision 2030 Institutional Risk Management

class RiskGuardian:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.max_daily_loss_percent = 0.10 # দিনে ১০% লস হলে সিস্টেম বন্ধ
        self.daily_loss_limit = initial_balance * self.max_daily_loss_percent
        self.current_daily_loss = 0
        self.is_locked = False

    def calculate_safe_stake(self, win_rate, market_volatility):
        """
        মার্কেট কন্ডিশন এবং আপনার উইন রেট দেখে সেফ স্টেক (Stake) বের করা।
        """
        if self.is_locked:
            return 0 # সিস্টেম লক থাকলে কোনো ট্রেড হবে না

        # ক্যালকুলেশন: একুরেসি বেশি হলে স্টেক বাড়বে, ভোলাটালিটি বেশি হলে স্টেক কমবে
        base_stake = self.balance * 0.01 # ১% ডিফল্ট রিস্ক
        
        if market_volatility > 0.8: # হাই ভোলাটালিটি
            safe_stake = base_stake * 0.5
        elif win_rate > 0.85: # হাই একুরেসি
            safe_stake = base_stake * 1.5
        else:
            safe_stake = base_stake
            
        return round(safe_stake, 2)

    def update_account_status(self, trade_result_amount):
        """
        প্রতিটি ট্রেডের পর লস ট্র্যাক করা এবং সার্কিট ব্রেকার চেক করা।
        """
        if trade_result_amount < 0:
            self.current_daily_loss += abs(trade_result_amount)

        if self.current_daily_loss >= self.daily_loss_limit:
            self.is_locked = True
            return "CIRCUIT_BREAKER_TRIGGERED: System Locked for 24 Hours 🛡️"
        
        return f"Daily Loss: {self.current_daily_loss}/{self.daily_loss_limit}"

# এই ফাইলটি আপনার প্রজেক্টের 'ফাইন্যান্সিয়াল ডিরেক্টর' হিসেবে কাজ করবে।
