import streamlit as st
import pandas as pd
import pickle
import base64

# Load the trained model
model = pickle.load(open('random_forest_model.pkl', 'rb'))

# Create a title for the app
#st.title('Employee Attrition Prediction App')

import streamlit as st

import streamlit as st

# Use HTML to change the title's color, size, and height
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

    # Numerical input fields
    age = st.sidebar.slider('Age', 18, 60, 30)
    daily_rate = st.sidebar.number_input('Daily Rate', min_value=0)
    distance_from_home = st.sidebar.number_input('Distance From Home', min_value=0)
    employee_count = st.sidebar.number_input('Employee Count', min_value=1, max_value=1000)
    employee_number = st.sidebar.number_input('Employee Number', min_value=1)
    environment_satisfaction = st.sidebar.slider('Environment Satisfaction', 1, 4, 3)
    hourly_rate = st.sidebar.number_input('Hourly Rate', min_value=0)
    job_involvement = st.sidebar.slider('Job Involvement', 1, 4, 3)
    job_level = st.sidebar.selectbox('Job Level', [1, 2, 3, 4, 5])
    job_satisfaction = st.sidebar.slider('Job Satisfaction', 1, 4, 3)
    monthly_income = st.sidebar.number_input('Monthly Income', min_value=0)
    monthly_rate = st.sidebar.number_input('Monthly Rate', min_value=0)
    num_companies_worked = st.sidebar.number_input('Number of Companies Worked', min_value=0)
    percent_salary_hike = st.sidebar.number_input('Percent Salary Hike', min_value=0, max_value=100)
    performance_rating = st.sidebar.slider('Performance Rating', 1, 4, 3)
    relationship_satisfaction = st.sidebar.slider('Relationship Satisfaction', 1, 4, 3)
    standard_hours = st.sidebar.number_input('Standard Hours', min_value=0)
    stock_option_level = st.sidebar.selectbox('Stock Option Level', [0, 1, 2, 3])
    total_working_years = st.sidebar.number_input('Total Working Years', min_value=0)
    training_times_last_year = st.sidebar.number_input('Training Times Last Year', min_value=0)
    work_life_balance = st.sidebar.slider('Work Life Balance', 1, 4, 3)
    years_at_company = st.sidebar.number_input('Years At Company', min_value=0)
    years_in_current_role = st.sidebar.number_input('Years In Current Role', min_value=0)
    years_since_last_promotion = st.sidebar.number_input('Years Since Last Promotion', min_value=0)
    years_with_curr_manager = st.sidebar.number_input('Years With Current Manager', min_value=0)

    # Categorical input fields
    business_travel = st.sidebar.selectbox('Business Travel', ['Non-Travel', 'Travel_Frequently', 'Travel_Rarely'])
    department = st.sidebar.selectbox('Department', ['Sales', 'Research & Development', 'Human Resources'])
    education = st.sidebar.selectbox('Education', ['Below College', 'College', 'Bachelor', 'Master', 'Doctor'])
    education_field = st.sidebar.selectbox('Education Field', ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other'])
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    marital_status = st.sidebar.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
    over18 = st.sidebar.selectbox('Over 18', ['Yes', 'No'])
    overtime = st.sidebar.selectbox('Overtime', ['Yes', 'No'])

    # Create a button to make predictions
    if st.sidebar.button('Predict Attrition'):
        # Create a DataFrame with the user input
        input_data = pd.DataFrame({
            'Age': [age],
            'DailyRate': [daily_rate],
            'DistanceFromHome': [distance_from_home],
            'EmployeeCount': [employee_count],
            'EmployeeNumber': [employee_number],
            'EnvironmentSatisfaction': [environment_satisfaction],
            'HourlyRate': [hourly_rate],
            'JobInvolvement': [job_involvement],
            'JobLevel': [job_level],
            'JobSatisfaction': [job_satisfaction],
            'MonthlyIncome': [monthly_income],
            'MonthlyRate': [monthly_rate],
            'NumCompaniesWorked': [num_companies_worked],
            'PercentSalaryHike': [percent_salary_hike],
            'PerformanceRating': [performance_rating],
            'RelationshipSatisfaction': [relationship_satisfaction],
            'StandardHours': [standard_hours],
            'StockOptionLevel': [stock_option_level],
            'TotalWorkingYears': [total_working_years],
            'TrainingTimesLastYear': [training_times_last_year],
            'WorkLifeBalance': [work_life_balance],
            'YearsAtCompany': [years_at_company],
            'YearsInCurrentRole': [years_in_current_role],
            'YearsSinceLastPromotion': [years_since_last_promotion],
            'YearsWithCurrManager': [years_with_curr_manager],
            'Gender': [gender],
            'MaritalStatus': [marital_status],
            'Over18': [over18],
            'OverTime': [overtime],
            'BusinessTravel': [business_travel],
            'Department': [department],
            'EducationField': [education_field],
        })

        # One-hot encoding for categorical variables
        input_data = pd.get_dummies(input_data, columns=['BusinessTravel', 'Department', 'EducationField'], drop_first=True)

        # Encoding binary categorical variables
        input_data['Gender'] = input_data['Gender'].map({'Male': 1, 'Female': 0})
        input_data['MaritalStatus'] = input_data['MaritalStatus'].map({'Single': 0, 'Married': 1, 'Divorced': 2})
        input_data['Over18'] = input_data['Over18'].map({'Yes': 1, 'No': 0})
        input_data['OverTime'] = input_data['OverTime'].map({'Yes': 1, 'No': 0})

        # Get the feature names from the model
        model_feature_names = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else model.get_feature_names_out()

        # Add missing columns based on the model's expected features
        for feature in model_feature_names:
            if feature not in input_data.columns:
                input_data[feature] = 0
        input_data = input_data[model_feature_names]

        # Make a prediction using the loaded model
        prediction = model.predict(input_data)[0]

        # Display the prediction
        if prediction == 1:
            st.error('The model predicts that the employee is likely to leave.')
        else:
            st.success('The model predicts that the employee is likely to stay.')




# CSV Upload option
elif option == 'Upload CSV':
    uploaded_file = st.sidebar.file_uploader('Upload your CSV file', type=['csv'])

    if uploaded_file is not None:
        # Load the CSV file
        input_data = pd.read_csv(uploaded_file)

        # One-hot encoding for categorical variables
        input_data = pd.get_dummies(input_data, columns=['BusinessTravel', 'Department', 'EducationField'], drop_first=True)

        # Encoding binary categorical variables
        input_data['Gender'] = input_data['Gender'].map({'Male': 1, 'Female': 0})
        input_data['MaritalStatus'] = input_data['MaritalStatus'].map({'Single': 0, 'Married': 1, 'Divorced': 2})
        input_data['Over18'] = input_data['Over18'].map({'Yes': 1, 'No': 0})
        input_data['OverTime'] = input_data['OverTime'].map({'Yes': 1, 'No': 0})

        # Get the feature names from the model
        model_feature_names = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else model.get_feature_names_out()

        # Add missing columns based on the model's expected features
        for feature in model_feature_names:
            if feature not in input_data.columns:
                input_data[feature] = 0
        input_data = input_data[model_feature_names]

        # Make predictions for each row in the CSV
        predictions = model.predict(input_data)

        # Display predictions
        input_data['Attrition Prediction'] = predictions
        st.write(input_data)

        # Option to download results as CSV
        st.download_button(label="Download Predictions", data=input_data.to_csv(index=False), file_name="predictions.csv")
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
            color: white;  /* Change text color to ensure visibility */
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

# Set the local background image
set_background("exit.png")