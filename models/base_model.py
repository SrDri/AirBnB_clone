#!/usr/bin/python3
""" Base class """
from uuid import uuid4
from datetime import datetime
import json


class BaseModel:
    """ Base class model """

    def __init__(self):
        """ Constructor """
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
