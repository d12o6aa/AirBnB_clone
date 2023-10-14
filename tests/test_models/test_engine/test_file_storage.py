#!/usr/bin/python3
"""
Tests for the file storage
"""
import os
import json
import models
import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestPycodestyle(unittest.TestCase):
    """
    test that we conform to PEP-8
    """
    def test_checking(self):
        """Testing
        pycodestyle"""
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocuemntationOfAll(unittest.TestCase):
    """
    This class will have the unittesting of that the
    whole module is well documented
    """
    def test_module_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(FileStorage.__module__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_class_doc(self):
        """
        Test if class documentation exists
        """
        boolVal = len(FileStorage.__doc__) > 1
        self.assertTrue(boolVal)

    def test_save_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(FileStorage.save.__doc__) > 1
        self.assertTrue(boolVal)

    def test_all_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(FileStorage.all.__doc__) > 1
        self.assertTrue(boolVal)

    def test_new_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(FileStorage.new.__doc__) > 1
        self.assertTrue(boolVal)

    def test_reload_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(FileStorage.reload.__doc__) > 1
        self.assertTrue(boolVal)


class TestInitialization(unittest.TestCase):
    """
    Test File storage intialization
    """
    def test_no_arguments(self):
        """
        Test normal case (no arguments)
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_type_attrs(self):
        """
        Test type the attributes
        """
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)


class TestMethods(unittest.TestCase):
    """
    This class is for testing all method
    """
    def setUp(self):
        """
        Setup for this class
        """
        self.user = User()
        self.state = State()
        self.amenity = Amenity()
        self.city = City()
        self.review = Review()
        self.place = Place()
        self.objectsList = [self.user, self.state, self.amenity, self.city,
                            self.review, self.place]

    def tearDown(self):
        """
        TearDown
        """
        pass

    def test_storageAll(self):
        """
        Test in normal conditions
        """
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """
        Testing new method
        """
        for obj in self.objectsList:
            storage.new(obj)
            self.assertIn(f"{obj.__class__.__name__}.{obj.id}",
                          storage.all().keys())

    def test_save(self):
        """
        Testing save method
        """
        for obj in self.objectsList:
            storage.new(obj)
        storage.save()
        with open('file.json', 'r', encoding="UTF-8") as f:
            data = f.read()
            self.assertIn(f'{obj.__class__.__name__}.' + obj.id, data)

    def test_reload1(self):
        """
        Testing the reload method
        """
        storage.reload()
        for value in storage._FileStorage__objects.values():
            for obj in self.objectsList:
                if value == obj:
                    self.assertTrue(value == obj)

    def test_reload2(self):
        """
        Testing the reload method with an empty file
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        self.assertIs(storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
