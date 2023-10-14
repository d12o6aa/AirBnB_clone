#!/usr/bin/python3
"""
Testing the Place model by unittest
"""

import unittest
from models.place import Place
import pycodestyle
from datetime import datetime
from io import StringIO
from unittest.mock import patch


class TestPycodestyle(unittest.TestCase):
    """
    test that we conform to PEP-8
    """
    def test_checking(self):
        """Testing
        pycodestyle"""
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/place.py'])
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
        boolVal = len(Place.__module__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_class_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(Place.__doc__) > 1
        self.assertTrue(boolVal)

    def test_init_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(Place.__init__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_str_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(Place.__str__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_save_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(Place.save.__doc__) > 1
        self.assertTrue(boolVal)

    def test_to_dict_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(Place.to_dict.__doc__) > 1
        self.assertTrue(boolVal)


class TestClassAttributes(unittest.TestCase):
    """
    Testing that class attributes are working correctly
    """

    def test_Inherited_attributes(self):
        """
        testing each attribute's type
        """
        self.assertEqual(Place.id.__class__, str)
        self.assertEqual(Place.created_at.__class__, datetime)
        self.assertEqual(Place.updated_at.__class__, datetime)

    def test_all_attributes_are_public(self):
            """
            Test whether all attributes are public
            """
            obj = Place()            
            attributes = dir(obj)
            public_attributes = [attr for attr in attributes if not attr.startswith('__')]
            class_attributes = dir(Place)
            for attr in class_attributes:
                if not attr.startswith('__'):
                    self.assertIn(attr, public_attributes)

    def test_nonInherited_attributes(self):
        """
        testing each Place object attribute's type
        """
        attributes = dir(Place)
        for attr in attributes:
            if isinstance(attr, str):
                self.assertIsInstance(attr, str)

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
        self.Obj1 = Place()
        self.Obj2 = Place()
        self.ObjKw1 = Place(name="test")
        self.ObjKw2 = Place(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.Objdt = Place(created_at, updated_at)

    def tearDown(self):
        """
        teardown method
        """
        pass

    def test_initialization(self):
        """
        Testing that instances are produced correctly
        """
        self.assertIsInstance(self.Obj1, Place)
        self.assertIsInstance(self.Obj2, Place)
        self.assertTrue(self.Obj1.id)
        self.assertEqual(self.Obj1.id.__class__, str)
        self.assertTrue(self.Obj1.created_at)
        self.assertEqual(self.Obj1.created_at.__class__, datetime)
        self.assertTrue(self.Obj1.updated_at)
        self.assertEqual(self.Obj1.updated_at.__class__, datetime)

    def test_instances_with_attrs(self):
        """
        test with keyworded attrs
        """
        self.assertEqual(self.ObjKw1.name, "test")
        self.assertEqual(self.ObjKw2.name, "test")
        self.assertEqual(self.ObjKw2.value, 98)

    def test_normal_attribute_type(self):
        """
        tests with random attributes and its values
        """
        self.assertIsInstance(self.ObjKw1.name, str)
        self.assertIsInstance(self.ObjKw2.name, str)
        self.assertIsInstance(self.ObjKw2.value, int)

    def test_kwargsInattrs(self):
        """
        Tests dates of creation and updating converting from string to
        datetime objects
        """
        self.assertFalse(self.Objdt.created_at.__class__ == str)
        self.assertTrue(self.Objdt.created_at.__class__ == datetime)
        self.assertFalse(self.Objdt.updated_at.__class__ == str)
        self.assertTrue(self.Objdt.updated_at.__class__ == datetime)


class TestStrMagicMethod(unittest.TestCase):
    """
    Testing __str__ magic method
    """
    def setUp(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        self.Obj1 = Place()
        self.Obj2 = Place()
        self.ObjKw1 = Place(name="test")
        self.ObjKw2 = Place(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.Objdt = Place(created_at, updated_at)

    def tearDown(self):
        """
        teardown method
        """
        pass

    def test_type_output(self):
        """
        testing the type of output
        """
        self.assertIsInstance(str(self.Obj1), str)

    def test_output(self):
        """
        testing the output
        """
        name = self.Obj1.__class__.__name__
        id = self.Obj1.id
        dic = self.Obj1.__dict__
        expected = f"[{name}] ({id}) {dic}"
        self.assertEqual(str(self.Obj1), expected)

    def test_when_printed(self):
        """
        Testing the output of printing an object
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(self.Obj1)
        printed_output = mock_stdout.getvalue().strip()
        name = self.Obj1.__class__.__name__
        id = self.Obj1.id
        dic = self.Obj1.__dict__
        pattern = f"[{name}] ({id}) {dic}"
        self.assertEqual(printed_output, pattern)


class TestSaveMethod(unittest.TestCase):
    """
    testing save
    """
    def setUp(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        self.Obj1 = Place()
        self.Obj2 = Place()
        self.ObjKw1 = Place(name="test")
        self.ObjKw2 = Place(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.Objdt = Place(created_at, updated_at)

    def tearDown(self):
        """
        teardown method
        """
        pass

    def test_if_time_is_updated(self):
        """
        Testing for the time of updating
        """
        time_1 = self.Obj1.updated_at
        self.Obj1.save()
        time_2 = self.Obj1.updated_at
        self.assertNotEqual(time_1, time_2)


if __name__ == '__main__':
    unittest.main()
