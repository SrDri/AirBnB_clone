#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Place --")
my_place = Place()
my_place.name = "PepitoRoom"
my_place.number_rooms = 2
my_place.max_guest = 4
my_place.price_by_night = 2000
my_place.latitude = 312112412241214124124124124.30121341242141442112414
my_place.save()
print(my_place)
