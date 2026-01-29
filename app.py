import streamlit as st
import google.generativeai as genai

# Aapka Naam aur Title
st.set_page_config(page_title="Rehan Raheel Hydir AI", page_icon="🤖")
st.title("🤖 Rehan Raheel Hydir AI")
st.markdown("---")
st.write("Assalam-o-Alaikum! Main Rehan ka banaya hua AI hoon. Mujhse kuch bhi poochein.")

# API Key - Isse error nahi aayega
API_KEY = "AIzaSyCLUCNYz3fI7Dnk-cMb7LisdXLVZL-9Vco"
genai.configure(api_key=API_KEY)

# Chatting ka dabba
user_input = st.text_input("Aapka Sawal:", placeholder="Yahan likhein...")

if st.button("Jawab Do"):
    if user_input:
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(user_input)
            st.success("Rehan AI ka Jawab:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Ek choti si galti hui hai: {e}")
    else:
        st.warning("Pehle kuch likhen toh sahi!")
