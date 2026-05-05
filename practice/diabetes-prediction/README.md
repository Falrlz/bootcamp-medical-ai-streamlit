# Diabetes Prediction (Streamlit App)

A machine learning-based web application to predict diabetes using the Pima Indians Diabetes Dataset and a trained Decision Tree model.

## Overview

This application performs real-time diabetes prediction based on patient medical data.  
The system uses a trained machine learning model with a preprocessing pipeline to ensure consistent predictions.

## Preview

![Diabetes App Preview](../../assets/diabetes-preview.gif)

## Machine Learning Pipeline

Input Data → Feature Scaling → Model Prediction → Probability Output

## Input Features

The model requires the following patient data:

- Pregnancies → Number of pregnancies  
- Glucose → Plasma glucose concentration (mg/dL)  
- BloodPressure → Diastolic blood pressure (mm Hg)  
- SkinThickness → Triceps skin fold thickness (mm)  
- Insulin → Serum insulin (mu U/mL)  
- BMI → Body Mass Index  
- DiabetesPedigreeFunction → Family history of diabetes  
- Age → Patient age (years)  

## Model & Preprocessing

- Model: Decision Tree Classifier  
- Preprocessing: StandardScaler  
- Model Artifact: `models/decision_tree_model.joblib`  
- Scaler Artifact: `models/scaler.joblib`  

⚠️ Important:
- Scaling must be applied before prediction  
- Model and scaler must match the training pipeline  

## Evaluation Metrics

- Accuracy  
- Recall (Sensitivity)  
- ROC-AUC  
- Classification Report (Precision, Recall, F1-Score)  
- Confusion Matrix  
- ROC Curve Visualization  

## Output

- Binary classification:
  - **Diabetes**
  - **Non-Diabetes**
- Prediction probability (confidence score)

## Application Flow

1. User inputs patient data  
2. Data is converted into numerical array  
3. Feature scaling is applied using trained scaler  
4. Model performs prediction  
5. Output is displayed:
   - Prediction result
   - Probability score  

## Project Structure

```
diabetes-prediction/
│
├── data/
│ └── diabetes.csv
│
├── models/
│ ├── decision_tree_model.joblib
│ └── scaler.joblib
│
├── notebook/
│ └── diabetes_prediction_decision_tree.ipynb
│
├── app.py
└── requirements.txt
```

## Technologies Used

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Scikit-learn  
- Imbalanced-learn (SMOTE)  
- Streamlit  
- Joblib  

## How to Run

1. Create Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**MacOS / Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run APP
```bash
streamlit run app.py
```