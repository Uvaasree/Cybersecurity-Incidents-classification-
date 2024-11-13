# Cybersecurity-Incidents-classification

## Overview

This project aims to build a machine learning model to predict the triage grade of cybersecurity incidents as **True Positive (TP)**, **Benign Positive (BP)**, or **False Positive (FP)**. By classifying incidents accurately, the model supports Security Operation Centers (SOCs) in prioritizing responses and improving threat management.

## Project Structure

- **Data Preprocessing**: Cleans and prepares data for modeling.
- **Model Training**: Builds and trains models to classify incidents.
- **Model Evaluation**: Tests the model's accuracy on a test dataset.

## Model Evaluation Metrics

Key metrics for performance assessment:
- **Macro-F1 Score**: Balances performance across TP, BP, and FP classes.
- **Precision**: Measures accuracy in positive predictions.
- **Recall**: Measures correct identification of true threats.

## Results

The model's performance on test data:

                precision    recall  f1-score   support
BenignPositive       0.75      0.83      0.79   1752940
 FalsePositive       0.60      0.59      0.59    902698
  TruePositive       0.84      0.74      0.79   1492354
  
## Future Enhancements

- Additional feature engineering
- More advanced model tuning and testing techniques

---

This README should provide a quick and clear overview for users to understand the purpose, structure, and essential steps for model building and testing.
