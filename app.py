import streamlit as st
import google.generativeai as genai

# API Key ကို ဒီနေရာမှာ အတိအကျ ထည့်ပါ
genai.configure(api_key="AIzaSyCRKebkyppnc0Cq3CTYp_EiR9FbXxYGaHw")

st.set_page_config(page_title="Movie Recap AI", page_icon="🎬")
st.title("🎬 Movie Recap AI")
st.write("ဇာတ်ကားနာမည် ရိုက်ထည့်ပြီး မြန်မာလို Recap ရေးခိုင်းပါ။")

movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:", placeholder="ဥပမာ - Titanic")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        with st.spinner('AI က စဉ်းစားနေပါတယ်...'):
            try:
                # Model နာမည်ကို gemini-1.5-flash ဟုသာ သုံးထားသည်
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Please write a detailed movie recap for '{movie_name}' in Burmese language."
                response = model.generate_content(prompt)
                
                st.success(f"'{movie_name}' အတွက် ဇာတ်လမ်းအညွှန်း ရပါပြီ")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error တက်နေပါသည်- {e}")
                st.info("API Key မှန်မမှန် သို့မဟုတ် Model နာမည် မှန်မမှန် ပြန်စစ်ပေးပါ။")
    else:
        st.warning("ကျေးဇူးပြု၍ ဇာတ်ကားနာမည် အရင်ရိုက်ပေးပါ။")
        
