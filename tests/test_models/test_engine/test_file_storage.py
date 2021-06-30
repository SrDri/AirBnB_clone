#!/usr/bin/python3
""" FileStorage unittest """
import os
import unittest
import pep8
import models
import models.base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestStorageDocumentation(unittest.TestCase):
    """ file storage docs """

    def test_filestorage_pep8(self):
        estilo = pep8.StyleGuide(quiet=True)
        path = estilo.check_files(['models/engine/file_storage.py'])
        self.assertEqual(path.total_errors, 0, "fix pep8")

    def test_shebang(self):
        with open("models/engine/file_storage.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_amenity_doc(self):
        self.assertIsNotNone(FileStorage.__doc__)

    def test_methods_doc(self):
        self.assertTrue(len(FileStorage.all.__doc__) != 0)
        self.assertTrue(len(FileStorage.new.__doc__) != 0)
        self.assertTrue(len(FileStorage.save.__doc__) != 0)
        self.assertTrue(len(FileStorage.reload.__doc__) != 0)

    """ edge cases """
    def test_attribute_path(self):
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertTrue(FileStorage._FileStorage__file_path != 0)
        self.assertTrue(type(FileStorage._FileStorage__file_path) is str)

    def test_attribute_class_objects(self):
        self.assertTrue(type(FileStorage._FileStorage__objects) is dict)

    def test_all(self):
        object = models.storage.all()
        self.assertIsInstance(object, dict)

    def test_new(self):
        pass

    def test_save_exists(self):
        file = "objeto.json"
        self.assertTrue(os.path.exists(file))
        FileStorage._FileStorage__file_path = "objeto.json"
        obj = BaseModel()
        obj.save()
        self.assertTrue(os.path.exists(file))
        os.remove(file)

    def test_reload(self):
        pass
