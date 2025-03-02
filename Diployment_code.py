# Import Libraries

import streamlit as st
import pandas as pd
import pickle

# Load Data

file_path = r"C:\Users\HP\Desktop\Diabetes\Diabetes_Prediction.pkl"

data = pickle.load(open(file_path,"rb"))
image_path = r'C:\Users\HP\Desktop\Diabetes\doctor-testing-blood-sugar-for-diabetes.jpg'
st.image(image_path)
st.title('Diabetes Prediction Web App')
st.info('Easy Application For Diabetes Prediction Dieseses')
st.write('This fetures required to check "Infected OR Not Infected"')
st.sidebar.header('Feature Selection')



Pregnancies = st.text_input('Pregnancies')
Glucose = st.text_input('Glucose')
BloodPressure = st.text_input('BloodPressure')
SkinThickness = st.text_input('SkinThickness')
Insulin = st.text_input('Insulin')
BMI = st.text_input('BMI')
DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
Age = st.text_input('Age')

df = pd.DataFrame({
    'Pregnancies':[Pregnancies],
    'Glucose':[Glucose],
    'BloodPressure':[BloodPressure],
    'SkinThickness' : [SkinThickness],
    'Insulin':[Insulin],
    'BMI':[BMI],
    'DiabetesPedigreeFunction':[DiabetesPedigreeFunction],
    'Age':[Age]},index=[0])


con = st.sidebar.button('confirm')

if con:
    result = data.predict(df)
    if result == 0:
        st.sidebar.write(f'{result} , The Patient is Not Infected')
        st.sidebar.image(r'C:\Users\HP\Desktop\Diabetes\healthy-heart.jpg')
    else:
        st.sidebar.write(f'{result} , The Patient is Infected')
        st.sidebar.image(r'C:\Users\HP\Desktop\Diabetes\DiabetesHeartDisease_iStock_82917699_MEDIUM.jpg')
