from fastapi import FastAPI
from app.schemas import PGRentRequest
import joblib
import pandas as pd
import os

app = FastAPI()

# Load the model
model_path = os.path.join("app", "model", "pg_rent_final_model.pkl")
model = joblib.load(model_path)

@app.get("/")
def read_root():
    return {"message": "PG Rent Prediction API is up!"}

@app.post("/predict")
def predict_rent(data: PGRentRequest):
    # Process shearing and meals interaction
    shearing = data.shearing if data.shearing not in ['four', 'multi'] else 'shared'
    meals_shearing = data.meals_avilable + "_" + shearing

    input_df = pd.DataFrame([{
        "city": data.city,
        "area": data.area,
        "location": data.location,
        "zone": data.zone,
        "shearing": shearing,
        "best_suit_for": data.best_suit_for,
        "meals_avilable": data.meals_avilable,
        "notic_period": data.notic_period,
        "lock_in_period": data.lock_in_period,
        "amenities_count": data.amenities_count,
        "in_time_at_night": data.in_time_at_night,
        "non_veg_allowed": data.non_veg_allowed,
        "opposite_gender_allowed": data.opposite_gender_allowed,
        "visitors_allowed": data.visitors_allowed,
        "gurdian_allowed": data.gurdian_allowed,
        "drinking_allowed": data.drinking_allowed,
        "smoking_allowed": data.smoking_allowed,
        "meals_shearing": meals_shearing
    }])

    prediction = model.predict(input_df)[0]
    return {"predicted_rent": round(prediction, 2)}
