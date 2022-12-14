#!/usr/bin/python3

"""Base model module for all classes"""

import uuid
import datetime
import models


class BaseModel:
    """Base model from which all other classes inherit from"""

    def __init__(self, *args, **kwargs):
        """?"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.datetime.fromisoformat(v)
                    self.__setattr__(k, v)
                elif k != "__class__":
                    self.__setattr__(k, v)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def __str__(self):
        """return string rep"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save to storage"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """convert to dictionary"""
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = type(self).__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr
