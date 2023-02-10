#!/usr/bin/python3
"""
Module implementing the FileStorage serialization
and deserialization class
"""
import json

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    Class that serializes instances to a JSON file
    and deserializes JSON files to instances
    """
    
    __file__path = "file.json"
    __objects = {}

    def all(self):
        """
        Method returning the __objects dict
        """
        return self.__objects
    
    def new(self, obj):
        """
        This method sets the obj in __objects with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file(path: __file_path)
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        deserializes the JSON file to __objects,
        only if the JSON(__file_path) exists; otherwise do nothing;
        if the file doesn't exist, no exception should be raised
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return

