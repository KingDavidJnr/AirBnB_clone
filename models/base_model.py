#!/usr/bin/python3
"""Initializes the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Stands for the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Creates a new BaseModel.

        Args:
            *args (any): Unused value.
            **kwargs (dict): Key/value pairs of the attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """To updates the updated_at method with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Prints the dict of the BaseModel instance.

        Including the key/value pair __class__ that represents
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Displays the print/string rep of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)