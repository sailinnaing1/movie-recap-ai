import streamlit as st
import google.generativeai as genai

# ၁။ API Key စစ်ဆေးခြင်း
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key မတွေ့ပါ။")
    st.stop()

st.set_page_config(page_title="Movie Recap AI Pro", page_icon="🎬")
st.title("🎬 Movie Recap AI (Professional)")

# ၂။ Sidebar မှာ မိနစ်ရွေးချယ်မှု ထည့်ခြင်း
st.sidebar.header("တင်ဆက်မှု ပုံစံ")
duration = st.sidebar.selectbox(
    "ဗီဒီယို ကြာချိန် ရွေးချယ်ပါ:",
    ("၃ မိနစ်စာ (အကျဉ်းချုပ်)", "၅ မိနစ်စာ (အသေးစိတ်)", "၁၀ မိနစ်စာ (Full Story)")
)

movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:", placeholder="ဥပမာ - Titanic")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        with st.spinner(f'AI က {duration} အတွက် ဇာတ်လမ်းကို စဉ်းစားနေပါတယ်...'):
            try:
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # Prompt ထဲမှာ duration ကို ထည့်သွင်းခိုင်းခြင်း
                prompt = f"""
                မင်းက Professional Movie Recapper တစ်ယောက်ပါ။ 
                ဇာတ်ကားနာမည် - {movie_name}
                ဗီဒီယိုကြာချိန် - {duration} ခန့်အတွက် Narrator Script ရေးပေးပါ။
                
                အောက်ပါအချက်များ ပါဝင်ပါစေ-
                ၁။ {duration} နဲ့ ကိုက်ညီအောင် စာလုံးရေကို ချိန်ညှိပေးပါ။ (၃ မိနစ်ဆိုလျှင် စာလုံးရေ ၅၀၀ ခန့်၊ ၁၀ မိနစ်ဆိုလျှင် ၁၅၀၀ ခန့်)
                ၂။ Narrator တစ်ယောက် ပြောပြနေတဲ့ ပုံစံမျိုး ဖြစ်ရမည်။
                ၃။ ဆွဲဆောင်မှုရှိသော Intro၊ အဓိကဇာတ်ကွက်များ၊ Plot Twists နှင့် သင်ခန်းစာ နိဂုံး ပါဝင်ရမည်။
                ၄။ မြန်မာလို သဘာဝကျကျ ရေးသားပေးပါ။
                """
                
                response = model.generate_content(prompt)
                st.success(f"'{movie_name}' အတွက် {duration} Script ရပါပြီ")
                st.markdown(response.text)
                
            except Exception as e:
                if "429" in str(e):
                    st.error("Error: ခဏအတွင်း မေးခွန်းအမေးများသွားလို့ပါ။ ၁ မိနစ်လောက်စောင့်ပေးပါ။")
                else:
                    st.error(f"Error: {e}")
