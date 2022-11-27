#!/usr/bin/env python3
# test_base_model.py

""" Defines unittests for base_model.py.
    Unittest classes:
        TestBase_instantiation
        TestBase_save
        TestBase_to_dict
        TestBase_with_kwargs
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase_instantiation(unittest.TestCase):
    """ Unittests for testing the instantiation of the BaseModel class. """

    def test_obj_is_basemodel(self):
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_no_args(self):
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_type_of_id(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertEqual(type(BaseModel().id), str)
        self.assertEqual(type(base1.id), type(base2.id))

    def test_unique_id(self):
        base1 = BaseModel()
        base2 = BaseModel()
        base3 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base2.id, base3.id)
        self.assertNotEqual(base3.id, base1.id)

    def test_created_at_type(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base1.created_at, datetime)
        self.assertEqual(type(base1.created_at), type(base2.created_at))

    def test_created_at_unique(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.created_at, base2.created_at)

    def test_updated_at_type(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(BaseModel().updated_at, datetime)
        self.assertEqual(type(base1.updated_at), type(base2.updated_at))

    def test_updated_at_unique(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.updated_at, base2.updated_at)


class TestBase_with_kwargs(unittest.TestCase):
    """ Unittests for initialising BaseModel object with kwargs """

    def test_create_BaseModel(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertEqual(str(b1), str(b2))
        obj_str = "[" + b1.__class__.__name__ + \
            "] (" + b1.id + ") " + str(b1.__dict__)
        self.assertEqual(obj_str, str(b1))

    def test_create_basemodel_is(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertIsNot(b1, b2)

    def test_create_baseModel_equals(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertNotEqual(b1, b2)

    def test_create_baseModel_update_at_type(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertIsInstance(b2.updated_at, datetime)

    def test_create_baseModel_create_at_type(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertIsInstance(b2.created_at, datetime)

    def test_create_BaseModel_getattr_class(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        with self.assertRaises(KeyError):
            print(b2.__dict__[__class__])


class TestBase_save(unittest.TestCase):
    """ Unittests for testing the save method in BaseModel Class. """

    def test_save_no_args(self):
        base1 = BaseModel()
        old_date = base1.updated_at
        base1.save()
        self.assertNotEqual(base1.updated_at, old_date)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            BaseModel().save(datetime.now())
        with self.assertRaises(TypeError):
            BaseModel().save(863, "two_args")
        with self.assertRaises(TypeError):
            BaseModel().save({"key": "value"})

    def test_save_type(self):
        base1 = BaseModel()
        base1.save()
        self.assertIsInstance(base1.updated_at, datetime)

    def test_save_changed_value(self):
        base1 = BaseModel()
        old_date = base1.updated_at
        base1.save()
        self.assertNotEqual(base1.updated_at, old_date)


class TestBase_to_dict(unittest.TestCase):
    """ Unittests for testing the to_dict method of the BaseModel class """

    def test_to_dict_no_args(self):
        self.assertIsInstance(BaseModel().to_dict(), dict)

    def test_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            BaseModel().to_dict("one arg")

        with self.assertRaises(TypeError):
            BaseModel().to_dict(
                "first arg", ["a list"], ("a tuple", "with another element"))

        with self.assertRaises(TypeError):
            BaseModel().to_dict(9, 87)

    def test_to_dict_type(self):
        self.assertIsInstance(BaseModel().to_dict(), dict)

    def test_to_dict_created_at_type(self):
        base = BaseModel().to_dict()
        created = base.get('created_at', None)
        self.assertIsInstance(created, str)

    def test_to_dict_updated_at_type(self):
        base = BaseModel()
        updated = base.to_dict().get('updated_at', None)
        self.assertIsInstance(updated, str)


class TestBase_string(unittest.TestCase):
    """ Unittest for testing the __str__ method in BaseModel class. """

    def test_string_type(self):
        base_str = BaseModel().__str__()
        self.assertIsInstance(base_str, str)

    def test_string_format(self):
        base = BaseModel()
        class_name = base.__class__
        base_id = base.id
        obj_str = "[" + base.__class__.__name__ + \
            "] (" + base.id + ") " + str(base.__dict__)
        self.assertEqual(base.__str__(), obj_str)


if "__name__" == "__main__":
    unittest.main()
