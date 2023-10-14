#!/usr/bin/python3
"""
Models (classes) of the project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all our classes
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        init method for baseModel instances
        """
        if kwargs:
            for key in kwargs.keys():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    formatOfdate = '%Y-%m-%dT%H:%M:%S.%f'
                    dateetime = datetime.strptime(kwargs[key], formatOfdate)
                    setattr(self, key, dateetime)
                    continue
                setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        :return:Return the print/str
        representation of the BaseModel instance.
        """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def __repr__(self):
        """
        repr
        """
        return self.__str__

    def save(self):
        """
        Update updated_at with the current datetime.
        :return: None
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        :return: Return the dictionary of the BaseModel instance.
        """
        dict = self.__dict__.copy()
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
