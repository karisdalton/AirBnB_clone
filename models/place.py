#!/usr/bin/python3
"""
Place model module
"""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place model implemented for any place object

    Attr:
        city_id: (str) The city's id
        user_id: (str) The user's id
        name: (str) The name of the place
        description: (str) Description of the place
        number_rooms: (int) Number of rooms in the place
        number_bathrooms: (int) Number of bathroooms in the place
        max_guest: (int) Maximum guests per place
        price_by_night: (int) Place's price per night
        latitude: (float) latitude of the place
        longitude: (float) longitude of the place
        amenity_ids: [(str)] List of amenity id's
    """
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
