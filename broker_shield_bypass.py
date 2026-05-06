import random

def rotate_digital_signature():
    # ডিজিটাল সিগনেচার পরিবর্তন করা যেন ব্রোকার ডিটেক্ট করতে না পারে
    signatures = ["Chrome_Win10", "Safari_MacOS", "Firefox_Linux"]
    selected = random.choice(signatures)
    return f"Agent Masked as: {selected}"
