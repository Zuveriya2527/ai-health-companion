# app.py
try:
    import streamlit as st
    from chatbot import health_chatbot
    from diet_fitness import diet_advice
    from mental_health import mental_health_check
    from risk_predictor import health_risk_prediction

    st.set_page_config(page_title="AI Health Companion", layout="wide")

    st.title("🤖 AI Health Companion")
    st.sidebar.title("🔍 Select a Service")

    option = st.sidebar.radio("Go to:", [
        "Symptom Checker",
        "Diet & Fitness Advisor",
        "Mental Wellness Check",
        "Health Risk Predictor",
        "AI Chatbot"
    ])

    if option == "Symptom Checker":
        st.header("🩺 Symptom Checker")
        st.info("Coming Soon: Upload symptoms and get condition predictions.")

    elif option == "Diet & Fitness Advisor":
        diet_advice()

    elif option == "Mental Wellness Check":
        mental_health_check()

    elif option == "Health Risk Predictor":
        health_risk_prediction()

    elif option == "AI Chatbot":
        health_chatbot()

except ModuleNotFoundError as e:
    print("Required module not found:", e)
    print("Please install the missing package using pip.")
