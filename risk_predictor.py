# risk_predictor.py
import streamlit as st

def health_risk_prediction():
    st.subheader("🔬 Health Risk Predictor")

    st.write("Answer a few questions to estimate your health risk:")

    age = st.slider("Age", 10, 100, 30)
    bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=60.0, value=22.0)
    smoker = st.radio("Do you smoke?", ["Yes", "No"])
    activity = st.selectbox("Physical Activity Level", ["Low", "Moderate", "High"])
    diet = st.selectbox("How would you describe your diet?", ["Unhealthy", "Moderate", "Healthy"])

    if st.button("Predict My Risk"):
        risk_score = 0

        # Basic rules to estimate risk
        if age > 50:
            risk_score += 2
        elif age > 30:
            risk_score += 1

        if bmi >= 30:
            risk_score += 2
        elif bmi >= 25:
            risk_score += 1

        if smoker == "Yes":
            risk_score += 2

        if activity == "Low":
            risk_score += 2
        elif activity == "Moderate":
            risk_score += 1

        if diet == "Unhealthy":
            risk_score += 2
        elif diet == "Moderate":
            risk_score += 1

        st.markdown("### 🧾 Health Risk Score: **{}/10**".format(risk_score))

        if risk_score <= 3:
            st.success("🟢 Low risk. Keep up your healthy lifestyle!")
        elif risk_score <= 6:
            st.warning("🟡 Moderate risk. Consider lifestyle improvements.")
        else:
            st.error("🔴 High risk. Please consult a healthcare professional.")
