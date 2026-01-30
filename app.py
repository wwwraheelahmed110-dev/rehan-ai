import streamlit as st
import google.generativeai as genai

# Yahan apni NAYI API KEY dhyan se paste karein
API_KEY = "AIzaSyADdxPEwvarm4xeNnaCDkl0q2KQo2HsM-Q"

genai.configure(api_key=API_KEY)

# Humne yahan 'gemini-pro' use kiya hai jo sab se stable hai
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Rehan AI", page_icon="🤖")

st.title("🤖 Rehan Raheel Hydir AI")
st.markdown("---")
st.write("Assalam-o-Alaikum! Main Rehan ka banaya hua AI hoon. Mujhse kuch bhi poochein.")

user_input = st.text_input("Aapka Sawal:", placeholder="Maslan: Pakistan kab azad hua?")

if st.button("Jawab Do"):
    if user_input:
        try:
            with st.spinner('AI soch raha hai...'):
                response = model.generate_content(user_input)
                st.success("### AI ka Jawab:")
                st.write(response.text)
        except Exception as e:
            st.error("Model ka masla hai. Please check karein ke API Key sahi hai.")
    else:
        st.warning("Pehle kuch sawal toh likhein!")
