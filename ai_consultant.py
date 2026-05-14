import streamlit as st
import requests

# আপনার এপিআই কি এখানে দিন
OPENROUTER_API_KEY = "YOUR_API_KEY_HERE"

def show_chat_box(live_data):
    st.subheader("💬 Elite AI Consultant")
    st.write("---")
    
    # ইউজার ইনপুট বক্স
    user_msg = st.text_input("সিস্টেমকে আপনার প্রশ্ন করুন:", placeholder="যেমন: এখন ট্রেড নেওয়া কি ঠিক হবে?")
    
    if st.button("পরামর্শ নিন"):
        if not OPENROUTER_API_KEY or "YOUR_API_KEY" in OPENROUTER_API_KEY:
            st.error("দয়া করে আপনার API Key সেট করুন।")
            return

        if live_data:
            # এআই-কে পাঠানোর জন্য বর্তমান মার্কেটের অবস্থা (Context)
            market_context = f"Price: {live_data['Price']}, Psychology: {live_data['Psychology']}%, News: {live_data['News']}%."
            
            with st.spinner("এআই এনালাইসিস করছে..."):
                try:
                    response = requests.post(
                        url="https://openrouter.ai/api/v1/chat/completions",
                        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
                        json={
                            "model": "google/gemini-2.0-flash-001",
                            "messages": [
                                {"role": "system", "content": "You are an Elite Trading Consultant. Answer in simple Bengali or English based on 95% logic."},
                                {"role": "user", "content": f"Market Data: {market_context}. User Question: {user_msg}"}
                            ]
                        }
                    )
                    advice = response.json()['choices'][0]['message']['content']
                    st.info(f"**Elite AI পরামর্শ:** {advice}")
                except:
                    st.error("এই মুহূর্তে এআই কানেকশন পাওয়া যাচ্ছে না।")
