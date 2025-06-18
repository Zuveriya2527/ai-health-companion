# chatbot.py
import streamlit as st

def health_chatbot():
    st.subheader("💬 Ask the Health Chatbot")

    user_input = st.text_input("You:", "")
    if user_input:
        # Simple mock response (replace with real AI model later)
        st.markdown(f"**AI:** I'm here to help with your health questions about: {user_input}")
