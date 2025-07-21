import streamlit as st
import requests

st.title("📊 Student Result Predictor")

math = st.number_input("Math Marks", min_value=0, max_value=100)
science = st.number_input("Science Marks", min_value=0, max_value=100)
english = st.number_input("English Marks", min_value=0, max_value=100)

if st.button("Predict"):
    # Call your FastAPI endpoint
    response = requests.post("https://predictmodel-xn8hcbq5xajxuw6acxes9m.streamlit.app/predict", json={
        "Math": math,
        "Science": science,
        "English": english
    })
    st.write("Status code:", response.status_code)
    st.write("Raw response text:", response.text)
    result=response.json()
    st.write(result)
    # if response.status_code == 200:
    #     result = response.json()
    #     st.success(f"🎯 Prediction: {result['prediction']} (Code: {result['code']})")
    # else:
    #     st.error("❌ Failed to get prediction. Check API server.")
