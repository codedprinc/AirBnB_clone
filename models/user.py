#!/usr/bin/python3
"""
Module: First User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from `BaseModel`
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
