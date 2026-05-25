# Pharmacy ML Models

Machine learning models developed for clinical research at a pharmacy department. Three independent datasets, each analysed separately using Logistic Regression with appropriate handling for class imbalance.

## Repository Structure

```
pharmacy-ml-model/
├── model1/   — ADR Prediction (Antiplatelet/Anticoagulant cohort A)
├── model2/   — ADR Prediction (Antiplatelet/Anticoagulant cohort B)
└── model3/   — Drug-Drug Interaction (DDI) Detection
```

## Task Overview

| Model | Task | Algorithm | Dataset Size |
|-------|------|-----------|--------------|
| Model 1 | Adverse Drug Reaction — Binary Classification | Logistic Regression | ~272 patients |
| Model 2 | Adverse Drug Reaction — Binary Classification | Logistic Regression | ~269 patients |
| Model 3 | Drug-Drug Interaction Detection | Logistic Regression | ~280 patients |

## Methodology

All models follow the same pipeline:
- Data cleaning and feature engineering from raw clinical records
- Binary encoding of categorical features
- StandardScaler normalisation
- Logistic Regression with `class_weight='balanced'` to handle class imbalance
- 80/20 stratified train/test split
- Evaluation: Confusion Matrix, ROC-AUC, Precision, Recall, F1, Odds Ratios

## Important Note on Dataset Size

Clinical datasets with low event rates (ADR present in ~8-9% of cases) present inherent evaluation challenges. Metrics are reported transparently with appropriate limitations documented per model. The Odds Ratio analysis is highlighted as the primary clinically actionable output in such cases.

## Privacy

Raw datasets are not included in this repository. All patient records are excluded via `.gitignore`. Only notebooks and output visualisations are committed.