
import streamlit as st
import pandas as pd
import pickle
import base64

# Load the trained model
model = pickle.load(open('random_forest_model.pkl', 'rb'))

# Create a title for the app
st.markdown(
    """
    <h1 style='color:#333333; font-size:20px; line-height: 0.5; text-align: center;'>
        Employee Attrition Prediction App
    </h1>
    """,
    unsafe_allow_html=True
)

# Sidebar options
option = st.sidebar.selectbox('Choose input method:', ['Manual Input', 'Upload CSV'])

# Manual input option
if option == 'Manual Input':
    st.sidebar.header('Employee Information')
    # Add the input fields here (e.g., sliders, number inputs, etc.)

    # Create a button to make predictions
    if st.sidebar.button('Predict Attrition'):
        # Collect inputs, process them, and make predictions using the model
        pass

# CSV Upload option
elif option == 'Upload CSV':
    uploaded_file = st.sidebar.file_uploader('Upload your CSV file', type=['csv'])

    if uploaded_file is not None:
        # Process and predict for the CSV data
        pass

# Function to load the local image as a background
def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode()
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            color: white;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

# Set the local background image
set_background("exit.png")
