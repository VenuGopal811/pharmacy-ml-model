# predict.py

import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Sample patient data
sample_data = pd.DataFrame([{
    "AGE_CLEAN": 25,
    "GENDER_BINARY": 0,
    "HAS_COMORBIDITY": 0,
    "SEVERITY_ENCODED": 0,
    "IS_PHARMACODYNAMIC": 0,
    "IS_PHARMACOKINETIC": 0,
    "MECH_CYP": 0,
    "MECH_ADDITIVE": 0,
    "MECH_SYNERGISM": 0,
    "MECH_QT": 0
}])

# Ensure correct feature order
sample_data = sample_data[[
    "AGE_CLEAN",
    "GENDER_BINARY",
    "HAS_COMORBIDITY",
    "SEVERITY_ENCODED",
    "IS_PHARMACODYNAMIC",
    "IS_PHARMACOKINETIC",
    "MECH_CYP",
    "MECH_ADDITIVE",
    "MECH_SYNERGISM",
    "MECH_QT"
]]

# Predict
prediction = model.predict(sample_data.values)[0]

# Predict probability
probability = model.predict_proba(sample_data.values)[0][1]

print("\n=== Prediction Probability ===")
print(f"Probability of Drug Interaction: {probability:.6f}")

# Output
print("\n=== Prediction Result ===")

if prediction == 1:
    print("Predicted Outcome: DRUG INTERACTION FOUND")
else:
    print("Predicted Outcome: NO DRUG INTERACTION")

print(f"Risk Probability: {probability:.4f}")