import streamlit as st
import google.generativeai as genai

# ၁။ Secrets ထဲက API Key ကို ယူခြင်း
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key မတွေ့ပါ။ Settings > Secrets ထဲမှာ 'GEMINI_API_KEY' ကို အရင်ထည့်ပေးပါ။")
    st.stop()

st.set_page_config(page_title="Movie Recap AI", page_icon="🎬")
st.title("🎬 Movie Recap AI (Narrator Version)")
st.write("ဇာတ်ကားနာမည် ရိုက်ထည့်ပြီး Professional Narrator Script ထုတ်ယူပါ။")

movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:", placeholder="ဥပမာ - Titanic")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        with st.spinner('AI က Professional Narrator တစ်ယောက်လို စဉ်းစားပေးနေပါတယ်...'):
            try:
                # သင့် API နှင့် အလုပ်လုပ်သော Gemini 2.5 Flash ကို သုံးထားပါသည်
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                prompt = f"""
                မင်္ဂလာပါ၊ အခု {movie_name} ဇာတ်ကားရဲ့ အညွှန်းကို Narrator တစ်ယောက် ပြောပြနေတဲ့ပုံစံမျိုးနဲ့ မြန်မာလို ရေးပေးပါ။
                
                အောက်ပါအတိုင်း စီစဉ်ပေးပါ-
                ၁။ ဗီဒီယိုအစမှာ ပရိသတ်စိတ်ဝင်စားသွားအောင် ဆွဲဆောင်မှုရှိတဲ့ Intro (ဥပမာ- "ဒီနေ့မှာတော့..." သို့မဟုတ် "ဒီဇာတ်ကားလေးဟာ...") နဲ့ စတင်ပါ။
                ၂။ ဇာတ်လမ်းရဲ့ အဓိက အနှစ်သာရနဲ့ ဇာတ်ကောင်တွေကို မိတ်ဆက်ပါ။
                ၃။ ဇာတ်လမ်းအလှည့်အပြောင်း (Plot twist) တွေကို စိတ်လှုပ်ရှားစရာကောင်းအောင် ရေးပါ။
                ၄။ နိဂုံးမှာ မှတ်ချက် ဒါမှမဟုတ် သင်ခန်းစာ တစ်ခုခုထည့်ပေးပါ။
                
                မှတ်ချက် - Text-to-Speech (TTS) နဲ့ ပြန်ဖတ်တဲ့အခါ အသံထွက် သဘာဝကျအောင် စာသားကို ရှင်းရှင်းလင်းလင်း ရေးပေးပါ။
                """
                
                response = model.generate_content(prompt)
                
                st.success(f"'{movie_name}' အတွက် Narrator Script ရပါပြီ")
                st.markdown(response.text)
                
            except Exception as e:
                # 429 Quota Error တက်လျှင် ပြမည့်စာသား
                if "429" in str(e):
                    st.error("Error: ခဏအတွင်း မေးခွန်းအမေးများသွားလို့ပါ။ ၁ မိနစ်လောက်စောင့်ပြီးမှ ပြန်နှိပ်ပေးပါ။")
                else:
                    st.error(f"Error တက်သွားပါတယ်- {e}")
    else:
        st.warning("ကျေးဇူးပြု၍ ဇာတ်ကားနာမည် အရင်ရိုက်ပေးပါ။")

