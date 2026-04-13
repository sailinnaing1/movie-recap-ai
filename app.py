import streamlit as st
import google.generativeai as genai

# ဒီနေရာမှာ သင့်ရဲ့ Gemini API Key ကို ထည့်ပါ
genai.configure(api_key="AIzaSyCRKebkyppnc0Cq3CTYp_EiR9FbXxYGaHw ")

st.title("🎬 Movie Recap AI")
st.write("ဇာတ်ကားနာမည် ရိုက်ထည့်ပြီး မြန်မာလို Recap ရေးခိုင်းပါ။")

movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ပါ:")

if st.button("Recap ရေးခိုင်းမယ်"):
    if movie_name:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"{movie_name} movie recap in Burmese language")
        st.subheader("ဇာတ်လမ်းအညွှန်း")
        st.write(response.text)
    else:
        st.warning("ကျေးဇူးပြု၍ ဇာတ်ကားနာမည် အရင်ရိုက်ပေးပါ။")
      
