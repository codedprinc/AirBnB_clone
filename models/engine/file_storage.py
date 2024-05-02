#!/usr/bin/python3
"""
Module: file_storage.py

Defines  a `FileStorage` class.
"""
import datetime
import json
import os


class FileStorage:
    """
    serializes instances to a JSON file
    deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in  __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        If the file doesnt exist, no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as js_fl:
                    data = json.load(js_fl)
                    data = {k: self.classes()[v["__class__"]](**v)
                            for k, v in data.items()}
                    FileStorage.__objects = obj_dict
            except Exception:
                pass

    def attributes(self):
        """
        returns the valid attributes and their types for classnames

        """

        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
             "user_id": str,
             "text": str}
        }
        return attributes

    def classes(self):
        """

        Returns a dictionary of valid classes and their references

        """

        from models.base_model  import BaseModel
        from models.user  import User
        from models.state  import State
        from models.city  import City
        from models.amenity  import Amenity
        from models.place  import Place
        from models.review  import Review

        classes = {"BaseModel" : BaseModel,
                   "User" : User,
                   "State" : State,
                   "City" : City,
                   "Amenity" : Amenity,
                   "Place" : Place,
                   "Review" : Review}
        return classes
