#!/usr/bin/python3
"""
Testing the base model by unittest
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import pycodestyle
from datetime import datetime


class TestPycodestyle(unittest.TestCase):
    """
    test that we conform to PEP-8
    """
    def test_checking(self):
        """Testing
        pycodestyle"""
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/base_model.py'])
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
        boolVal = len(BaseModel.__module__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_class_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.__doc__) > 1
        self.assertTrue(boolVal)

    def test_init_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.__init__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_str_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.__str__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_save_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.save.__doc__) > 1
        self.assertTrue(boolVal)

    def test_to_dict_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.to_dict.__doc__) > 1
        self.assertTrue(boolVal)

class TestClassAttributes(unittest.TestCase):
    """
    Testing that class attributes are working correctly
    """
    def test_attributes(self):
        """
        testing each attribute's type
        """
        self.assertEqual(BaseModel.id.__class__, str)
        self.assertEqual(BaseModel.created_at.__class__, datetime)
        self.assertEqual(BaseModel.updated_at.__class__, datetime)

class TestConstructorMethod(unittest.TestCase):
    """
    Testing the __init__ method
    """
    def setUp(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        self.testObject1 = BaseModel()
        self.testObject2 = BaseModel()
        self.testObjKwarg1 = BaseModel(name="test")
        self.testObjKwarg2 = BaseModel(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.testObjdate = BaseModel(created_at, updated_at)

    def tearDown(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        pass

    def test_initialization(self):
        """
        Testing that instances are produced correctly
        """
        self.assertIsInstance(self.testObject1, BaseModel)
        self.assertIsInstance(self.testObject2, BaseModel)
        self.assertTrue(self.testObject1.id)
        self.assertEqual(self.testObject1.id.__class__, str)
        self.assertTrue(self.testObject1.created_at)
        self.assertEqual(self.testObject1.created_at.__class__, datetime)
        self.assertTrue(self.testObject1.updated_at)
        self.assertEqual(self.testObject1.updated_at.__class__, datetime)

    def test_instances_with_attrs(self):
        """
        test with keyworded attrs
        """
        self.assertEqual(self.testObjKwarg1.name, "test")
        self.assertEqual(self.testObjKwarg2.name, "test")
        self.assertEqual(self.testObjKwarg2.value, 98)

    def test_normal_attribute_type(self):
        """
        tests with random attributes and its values
        """
        self.assertIsInstance(self.testObjKwarg1.name, str)
        self.assertIsInstance(self.testObjKwarg2.name, str)
        self.assertIsInstance(self.testObjKwarg2.value, int)

    def test_kwargsInattrs(self):
        """
        Tests dates of creation and updating converting from string to
        datetime objects
        """
        self.assertFalse(self.testObjdate.created_at.__class__ == str)
        self.assertTrue(self.testObjdate.created_at.__class__ == datetime)
        self.assertFalse(self.testObjdate.updated_at.__class__ == str)
        self.assertTrue(self.testObjdate.updated_at.__class__ == datetime)

# To be continued

class TestStrMagicMethod(unittest.TestCase):
    ...
class TestSaveMethod(unittest.TestCase):
    ...
class TestToDictMethod(unittest.TestCase):
    ...


if __name__ == '__main__':
    unittest.main()
