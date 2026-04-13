import streamlit as st
import google.generativeai as genai

# API Key ကို ဒီမှာ ထည့်ပါ
genai.configure(api_key="AIzaSyCRKebkyppnc0Cq3CTYp_EiR9FbXxYGaHw")

st.set_page_config(page_title="Movie Recap AI", page_icon="🎬")
st.title("🎬 Movie Recap AI")

movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:", placeholder="ဥပမာ - Titanic")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        with st.spinner('AI က စဉ်းစားနေပါတယ်...'):
            try:
                # Model နာမည်ကို 'gemini-pro' ဟု ပြောင်းသုံးကြည့်ပါ
                # တကယ်လို့ flash သုံးချင်ရင် 'models/gemini-1.5-flash-latest' ဟု ရေးပါ
                model = genai.GenerativeModel('gemini-pro')
                
                prompt = f"Please write a detailed movie recap for '{movie_name}' in Burmese language."
                response = model.generate_content(prompt)
                
                st.success(f"'{movie_name}' အတွက် ရလာဒ် ရပါပြီ")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("ကျေးဇူးပြု၍ ဇာတ်ကားနာမည် အရင်ရိုက်ပေးပါ။")
        
