from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

with open("xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("threshold.pkl", "rb") as f:
    threshold = pickle.load(f)


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
def health():
    return {"status": "API is running"}


@app.post("/predict")
def predict(data: ChurnInput):
    df = pd.DataFrame([data.dict()])
    encoded = encoder.transform(df)
    prob = model.predict_proba(encoded)[0][1]
    pred = int(prob >= threshold)

    return {
        "churn_prediction": pred,
        "churn_probability": round(float(prob), 3),
        "threshold_used": float(threshold)
    }
