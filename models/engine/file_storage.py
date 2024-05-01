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

        if hasattr(obj, 'id'):
            FileStorage.__objects['{}.id'.format(type(obj).__name__)] =
            getattr(obj, 'id')

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        If the file doesnt exist, no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                return json.load(json_file)
