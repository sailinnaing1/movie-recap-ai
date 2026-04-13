import streamlit as st
import google.generativeai as genai

# Secrets ထဲက Key ကို ယူခြင်း
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key မတွေ့ပါ။")
    st.stop()

st.title("🎬 Movie Recap AI")
movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        with st.spinner('ခဏစောင့်ပါ...'):
            try:
                # ဤနေရာတွင် gemini-1.5-flash ဟုသာ ရေးပါ
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Write a movie recap for {movie_name} in Burmese.")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
                
