#!/usr/bin/python3
""" Unittest City """
import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Testing """

    @classmethod
    def setUp(cls):
        cls.my_city = City()
        cls.my_city.state_id = "Antioquia"
        cls.my_city.name = "Medellin"

    def test_city_pep8(self):
        """ tests pep8 """
        estilo = pep8.StyleGuide(quiet=True)
        path = estilo.check_files(['models/city.py'])
        self.assertEqual(path.total_errors, 0, "fix pep8")

    def test_city_subclass(self):
        self.assertTrue(issubclass(self.my_city.__class__, BaseModel), True)

    def test_city_doc(self):
        self.assertIsNotNone(City.__doc__)

    def test_city_atr(self):
        self.assertTrue('state_id' in self.my_city.__dict__)
        self.assertTrue('name' in self.my_city.__dict__)
        self.assertTrue('created_at' in self.my_city.__dict__)
        self.assertTrue('updated_at' in self.my_city.__dict__)

    def test_city_save(self):
        self.my_city.save()
        self.assertNotEqual(self. my_city.created_at, self. my_city.updated_at)

    def test_city_todict(self):
        self.assertEqual('to_dict' in dir(self.my_city), True)

if __name__ == "__main__":
    unittest.main()
