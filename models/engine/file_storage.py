#!/usr/bin/python3
""" Base class """

from models.base_model import BaseModel
import json


class FileStorage:
    """ Serializes JSON and deserializes """
    __file_path = 'file.json'
    __objects = {}
    clases = {
        "BaseModel": BaseModel
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
