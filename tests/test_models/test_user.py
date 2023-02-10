#!/usr/bin/python3
"""Test suite for the User class in models.user"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases against the User class"""
    def setup(self):
        self.user = User()

    def test_attrs_are_class_attrs(self):
        # test that it is a class attribute
        self.assertTrue(hasattr(self.user, "first_name")
                        and hasattr(self.user, "last_name"))

    def test_class_attrs(self):
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.last_name), str)
        self.assertTrue(self.user.first_name == "")
        self.assertTrue(self.user.last_name == "")

    def test_user_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.user), BaseModel))
