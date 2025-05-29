import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("C:/Users/nishi/OneDrive/文档/GitHub/churn-prediction-project/notebooks/churn_model.pkl")

st.title("📉 Telco Customer Churn Prediction")
st.markdown("Predict whether a customer will churn based on their details.")

# Collect user input
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])
Partner = st.selectbox("Has a Partner?", ["Yes", "No"])
Dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
MonthlyCharges = st.slider("Monthly Charges", 0.0, 150.0, 70.0)
TotalCharges = st.slider("Total Charges", 0.0, 10000.0, 2000.0)

# Encode input
def encode_input():
    def binary(val): return 1 if val == "Yes" else 0
    def gender_encode(val): return 1 if val == "Male" else 0

    data = {
        "gender": gender_encode(gender),
        "SeniorCitizen": binary(SeniorCitizen),
        "Partner": binary(Partner),
        "Dependents": binary(Dependents),
        "tenure": tenure,
        "PhoneService": binary(PhoneService),
        "MultipleLines": ["No", "Yes", "No phone service"].index(MultipleLines),
        "InternetService": ["DSL", "Fiber optic", "No"].index(InternetService),
        "OnlineSecurity": ["Yes", "No", "No internet service"].index(OnlineSecurity),
        "OnlineBackup": ["Yes", "No", "No internet service"].index(OnlineBackup),
        "DeviceProtection": ["Yes", "No", "No internet service"].index(DeviceProtection),
        "TechSupport": ["Yes", "No", "No internet service"].index(TechSupport),
        "StreamingTV": ["Yes", "No", "No internet service"].index(StreamingTV),
        "StreamingMovies": ["Yes", "No", "No internet service"].index(StreamingMovies),
        "Contract": ["Month-to-month", "One year", "Two year"].index(Contract),
        "PaperlessBilling": binary(PaperlessBilling),
        "PaymentMethod": ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"].index(PaymentMethod),
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
    }
    return pd.DataFrame([data])

# Predict
if st.button("Predict Churn"):
    input_df = encode_input()
    prediction = model.predict(input_df)[0]
    result = "🔴 Churn" if prediction == 1 else "🟢 Not Churn"
    st.success(f"Prediction: {result}")
