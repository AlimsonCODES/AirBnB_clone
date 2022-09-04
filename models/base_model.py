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
        if len(kwargs) != 0:
            for i in kwargs:
                if i == "__class__":
                    del(i)
                    break
            self.id = kwargs['id']
            kwargs['created_at'] = datetime.datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.created_at = kwargs['created_at']
            self.updated_at = kwargs['updated_at']
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.save()

    def __str__(self):
        return '[{}] ({}) {}'\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()
        return self.updated_at

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        self.__dict__['__class__'] = type(self).__name__

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
