import streamlit as st
import pandas as pd
import pickle

st.title("Student Performance Prediction")

study_time = st.number_input("Study time (hours)", min_value=0.0)
attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0)

if st.button("Predict"):
    # replace with your real model loading
    prediction = "Pass" if attendance > 60 and study_time > 2 else "Fail"
    st.success(f"Prediction: {prediction}")