from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel

# Initialize FastAPI
app = FastAPI()

# Load saved encoder (ColumnTransformer)
with open("encoder.pkl", "rb") as file:
    encoder = pickle.load(file)

# Load trained XGBoost model
with open("xgboost_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load threshold
with open("threshold.pkl", "rb") as file:
    threshold = pickle.load(file)


# Input Schema
class ChurnInput(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is running"}


@app.post("/predict")
def predict_churn(data: ChurnInput):
    input_df = pd.DataFrame([data.dict()])
    transformed_input = encoder.transform(input_df)
    prob = model.predict_proba(transformed_input)[0][1].item()
    pred = int(prob >= threshold)
    return {
        "churn_prediction": pred,
        "churn_probability": round(prob, 3),
        "threshold_used": float(threshold)  # Also convert threshold if NumPy
    }
