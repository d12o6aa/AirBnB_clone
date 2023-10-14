#!/bin/usr/python3
"""
City module
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    City class
    :state_id - t will be the State.id
    :name - name of the city
    """
    state_id = ""
    name = ""
