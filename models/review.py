#!/usr/bin/python3
"""
Review model module
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review model implemented for any review object

    Attr:
        place_id: (str) Id of the place
        user_id: (str) Id of the user
        text: (str) The review itself
    """
    place_id = ""
    user_id = ""
    text = ""
