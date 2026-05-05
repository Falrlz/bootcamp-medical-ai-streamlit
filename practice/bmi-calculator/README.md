# BMI Calculator (Streamlit App)

A web-based application to calculate Body Mass Index (BMI) and classify health status based on WHO standards.

## Overview

This application enables users to calculate their BMI by entering height and weight. It also provides an automatic classification and personalized feedback based on the BMI result.

The system is built with a clean separation between logic and interface, including input validation and dynamic UI feedback.

## Preview

![BMI App Preview](../../assets/bmi-preview.gif)

## Features

- User input:
  - Name
  - Height (cm)
  - Weight (kg)
- Automatic BMI calculation
- BMI classification based on WHO standard:
  - Underweight
  - Normal
  - Overweight
  - Obese
- Dynamic feedback based on BMI category
- Input validation (empty name, invalid values)
- Clean UI with responsive layout (Streamlit columns)

## Formula

BMI = Weight (kg) / [Height (m)]<sup>2</sup>

**Where:**
- **Weight (kg)** = body weight in kilograms  
- **Height (m)** = body height in meters  

## BMI Classification (WHO Standard)

| BMI Range        | Category     |
|------------------|--------------|
| < 18.5           | Underweight  |
| 18.5 – 24.9      | Normal       |
| 25.0 – 29.9      | Overweight   |
| ≥ 30.0           | Obese        |

## Application Flow

1. User inputs name, height, and weight  
2. Input validation is performed  
3. BMI is calculated using the formula  
4. BMI category is determined  
5. Result is displayed with:
   - BMI value
   - Category
   - Personalized feedback  

## Code Structure

- `hitung_bmi()` → BMI calculation logic  
- `kategori_bmi()` → BMI classification logic  
- Streamlit UI → input handling, validation, and output display  

## Technologies Used

- Python
- Streamlit

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