import streamlit as st
import pandas as pd
import joblib

model = joblib.load("salary_model.pkl")

st.title("Employee Salary Prediction")
st.write("Enter employee details to estimate salary.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
education = st.selectbox(
    "Education Level",
    ["Bachelor's", "Master's", "PhD", "High School"]
)
job_title = st.text_input("Job Title", value="Software Engineer")
experience = st.number_input(
    "Years of Experience", min_value=0.0, max_value=50.0, value=5.0
)

if st.button("Predict Salary"):
    employee = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Education Level": education,
        "Job Title": job_title,
        "Years of Experience": experience
    }])

    prediction = model.predict(employee)[0]
    st.success(f"Estimated Salary: {prediction:,.2f}")
    st.caption("This is a model estimate, not a guaranteed salary.")
