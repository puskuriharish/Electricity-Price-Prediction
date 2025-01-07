# Electricity Price Prediction
This project predicts electricity prices using machine learning models, including Linear Regression, SVM, KNN, and Random Forest. The application features a user-friendly interface built with Flask and a backend for accurate predictions.

# Features
Machine Learning Models: Linear Regression, SVM, KNN, Random Forest
Web Interface: Developed with Flask to input data and display predictions
Interactive Form: Users can input features via an HTML form with 13 fields
# Deployment: Hosted on Render
# Demo
Access the live application here: https://electricity-price-prediction.onrender.com/

Getting Started
Prerequisites

Python 3.x

Flask

scikit-learn

pandas

numpy

Render account (optional, for deployment)

# Project Structure
app.py: Main application logic

templates/: HTML files for the web interface

models/: Machine learning models and preprocessing scripts

requirements.txt: List of dependencies

# Machine Learning Models
Linear Regression

SVM (Support Vector Machine)

KNN (K-Nearest Neighbors)

Random Forest

Results
The performance of the models is evaluated using the following metrics:

## Model Performance Summary  

| Model                    | R² Score   | MAE         | RMSE        |  
|--------------------------|------------|-------------|-------------|  
| **Linear Regression**    | 0.999999   | 0.077733    | 0.097529    |  
| **Support Vector Machine** | 0.243788   | 89.705079   | 112.951964  |  
| **K-Nearest Neighbors**  | 0.779010   | 48.860734   | 61.060169   |  
| **Random Forest**        | 0.844599   | 40.177080   | 51.203449   |  


