#!/usr/bin/python3
"""
Simple User implementation
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from the BaseModel class

    Attr:
        email: (str) user's email
        password: (str) user's password
        first_name: (str) user's firstname
        last_name: (str) user's lastname
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
