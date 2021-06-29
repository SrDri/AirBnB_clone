#!/usr/bin/python3
""" Base class """

import json
from models.review import Review
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ Serializes JSON and deserializes """
    __file_path = 'file.json'
    __objects = {}
    clases = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """ Return dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ New __objects <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize JSON file __objects """
        dict_save = {}
        for key, value in FileStorage.__objects.items():
            valor_dict = value.to_dict()
            dict_save[key] = valor_dict

        with open(FileStorage.__file_path, 'w') as archivo:
            json.dump(dict_save, archivo)

    def reload(self):
        """ Deserialize JSON file __objects """
        try:
            with open(FileStorage.__file_path, 'r') as archivo:
                dicts = json.load(archivo)
                FileStorage.__objects = {}
                for keys, values in dicts.items():
                    obj = FileStorage.clases[values['__class__']](**values)
                    FileStorage.__objects[keys] = obj
        except:
            return

    def find_object(cls, id=''):
        """ Return object id """
        objs = cls.__objects
        for obj in objs.values():
            if obj.id == id:
                return obj
        print("No encuentro la ID :::: {} ::::".format(id))
