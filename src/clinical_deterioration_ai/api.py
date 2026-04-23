from fastapi import FastAPI
from clinical_deterioration_ai.predictor import predict_risk

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Clinical Deterioration AI API"}

@app.get("/predict/{score}")
def predict(score: float):
    return {"risk": predict_risk(score)}