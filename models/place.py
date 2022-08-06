<<<<<<< HEAD
#!/usr/bin/python3
"""State module"""
from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
=======
#!/usr/bin/python3
"""State module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """place model"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
>>>>>>> f2f06b18c3c9734cb473ccd4bfc353c72b2619ef
