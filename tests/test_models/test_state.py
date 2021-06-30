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
        cls.my_place.name = "Juan"

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
        self.assertTrue('name' in self.my_place.__dict__)
        self.assertTrue('created_at' in self.my_place.__dict__)
        self.assertTrue('updated_at' in self.my_place.__dict__)

    def test_place_save(self):
        self.my_place.save()
        self.assertNotEqual(self. my_place.created_at, self. my_place.updated_at)

    def test_place_todict(self):
        self.assertEqual('to_dict' in dir(self.my_place), True)

if __name__ == "__main__":
    unittest.main()