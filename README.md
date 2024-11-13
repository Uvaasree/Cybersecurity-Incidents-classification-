# Cybersecurity-Incident-classification

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

## Model Performance

The model's performance on the test set:

| Class           | Precision | Recall | F1-Score | Support |
|-----------------|-----------|--------|----------|---------|
| **BenignPositive** | 0.75      | 0.83   | 0.79     | 1,752,940 |
| **FalsePositive**  | 0.60      | 0.59   | 0.59     | 902,698   |
| **TruePositive**   | 0.84      | 0.74   | 0.79     | 1,492,354 |

## Future Enhancements

- Additional feature engineering
- More advanced model tuning and testing techniques

---

This README now includes a detailed model performance section to clearly show the evaluation metrics for each class.
