import streamlit as st
import google.generativeai as genai

# ၁။ Secrets ထဲက API Key ကို ယူခြင်း
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
    else:
        st.error("Secrets ထဲမှာ GEMINI_API_KEY ကို မတွေ့ရပါ။ Settings တွင် အရင်ထည့်ပေးပါ။")
        st.stop()
except Exception as e:
    st.error(f"Secrets Error: {e}")
    st.stop()

st.title("🎬 Movie Recap AI")

movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:", placeholder="ဥပမာ - Titanic")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        with st.spinner('AI က စဉ်းစားနေပါတယ်...'):
            try:
                # Model နာမည်ကို အရှင်းဆုံးပုံစံဖြင့် သုံးကြည့်ပါ
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Write a movie recap for {movie_name} in Burmese.")
                
                st.success(f"'{movie_name}' အတွက် ရလဒ် ရပါပြီ")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("API Key အသစ်တစ်ခုဖြင့် ပြန်စမ်းကြည့်ရန် အကြံပြုပါသည်။")
    else:
        st.warning("ဇာတ်ကားနာမည် ရိုက်ပေးပါ။")

