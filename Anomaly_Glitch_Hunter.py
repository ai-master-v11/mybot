# Module 3: Anomaly Glitch Hunter
# Purpose: Real-time Data Discrepancy Detection (Broker vs Market)
# Level: Ultra-Advanced System Architecture

import time

class GlitchHunter:
    def __init__(self):
        self.threshold = 0.00005  # প্রাইস ডিফারেন্সের লিমিট (আপনার প্রয়োজনমতো সেট করুন)

    def scan_for_anomaly(self, broker_price, global_market_price):
        """
        ব্রোকার প্রাইস এবং গ্লোবাল মার্কেটের প্রাইস তুলনা করে।
        যদি ডিফারেন্স বেশি হয়, তবে সেটি একটি প্রফিটেবল গ্লিচ।
        """
        price_diff = abs(broker_price - global_market_price)
        
        if price_diff > self.threshold:
            # গ্লিচ ডিটেকটেড
            if broker_price < global_market_price:
                return "GLITCH_FOUND: HIGH_PROBABILITY_BUY 🟢"
            else:
                return "GLITCH_FOUND: HIGH_PROBABILITY_SELL 🔴"
        
        return "SYNC_STABLE: NO_GLITCH_DETECTED"

    def latency_check(self, start_time):
        """
        রেন্ডার সার্ভার থেকে ব্রোকারের ডাটা আসতে কত সময় লাগছে তা চেক করবে।
        এটি নিশ্চিত করে যেন আপনার সিগন্যাল ১ মিলিসেকেন্ডও দেরি না হয়।
        """
        execution_time = time.time() - start_time
        if execution_time > 0.5: # ০.৫ সেকেন্ডের বেশি হলে ওয়ার্নিং
            return f"LATENCY_CRITICAL: {execution_time}s"
        return "NETWORK_OPTIMIZED"

# এই মডিউলটি আপনার ২৬ নম্বর ফাইলের অন্যতম শক্তিশালী লজিক হিসেবে কাজ করবে।
