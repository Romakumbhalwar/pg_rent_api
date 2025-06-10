import streamlit as st
import requests

st.set_page_config(page_title="PG & Coliving Rent Prediction", layout="centered")
st.title("🏠 PG & Coliving Rent Prediction")

with st.form("predict_form"):
    listing_title = st.text_input("Listing Title")
    city = st.text_input("City")
    area = st.text_input("Area")
    location = st.text_input("Location")
    zone = st.text_input("Zone"["east","west","north","south","central"])
    shearing = st.selectbox("Shearing", ["Single", "Double", "Tripal", "Four"])
    best_suit_for = st.selectbox(
    "Best suited for",
    options=["Students", "Working Professionals", "Students and Working Professionals"]
)

    meals_avilable = st.selectbox("Meals Available", ["Yes", "No"])
    notic_period = st.text_input("Notice Period")
    lock_in_period = st.text_input("Lock-in Period")
    amenities_count = st.number_input("Amenities Count", min_value=0)
    in_time_at_night = st.text_input("In Time at Night")
    non_veg_allowed = st.selectbox("Non-Veg Allowed", ["Yes", "No"])
    opposite_gender_allowed = st.selectbox("Opposite Gender Allowed", ["Yes", "No"])
    visitors_allowed = st.selectbox("Visitors Allowed", ["Yes", "No"])
    gurdian_allowed = st.selectbox("Guardian Allowed", ["Yes", "No"])
    drinking_allowed = st.selectbox("Drinking Allowed", ["Yes", "No"])
    smoking_allowed = st.selectbox("Smoking Allowed", ["Yes", "No"])
    security_deposite = st.number_input("Security Deposit", min_value=0.0)

    submit = st.form_submit_button("Predict Rent")

if submit:
    data = {
        "listing_title": listing_title,
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
        "smoking_allowed": smoking_allowed,
        "security_deposite": security_deposite
    }

    # Replace with actual FastAPI backend URL after deployment
    api_url = "https://pg-rent-api.onrender.com"

    try:
        response = requests.post(api_url, json=data)
        prediction = response.json().get("predicted_rent")
        st.success(f"✅ Predicted Rent: ₹{prediction}")
    except:
        st.error("❌ Could not connect to FastAPI backend. Please check the API URL.")
