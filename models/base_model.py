#!/usr/bin/python3
"""
Models
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class for all our classes
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self):
        self.id = BaseModel.id
        self.created_at = BaseModel.created_at
        self.updated_at = BaseModel.updated_at

    def __str__(self):
        """
        :return:Return the print/str
        representation of the BaseModel instance.
        """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """
        Update updated_at with the current datetime.
        :return: None
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        :return: Return the dictionary of the BaseModel instance.
        """
        dict = self.__dict__.copy()
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
