from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)
app.secret_key = '9494'

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Save user info and redirect to prediction page
@app.route('/save_user_info', methods=['POST'])
def save_user_info():
    session['name'] = request.form['name']
    session['service_number'] = request.form['service_number']
    return redirect(url_for('index'))

# Input features page
@app.route('/predict_form')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form
        features = [
            int(data['num_rooms']),
            int(data['num_people']),
            float(data['housearea']),
            int(data['is_ac']),
            int(data['is_tv']),
            int(data['is_flat']),
            float(data['ave_monthly_income']),
            int(data['num_children']),
            int(data['is_urban'])
        ]

        # Predict
        features = np.array(features).reshape(1, -1)
        prediction = model.predict(features)[0]

        # Render receipt.html with the prediction and user details
        return render_template('receipt.html', 
                               name=session.get('name', 'N/A'), 
                               service_number=session.get('service_number', 'N/A'), 
                               prediction=round(prediction, 2))

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
