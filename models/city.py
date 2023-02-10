#!/usr/bin/python3
"""
City Model Module
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    City Model implemented for a city object

    Attr:
        state_id: (str) State ID rep as State.id
        name: (str) City name
    """
    state_id = ""
    name = ""
