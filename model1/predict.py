# predict.py

import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Example patient data
# Replace values as needed

sample_data = pd.DataFrame([{
    "AGE_CLEAN": 65,
    "GENDER_BINARY": 1,
    "HAS_COMORBIDITY": 1,
    "HAS_ASPIRIN": 1,
    "HAS_CLOPIDOGREL": 1,
    "HAS_TICAGRELOR": 0,
    "HAS_ANTICOAG": 1,
    "HAS_CARDIAC_DX": 1
}])

# Predict
prediction = model.predict(sample_data)[0]

# Predict probability
probability = model.predict_proba(sample_data)[0][1]

# Output
print("\n=== Prediction Result ===")

if prediction == 1:
    print("Predicted Outcome: ADR PRESENT")
else:
    print("Predicted Outcome: ADR ABSENT")

print(f"Risk Probability: {probability:.2f}")