from pydantic import BaseModel

class PGRentRequest(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    shearing: str
    best_suit_for: str
    meals_avilable: str
    notic_period: str
    lock_in_period: str
    amenities_count: int
    in_time_at_night: str
    non_veg_allowed: str
    opposite_gender_allowed: str
    visitors_allowed: str
    gurdian_allowed: str
    drinking_allowed: str
    smoking_allowed: str
