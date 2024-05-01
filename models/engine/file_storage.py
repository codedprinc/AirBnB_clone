#!/usr/bin/python3
"""
Module: file_storage.py

Defines  a `FileStorage` class.
"""
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
                for k, v in data.items():
                    clss_name, obj_id = key.split(".")
                    obj_class = globals()[clss_name]
                    obj = obj_class()
                    obj.__dict__.update(v)
                    obj.id = obj_id
                    FileStorage.__objects[k] = obj
                print(FileStorage.__objects)
            except Exception:
                pass
