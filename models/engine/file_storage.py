#!/usr/bin/python3

"""Manage file storage of objects"""

import json
from ..base_model import BaseModel
from ..user import User
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State

class FileStorage:
    """Class to manage file storage of objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all file objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__  + "." + obj.id] = obj

    def save(self):
        """serialize all objects into json file"""
        tmp_dict = {}
        for k, v in self.__objects.items():
            _v = v.to_dict()
            tmp_dict[k] = _v

        with open(self.__file_path, "w") as f:
            json.dump(tmp_dict, f)

    def reload(self):
        """deserialize from file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                tmp_dict = json.load(f)

            for k, v in tmp_dict.items():
                self.__objects[k] = eval(v["__class__"])(**v)
        except FileNotFoundError:
            pass