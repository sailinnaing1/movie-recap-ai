import streamlit as st
import google.generativeai as genai

# API Key ကို သေချာထည့်ပါ
genai.configure(api_key="AIzaSyCRKebkyppnc0Cq3CTYp_EiR9FbXxYGaHw")

st.title("🎬 Movie Recap AI")

movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        try:
            # နာမည်ကို models/gemini-1.5-flash ဟု အပြည့်အစုံ ရေးကြည့်ပါ
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            response = model.generate_content(f"Write a movie recap for {movie_name} in Burmese.")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
            
