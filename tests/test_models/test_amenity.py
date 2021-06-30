#!/usr/bin/python3
""" Unittest Amenity """
import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Testing """

    @classmethod
    def setUp(cls):
        cls.my_amenity = Amenity()
        cls.my_amenity.name = "Juan"

    def test_amenity_pep8(self):
        """ tests pep8 """
        estilo = pep8.StyleGuide(quiet=True)
        path = estilo.check_files(['models/amenity.py'])
        self.assertEqual(path.total_errors, 0, "fix pep8")

    def test_amenity_subclass(self):
        self.assertTrue(issubclass(self.my_amenity.__class__, BaseModel), True)

    def test_amenity_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_amenity_atr(self):
        self.assertTrue('name' in self.my_amenity.__dict__)
        self.assertTrue('created_at' in self.my_amenity.__dict__)
        self.assertTrue('updated_at' in self.my_amenity.__dict__)

    def test_amenity_save(self):
        self.my_amenity.save()
        created = self.my_amenity.created_at
        updated = self.my_amenity.updated_at
        self.assertNotEqual(created, updated)

    def test_amenity_todict(self):
        self.assertEqual('to_dict' in dir(self.my_amenity), True)

if __name__ == "__main__":
    unittest.main()
