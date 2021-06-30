#!/usr/bin/python3
""" Unittest State """
import unittest
import os
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Testing """

    @classmethod
    def setUp(cls):
        cls.my_state = State()
        cls.my_state.name = "Juan"

    def test_state_pep8(self):
        """ tests pep8 """
        estilo = pep8.StyleGuide(quiet=True)
        path = estilo.check_files(['models/state.py'])
        self.assertEqual(path.total_errors, 0, "fix pep8")

    def test_state_subclass(self):
        self.assertTrue(issubclass(self.my_state.__class__, BaseModel), True)

    def test_state_doc(self):
        self.assertIsNotNone(State.__doc__)

    def test_state_atr(self):
        self.assertTrue('name' in self.my_state.__dict__)
        self.assertTrue('created_at' in self.my_state.__dict__)
        self.assertTrue('updated_at' in self.my_state.__dict__)

    def test_state_save(self):
        self.my_state.save()
        created = self.my_state.created_at
        updated = self.my_state.updated_at
        self.assertNotEqual(created, updated)

    def test_state_todict(self):
        self.assertEqual('to_dict' in dir(self.my_state), True)

if __name__ == "__main__":
    unittest.main()
