# predict.py

import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Sample patient input
sample_data = pd.DataFrame([{
    "AGE_CLEAN": 40,
    "GENDER_BINARY": 1,
    "NUM_DRUGS": 15,
    "HAS_CARDIAC_DX": 0,
    "HAS_ASPIRIN": 1,
    "HAS_CLOPIDOGREL": 1,
    "HAS_HEPARIN": 0,
    "HAS_ECOSPRIN": 0
}])

# IMPORTANT:
# Feature order must exactly match training

sample_data = sample_data[[
    'AGE_CLEAN',
    'GENDER_BINARY',
    'NUM_DRUGS',
    'HAS_CARDIAC_DX',
    'HAS_ASPIRIN',
    'HAS_CLOPIDOGREL',
    'HAS_HEPARIN',
    'HAS_ECOSPRIN'
]]

# Predict
prediction = model.predict(sample_data.values)[0]

# Predict probability
probability = model.predict_proba(sample_data.values)[0][1]

# Output
print("\n=== Prediction Result ===")

if prediction == 1:
    print("Predicted Outcome: ADR PRESENT")
else:
    print("Predicted Outcome: ADR ABSENT")

print(f"Risk Probability: {probability:.2f}")