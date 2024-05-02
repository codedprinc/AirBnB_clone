#!/usr/bin/python3
"""


Module: review.py


"""
from models.base_model import BaseModel


class Review(BaseModel):
    """

    Inherits from `BaseModel`


    """

    place_id = ""
    user_id = ""
    text = ""
