from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('heart_disease_prediction_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    data = request.form
    features = [
        float(data['age']),
        float(data['sex']),
        float(data['cp']),
        float(data['trestbps']),
        float(data['chol']),
        float(data['fbs']),
        float(data['restecg']),
        float(data['thalach']),
        float(data['exang']),
        float(data['oldpeak']),
        float(data['slope']),
        float(data['ca']),
        float(data['thal'])
    ]

    # Make prediction
    prediction = model.predict([features])[0]

    # Return the result
    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
# This code is a Flask web application that serves a machine learning model for heart disease prediction.
# It loads a pre-trained model from a pickle file and uses it to make predictions based on user input from a web form.
# The application has two routes: the home route that renders the input form and the predict route that handles the prediction logic.
# The prediction result is then displayed back on the web page.     