import streamlit as st
import requests

st.set_page_config(page_title="PG Rent Predictor", layout="centered")
st.title("🏠 PG Rent Predictor")

with st.form("rent_form"):
    city = st.text_input("City", "nagpur")
    area = st.text_input("Area", "manewada")
    location = st.text_input("Location", "manewada, nagpur")
    zone = st.selectbox("Zone", ["north", "south", "east", "west", "central"])
    shearing = st.selectbox("Shearing", ["private", "double", "triple", "shared"])
    best_suit_for = st.selectbox("Best Suited For", ["students", "working", "students and working"])
    meals_avilable = st.selectbox("Meals Available", ["yes", "no"])
    notic_period = st.text_input("Notice Period", "15 days")
    lock_in_period = st.text_input("Lock-in Period", "30 days")
    amenities_count = st.slider("Amenities Count", 0, 15, 3)
    in_time_at_night = st.text_input("In-Time at Night", "10 PM")
    non_veg_allowed = st.selectbox("Non-Veg Allowed", ["yes", "no"])
    opposite_gender_allowed = st.selectbox("Opposite Gender Allowed", ["yes", "no"])
    visitors_allowed = st.selectbox("Visitors Allowed", ["yes", "no"])
    gurdian_allowed = st.selectbox("Guardian Allowed", ["yes", "no"])
    drinking_allowed = st.selectbox("Drinking Allowed", ["yes", "no"])
    smoking_allowed = st.selectbox("Smoking Allowed", ["yes", "no"])

    submitted = st.form_submit_button("Predict Rent")

    if submitted:
        payload = {
            "city": city,
            "area": area,
            "location": location,
            "zone": zone,
            "shearing": shearing,
            "best_suit_for": best_suit_for,
            "meals_avilable": meals_avilable,
            "notic_period": notic_period,
            "lock_in_period": lock_in_period,
            "amenities_count": amenities_count,
            "in_time_at_night": in_time_at_night,
            "non_veg_allowed": non_veg_allowed,
            "opposite_gender_allowed": opposite_gender_allowed,
            "visitors_allowed": visitors_allowed,
            "gurdian_allowed": gurdian_allowed,
            "drinking_allowed": drinking_allowed,
            "smoking_allowed": smoking_allowed
        }

        try:
            # 🔁 Replace with your deployed FastAPI URL
            response = requests.post("https://pg-rent-api.onrender.com/predict", json=payload)
            if response.status_code == 200:
                result = response.json()
                st.success(f"✅ Predicted Rent: ₹{result['predicted_rent']}")
            else:
                st.error("❌ API error. Please check the backend.")
        except Exception as e:
            st.error(f"⚠️ Connection error: {e}")
