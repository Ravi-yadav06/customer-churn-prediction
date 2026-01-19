📊 Customer Churn Prediction System

A Machine Learning project to predict whether a customer is likely to churn (leave the service) based on historical customer data. The system helps businesses identify at-risk customers and take preventive actions.

🚀 Project Overview

Customer churn is a critical business problem. Retaining existing customers is cheaper than acquiring new ones. This project builds a classification model that predicts churn using customer behavioral and demographic data.

🛠 Tech Stack

Python

Pandas & NumPy – Data preprocessing

Scikit-learn – Model training and evaluation

Matplotlib / Seaborn – Visualization

FastAPI (optional) – Model deployment

Jupyter Notebook / Google Colab

📁 Project Structure
Customer-Churn/
│
├── churn_model.ipynb
├── dataset.csv
├── model.pkl
├── main.py (optional API)
├── requirements.txt
└── README.md

📌 Problem Statement

Predict whether a customer will:

0 → Not Churn

1 → Churn

Based on features such as:

Customer tenure

Monthly charges

Contract type

Payment method

Internet services

Demographic information

⚙ Data Preprocessing Steps

The following preprocessing steps were applied:

Handling missing values

Encoding categorical variables

Feature selection

Train-test split

Handling class imbalance

Feature scaling (for applicable models)

🤖 Models Used

The following machine learning models were trained and compared:

Logistic Regression

Decision Tree

Random Forest

AdaBoost

Final model selected based on performance metrics and imbalance handling.

⚖ Handling Imbalanced Dataset

The dataset was imbalanced (more non-churn customers than churn customers). To address this:

Class Weight Balancing was applied

Threshold Tuning was performed

PR-AUC was used as the main evaluation metric

📈 Evaluation Metrics

Due to data imbalance, accuracy alone was not sufficient. The following metrics were used:

Precision

Recall

F1-Score

Confusion Matrix

PR-AUC (Primary Metric)

ROC-AUC (Secondary)

📊 Sample Results

Example evaluation output:

Accuracy: ~78%

PR-AUC: ~0.61

Improved recall after threshold tuning

These results indicate moderate but meaningful performance in identifying churn customers.

🎯 Threshold Tuning

Instead of using default probability threshold (0.5), threshold tuning was applied to:

Improve churn recall

Reduce false negatives

Optimize business impact

This allowed better identification of high-risk customers.

🧠 Key Learnings

Accuracy is misleading for imbalanced datasets

PR-AUC is more reliable than ROC-AUC for churn prediction

Threshold tuning improves minority class detection

Feature engineering impacts model performance significantly

▶ How To Run The Project
1️⃣ Install Dependencies
pip install pandas numpy scikit-learn matplotlib seaborn fastapi uvicorn

2️⃣ Run Notebook

Open:

churn_model.ipynb


in Jupyter Notebook or Google Colab.

3️⃣ (Optional) Run API Server
uvicorn main:app --reload


Open:

http://127.0.0.1:8000/docs

📌 Business Impact

This system can help companies:

Identify customers at risk

Reduce churn rate

Improve customer retention

Increase revenue

🚀 Future Improvements

Hyperparameter tuning

SMOTE oversampling

Deep learning models

Model deployment on cloud

Real-time prediction dashboard

👨‍💻 Author

Ravi
Machine Learning Developer
JECRC University
