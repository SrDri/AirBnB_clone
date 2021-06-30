#!/usr/bin/python3
""" Unittets BaseModel class """

import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing """

    @classmethod
    def setUpClass(cls):
        cls.base_m = BaseModel()
        cls.base_m.name = "Juan"
        cls.base_m.my_number = 89

    def test_docstrings(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init(self):
        self.assertTrue(isinstance(self.base_m, BaseModel))

    def test_save(self):
        self.base_m.save()
        self.assertNotEqual(self.base_m.created_at, self.base_m.updated_at)

    def test_to_dict(self):
        base_m_dict = self.base_m.to_dict()
        self.assertIsInstance(base_m_dict['created_at'], str)
        self.assertIsInstance(base_m_dict['updated_at'], str)
        self.assertEqual(self.base_m.__class__.__name__, 'BaseModel')