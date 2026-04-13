import streamlit as st
import google.generativeai as genai

# ၁။ Secrets ထဲက API Key ကို ယူခြင်း
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key မတွေ့ပါ။")
    st.stop()

st.title("🎬 Movie Recap AI")
movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        with st.spinner('AI က ဇာတ်လမ်းကို စဉ်းစားနေပါတယ်...'):
            try:
                # သင့် API စာရင်းထဲမှာပါတဲ့ gemini-2.5-flash ကို သုံးပါ
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # --- ဒီနေရာမှာ အသစ်ပြောင်းလိုက်တဲ့ Prompt ကို ထည့်ပါ ---
                prompt = f"""
                မင်္ဂလာပါ၊ အခု {movie_name} ဇာတ်ကားရဲ့ အညွှန်းကို Narrator တစ်ယောက် ပြောပြနေတဲ့ပုံစံမျိုးနဲ့ မြန်မာလို ရေးပေးပါ။
                အောက်ပါ အချက်တွေ ပါဝင်ပါစေ-
                ၁။ ဗီဒီယိုအစမှာ ပရိသတ်စိတ်ဝင်စားသွားအောင် ဆွဲဆောင်မှုရှိတဲ့ Intro နဲ့ စတင်ပါ။
                ၂။ ဇာတ်လမ်းရဲ့ အဓိက အနှစ်သာရနဲ့ ဇာတ်ကောင်တွေကို မိတ်ဆက်ပါ။
                ၃။ ဇာတ်လမ်းအလှည့်အပြောင်း (Plot twist) တွေကို စိတ်လှုပ်ရှားစရာကောင်းအောင် ရေးပါ။
                ၄။ နိဂုံးမှာ မှတ်ချက် ဒါမှမဟုတ် သင်ခန်းစာ တစ်ခုခုထည့်ပေးပါ။
                
                မှတ်ချက် - Text-to-Speech နဲ့ ဖတ်တဲ့အခါ အဆင်ပြေအောင် စာသားတွေကို သဘာဝကျကျနဲ့ ရှင်းရှင်းလင်းလင်း ရေးပေးပါ။
                """
                # --------------------------------------------------
                
                response = model.generate_content(prompt)
                
                st.success(f"'{movie_name}' အတွက် Narrator Script ရပါပြီ")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
                
