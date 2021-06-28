#!/usr/bin/python3
""" Base class """
import json
import models
from uuid import uuid4
from datetime import datetime


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
            models.storage.new(self)

    def __str__(self):
        """ representation str"""
        name_cls = __class__.__name__
        return "[{}] ({}) {}".format(name_cls, self.id, self.__dict__)

    def save(self):
        """ update status time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return __dict__"""
        name_cls = __class__.__name__
        self_dict = self.__dict__.copy()
        self_dict['__class__'] = name_cls
        self_dict['created_at'] = self.created_at.isoformat()
        self_dict['updated_at'] = self.updated_at.isoformat()
        return self_dict
