#!/usr/bin/python3
""" Base class """
from uuid import uuid4
from datetime import datetime
import json


class BaseModel:
    """ Base class model """

    def __init__(self, *args, **kwargs):
        """ Constructor """
        time_format = '%Y-%m-%dT%H:%M:%S.%f'

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                else:
                    setattr(self, key, value)

            if 'id' in kwargs.keys():
                self.id = kwargs['id']
            if 'created_at' in kwargs.keys():
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    time_format)
            if 'updated_at' in kwargs.keys():
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    time_format)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ representation str"""
        name_cls = __class__.__name__
        return "[{}] ({}) {}".format(name_cls, self.id, self.__dict__)

    def save(self):
        """ update status time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ return __dict__"""
        name_cls = __class__.__name__
        diccionary = self.__dict__
        diccionary['__class__'] = name_cls
        diccionary['created_at'] = self.created_at.isoformat()
        diccionary['updated_at'] = self.updated_at.isoformat()

        return diccionary
