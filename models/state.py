#!/usr/bin/python3
"""
State model module
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    State class implementing the state model for a state object

    Attr:
        name: (str) The state's name.
    """
    name = ""
