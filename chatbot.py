# chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "fever" in user_input:
        return "Common symptoms of fever include high body temperature, chills, sweating, headache, and body aches."

    elif "cold" in user_input:
        return "Symptoms of a cold often include sneezing, runny nose, sore throat, and mild cough."

    elif "covid" in user_input or "corona" in user_input:
        return "COVID-19 symptoms may include fever, dry cough, tiredness, and loss of taste or smell."

    elif "headache" in user_input:
        return "A headache may be caused by stress, dehydration, or illness. Rest and proper hydration can help."

    elif "diet" in user_input:
        return "A balanced diet should include vegetables, fruits, whole grains, lean protein, and plenty of water."

    elif "exercise" in user_input or "fitness" in user_input:
        return "Regular physical activity like walking, jogging, or yoga can help maintain good health and fitness."

    elif "mental health" in user_input:
        return "Mental health is vital. Practices like mindfulness, talking to friends, and seeking help when needed are beneficial."

    else:
        return "I'm sorry, I couldn't find an answer. Please ask about common health topics like fever, diet, or exercise."


# 🧠 Add this for Streamlit chatbot UI
import streamlit as st

def health_chatbot():
    st.subheader("💬 Ask the Health Chatbot")
    user_input = st.text_input("You:")
    if user_input:
        response = chatbot_response(user_input)
        st.write(f"**AI:** {response}")


