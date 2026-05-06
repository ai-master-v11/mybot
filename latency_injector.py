import time

def calculate_latency_gap(broker_time, server_time):
    # মিলি-সেকেন্ডের গ্যাপ খুঁজে বের করা
    gap = abs(broker_time - server_time)
    if gap > 0.005: # ৫ মিলি-সেকেন্ডের বেশি হলে
        return "GAP DETECTED ⚡", "Injecting Signal Now"
    return "Synced", "Waiting for Lag"
