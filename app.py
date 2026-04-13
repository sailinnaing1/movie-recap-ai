import streamlit as st
import google.generativeai as genai

# Streamlit Secrets ထဲကနေ API Key ကို ယူတာဖြစ်လို့ ပိုလုံခြုံပါတယ်
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Secrets ထဲမှာ 'GEMINI_API_KEY' ကို မထည့်ရသေးပါဘူး။")
    st.stop()

st.set_page_config(page_title="Movie Recap AI", page_icon="🎬")
st.title("🎬 Movie Recap AI")
st.write("ဇာတ်ကားနာမည် ရိုက်ထည့်ပြီး မြန်မာလို Recap ရေးခိုင်းပါ။")

movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:", placeholder="ဥပမာ - Titanic")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        with st.spinner('AI က ဇာတ်လမ်းကို စဉ်းစားနေပါတယ်...'):
            try:
                # Model နာမည်ကို အမှားကင်းအောင် models/gemini-1.5-flash ဟု သုံးထားပါသည်
                model = genai.GenerativeModel('models/gemini-1.5-flash')
                
                prompt = f"Please write a comprehensive movie recap of '{movie_name}' in Burmese language. Focus on the main plot, characters, and the ending."
                response = model.generate_content(prompt)
                
                st.success(f"'{movie_name}' အတွက် ဇာတ်လမ်းအညွှန်း ရပါပြီ")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error တက်သွားပါတယ်- {e}")
    else:
        st.warning("ကျေးဇူးပြု၍ ဇာတ်ကားနာမည် အရင်ရိုက်ပေးပါ။")
        
