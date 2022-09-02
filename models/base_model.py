#!/usr/bin/python3
"""
This module creates a BaseModel class
"""
import datetime
import uuid


class BaseModel:
    """ This is the base class"""

    def __init__(self, *args, **kwargs):
        """initializes"""
        if len(kwargs) == 0:
            for i in dir(kwargs):
                if i == "__class__":
                    continue
                else:
                    self.i = kwargs.get(i)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()

    def __str__(self):
        return '[{}] ({}) {}'\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        self.__dict__['__class__'] = type(self).__name__

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
