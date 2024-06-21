import streamlit as st
import requests
import json

# Title of the app
st.title("API Request App")

# Input fields for the three features
feature1 = st.number_input("Enter feature 1", value=0.0)
feature2 = st.number_input("Enter feature 2", value=0.0)
feature3 = st.number_input("Enter feature 3", value=0.0)

# Submit button
if st.button("Submit"):
    # Create the payload
    payload = {
        "feature1": feature1,
        "feature2": feature2,
        "feature3": feature3
    }

    # Send the POST request
    response = requests.post("http://localhost:8080/predict", json=payload)

    # Print the response
    st.write(f"The prediction is {response.json()["prediction"]}")


# In the terminal just run streamlit run app.py --server.port 4000  and it will run this on port 4000
