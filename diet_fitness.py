# diet_fitness.py
import streamlit as st

def diet_advice():
    st.subheader("🥗 Personalized Diet & Fitness Advisor")

    goal = st.selectbox("Choose your goal:", ["Weight Loss", "Muscle Gain", "Maintain Weight"])
    age = st.slider("Your age:", 10, 80, 25)
    activity = st.selectbox("Activity Level:", ["Sedentary", "Moderate", "Active"])

    if st.button("Get Plan"):
        st.markdown("### 📝 Recommended Plan:")

        if goal == "Weight Loss":
            st.write("🔹 Eat high-protein, low-carb meals.")
            st.write("🔹 Walk 30 minutes daily. Try intermittent fasting.")
        elif goal == "Muscle Gain":
            st.write("🔹 High protein intake: chicken, eggs, legumes.")
            st.write("🔹 Weight training 3–5x/week.")
        else:
            st.write("🔹 Balanced macros and hydration.")
            st.write("🔹 Mix cardio and strength 3x/week.")

        st.success("✅ Stay consistent and track progress weekly!")
