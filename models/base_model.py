#!/usr/bin/python3
"""
Module: base.py
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class which defines all common attributes
    / methods for other classes
    """

    def __init__(self):
        """
        Instatiates an object with it' s attributes
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return the string representation of the instance
        """
        return '[{0}] ({1}) {2}'.format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute `updated_at`
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of instance.
        """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
