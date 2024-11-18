import streamlit as st
import pandas as pd
import pickle


# Load the pre-trained model
with open('eq1_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the dataset extracted from the whole set
df = pd.read_csv("test.csv")

df=df[[
    'OrgId', 'IncidentId', 'DetectorId', 'AlertId', 'AlertTitle',
    'Category','IncidentGrade']]

def encode(df):

    from sklearn.preprocessing import LabelEncoder
    # Label Encoding
    label_encoder = LabelEncoder()

    for i in df.columns:
        df[i]=label_encoder.fit_transform(df[i])
    return df

# App configuration
st.title("Incident Classification")

# Collecting user inputs with dropdowns
OrgId = st.selectbox("Organization Id", sorted(df['OrgId'].unique()))
IncidentId = st.selectbox("Incident Id", sorted(df['IncidentId'].unique()))
DetectorId = st.selectbox("Detector Id", sorted(df['DetectorId'].unique()))
AlertId = st.selectbox("Alert Id", sorted(df['AlertId'].unique()))
AlertTitle = st.selectbox("Alert Title", sorted(df['AlertTitle'].unique()))
Category = st.selectbox("Category", sorted(df['Category'].unique()))

# Prepare the input DataFrame for prediction
user_input = pd.DataFrame(
    [[OrgId, IncidentId, DetectorId, AlertId, AlertTitle, Category]],
    columns=['OrgId', 'IncidentId', 'DetectorId', 'AlertId', 'AlertTitle', 'Category']
)

user_input = encode(user_input) # function calling


# Prediction
if st.button("Predict"):
    try:
        Incident = model.predict(user_input)[0]  # Predict incident grade
        st.success(f'Predicted Incident Grade: {Incident}')
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
