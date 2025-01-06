import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset
data = pd.read_csv('Household energy bill data.csv')

# Split into features and target
X = data.drop(columns=['amount_paid'])
y = data['amount_paid']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
with open('random_forest_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as random_forest_model.pkl")
