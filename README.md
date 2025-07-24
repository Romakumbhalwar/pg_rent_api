PG & Coliving Rent Price Prediction

This project is a machine learning pipeline to predict the rental price 
of PG and coliving accommodations based on various attributes such as location, 
shearing type, amenities, and rules.

live demo:https://pg-rent-api-1.onrender.com

Project Overview

-  Model: `RandomForestRegressor`
-  Pipeline: OneHotEncoding + Regression
-  Dataset: `pg_coliving_dataset.csv`
-  Target: `rent_price`
-  Output: `pg_rent_final_model.pkl`

Features Used

- Location Info: `city`, `area`, `location`, `zone`
- Accommodation Type: `shearing`, `best_suit_for`, `meals_avilable`
- Stay Terms: `notic_period`, `lock_in_period`
- Rules: `in_time_at_night`, `non_veg_allowed`, `opposite_gender_allowed`, `visitors_allowed`, `gurdian_allowed`, `drinking_allowed`, `smoking_allowed`
- Others: `amenities_count`, `meals_shearing` *(engineered feature)

Data Preprocessing

- Merged rare `shearing` categories (`four`, `multi`) into `shared`
- Created interaction feature: `meals_shearing = meals_avilable + "_" + shearing`
- One-hot encoded categorical columns
- Converted `amenities_count` and `rent_price` to numeric