# mental_health.py
import streamlit as st

def mental_health_check():
    st.subheader("🧠 Mental Wellness Check")

    st.write("Please answer the following questions honestly:")

    q1 = st.slider("1. Feeling down, depressed, or hopeless?", 0, 3)
    q2 = st.slider("2. Trouble falling or staying asleep?", 0, 3)
    q3 = st.slider("3. Feeling tired or having little energy?", 0, 3)
    q4 = st.slider("4. Poor appetite or overeating?", 0, 3)
    q5 = st.slider("5. Feeling bad about yourself or like a failure?", 0, 3)

    if st.button("Check My Mental Health"):
        score = q1 + q2 + q3 + q4 + q5

        st.markdown(f"### Your Score: {score}/15")

        if score <= 4:
            st.success("🟢 Mild or no signs of concern.")
        elif score <= 9:
            st.warning("🟡 Moderate signs. Consider talking to someone.")
        else:
            st.error("🔴 Severe signs. Please reach out to a professional.")

        st.caption("Disclaimer: This is not a diagnosis. For medical advice, consult a psychologist.")



