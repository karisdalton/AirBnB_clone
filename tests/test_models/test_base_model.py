#!/usr/bin/python3
"""
Module containing the test suite for BaseModel class
"""
import unittest
from time import sleep
from uuid import uuid4
from datetime import datetime
import os

import models
from models.base_models import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Tests for models.base_model.BaseModel
    """
    
    def test_if_BaseModel_has_id_attr(self):
        """
        Test to see if the BaseModel class has
        an id instance attribute
        """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))


