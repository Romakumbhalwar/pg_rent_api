from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from app.schemas import PGInput

app = FastAPI()

model = joblib.load("app/pg_rent_model_full.pkl")

@app.get("/")
def root():
    return {"message": "PG Rent Prediction API is running!"}

@app.post("/predict")
def predict(data: PGInput):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)[0]
    return {"predicted_rent": round(prediction, 2)}
