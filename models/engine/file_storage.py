#!/usr/bin/python3
"""Instantiates the FileStorage class."""
import json
from models.base_model import BaseModel
from models.review import Review
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity


class FileStorage:
    """Reps the abstracted storage engine.

    Attributes:
        __file_path (string): Name of the file to save objects to.
        __objects (dictionary): The dict of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returning the dict __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Specifies the in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Creates series of __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Reduces the series of the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return