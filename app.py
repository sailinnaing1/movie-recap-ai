import streamlit as st
import google.generativeai as genai

# Secrets ထဲက API Key ကို ယူခြင်း
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key မတွေ့ပါ။ Settings > Secrets တွင် အရင်ထည့်ပါ။")
    st.stop()

st.title("🎬 Movie Recap AI")
movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        with st.spinner('AI က ဇာတ်လမ်းကို စဉ်းစားနေပါတယ်...'):
            try:
                # Model နာမည်ကို models/ မပါဘဲ အခုလိုပဲ ရေးကြည့်ပါ
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Write a movie recap for {movie_name} in Burmese.")
                st.write(response.text)
            except Exception as e:
                # Error တက်ရင် ဘယ် Model တွေ သုံးလို့ရလဲဆိုတာ ပြခိုင်းမယ်
                st.error(f"Error: {e}")
                st.write("အသုံးပြုနိုင်သော Model များစာရင်း:")
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        st.write(f"- {m.name}")
                        
