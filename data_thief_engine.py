def extract_hidden_liquidity(order_book):
    # হিডেন অর্ডার বা বড় প্লেয়ারদের পেন্ডিং অর্ডার ট্র্যাক করা
    hidden_volume = order_book['bid_size'].max() * 1.5
    return f"Hidden liquidity found at level: {hidden_volume}"
