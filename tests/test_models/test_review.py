#!/usr/bin/python3
""" Unittest Review """
import unittest
import os
import pep8
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """ Testing """

    @classmethod
    def setUp(cls):
        cls.my_review = Review()
        cls.my_review.place_id = "Antioquia"
        cls.my_review.user_id = "Juan"
        cls.my_review.text = "Hola"

    def test_review_pep8(self):
        """ tests pep8 """
        estilo = pep8.StyleGuide(quiet=True)
        path = estilo.check_files(['models/review.py'])
        self.assertEqual(path.total_errors, 0, "fix pep8")

    def test_review_subclass(self):
        self.assertTrue(issubclass(self.my_review.__class__, BaseModel), True)

    def test_review_doc(self):
        self.assertIsNotNone(Review.__doc__)

    def test_review_atr(self):
        self.assertTrue('place_id' in self.my_review.__dict__)
        self.assertTrue('user_id' in self.my_review.__dict__)
        self.assertTrue('text' in self.my_review.__dict__)
        self.assertTrue('created_at' in self.my_review.__dict__)
        self.assertTrue('updated_at' in self.my_review.__dict__)

    def test_review_save(self):
        self.my_review.save()
        self.assertNotEqual(self. my_review.created_at, self. my_review.updated_at)

    def test_review_todict(self):
        self.assertEqual('to_dict' in dir(self.my_review), True)

if __name__ == "__main__":
    unittest.main()