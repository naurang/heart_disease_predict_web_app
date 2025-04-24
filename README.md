# Heart Disease Prediction Web App

This is a web application for predicting the likelihood of heart disease based on user input. The app uses a machine learning model trained on heart disease data to make predictions.

## Features
- User-friendly web interface built with Flask and Bootstrap.
- Input form for entering medical data.
- Real-time prediction of heart disease likelihood.
- Visualizations and KPIs for better understanding.

## Requirements
To run this application, you need the following dependencies:

- Flask
- scikit-learn==1.3.0
- numpy

Install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/naurang/heart_disease_predict_web_app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd heart_disease_predict_web_app
   ```
3. Run the Flask application:
   ```bash
   python3 deploy.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000/` to access the app.

## Input Fields
The app requires the following inputs:
- **Age:** Enter your age in years.
- **Sex:** Enter 1 for Male and 0 for Female.
- **Chest Pain Type (cp):** 0 = Typical Angina, 1 = Atypical Angina, 2 = Non-Anginal Pain, 3 = Asymptomatic.
- **Resting Blood Pressure (trestbps):** Your resting blood pressure in mm Hg.
- **Cholesterol (chol):** Serum cholesterol in mg/dl.
- **Fasting Blood Sugar (fbs):** 1 = True (Fasting blood sugar > 120 mg/dl), 0 = False.
- **Resting ECG Results (restecg):** 0 = Normal, 1 = Having ST-T wave abnormality, 2 = Showing probable or definite left ventricular hypertrophy.
- **Maximum Heart Rate Achieved (thalach):** Enter the maximum heart rate achieved during exercise.
- **Exercise Induced Angina (exang):** 1 = Yes, 0 = No.
- **ST Depression (oldpeak):** ST depression induced by exercise relative to rest.
- **Slope of Peak Exercise ST Segment (slope):** 0 = Upsloping, 1 = Flat, 2 = Downsloping.
- **Number of Major Vessels (ca):** Number of major vessels (0-3) colored by fluoroscopy.
- **Thalassemia (thal):** 1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect.

## Screenshots
- **Input Form:**
  ![Input Form](screenshots/input_form.png)
- **Prediction Result:**
  ![Prediction Result](screenshots/prediction_result.png)

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
