# Diabetes Classifier Web App

## Overview

This is a Streamlit-based web application for classify diabetes in patients. Users can input relevant medical parameters, and the app will classify whether the patient is likely to be infected or not based on a pre-trained machine learning model.

## Features

- User-friendly interface built with Streamlit.
- Takes user input for multiple medical parameters.
- Uses a pre-trained model (`Diabetes_Prediction.pkl`) for prediction.
- Displays corresponding images based on prediction results.

## Installation

To run this application locally, follow these steps:

1. Clone this repository or download the project files.
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate  # On Windows
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure that `Diabetes_Prediction.pkl` is placed in the correct directory.
5. Run the application:
   ```bash
   streamlit run Diployment_code.py
   ```

## Required Inputs

The user needs to input the following parameters:

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI
- Diabetes Pedigree Function
- Age

## Output

- The application predicts whether the patient is **Infected** or **Not Infected**.
- Displays a relevant image based on the prediction result.

## Files

- **Diployment\_code.py**: Contains the Streamlit web application code.
- **Model\_Code.ipynb**: Jupyter notebook file for model training (not detailed here but assumed to contain model training and saving logic).
- **Diabetes\_Prediction.pkl**: Pre-trained model file used for prediction.
- **Relevant images**: Used for visualization of results.
- **requirements.txt**: Contains all necessary dependencies to run the application.

## Notes

- Ensure that the model file and required images are in the correct paths.
- The current script references absolute paths (e.g., `C:\Users\HP\Desktop\Diabetes\...`), which may need modification based on the deployment environment.
- The model should be trained and exported before running the deployment script.

## Future Improvements

- Enhance user experience with a more interactive UI.
- Implement error handling for missing inputs.
- Deploy the application on a cloud platform for public access.

