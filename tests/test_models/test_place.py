#!/usr/bin/python3
""" Unittest Place """
import unittest
import os
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Testing """

    @classmethod
    def setUp(cls):
        cls.my_place = Place()
        cls.my_place.city_id = "Medellin"
        cls.my_place.user_id = "jj"
        cls.my_place.name = "Juan"
        cls.my_place.description = "description"
        cls.my_place.number_rooms = 2
        cls.my_place.number_bathrooms = 2
        cls.my_place.max_guest = 3
        cls.my_place.price_by_night = 200
        cls.my_place.latitude = 3.502
        cls.my_place.longitude = 4.021
        cls.my_place.amenity_ids = ["id1", "id2"]

    def test_place_pep8(self):
        """ tests pep8 """
        estilo = pep8.StyleGuide(quiet=True)
        path = estilo.check_files(['models/place.py'])
        self.assertEqual(path.total_errors, 0, "fix pep8")

    def test_place_subclass(self):
        self.assertTrue(issubclass(self.my_place.__class__, BaseModel), True)

    def test_place_doc(self):
        self.assertIsNotNone(Place.__doc__)

    def test_place_atr(self):
        self.assertTrue('city_id' in self.my_place.__dict__)
        self.assertTrue('user_id' in self.my_place.__dict__)
        self.assertTrue('name' in self.my_place.__dict__)
        self.assertTrue('description' in self.my_place.__dict__)
        self.assertTrue('number_rooms' in self.my_place.__dict__)
        self.assertTrue('number_bathrooms' in self.my_place.__dict__)
        self.assertTrue('max_guest' in self.my_place.__dict__)
        self.assertTrue('price_by_night' in self.my_place.__dict__)
        self.assertTrue('latitude' in self.my_place.__dict__)
        self.assertTrue('longitude' in self.my_place.__dict__)
        self.assertTrue('amenity_ids' in self.my_place.__dict__)
        self.assertTrue('created_at' in self.my_place.__dict__)
        self.assertTrue('updated_at' in self.my_place.__dict__)

    def test_place_save(self):
        self.my_place.save()
        created = self.my_place.created_at
        updated = self.my_place.updated_at
        self.assertNotEqual(created, updated)

    def test_place_todict(self):
        self.assertEqual('to_dict' in dir(self.my_place), True)

if __name__ == "__main__":
    unittest.main()
