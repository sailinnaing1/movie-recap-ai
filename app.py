import streamlit as st
import google.generativeai as genai

# Secrets ထဲက API Key ကို ယူခြင်း
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
                # သင့် API Key နှင့် အလုပ်လုပ်သော Model အသစ်ကို ပြောင်းသုံးပါ
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                prompt = f"Write a comprehensive movie recap of '{movie_name}' in Burmese language."
                response = model.generate_content(prompt)
                
                st.success(f"'{movie_name}' အတွက် ရလဒ် ရပါပြီ")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
                
