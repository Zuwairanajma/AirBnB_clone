#!/usr/bin/env python3
# test_city.py

""" Defines unittests for the Class City
    Test Classes:
        TestCity_instantiation
        TestCity_save
        TestCity_to_dict
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """ Unittests for testing the instantiation of the class City """

    def test_city_class(self):
        self.assertIsInstance(City(), City)

    def test_subclass(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_with_kwargs(self):
        ct = City()
        ct_dict = ct.to_dict()
        ct_new = City(**ct_dict)
        self.assertEqual(ct.id, ct_new.id)
        self.assertEqual(ct.created_at, ct_new.created_at)
        self.assertEqual(ct.updated_at, ct_new.updated_at)

    def test_created_at(self):
        self.assertIsInstance(City().created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(City().updated_at, datetime)

    def test_name_attr(self):
        ct = City()
        self.assertIsInstance(ct.name, str)
        self.assertIn('name', dir(ct))

    def test_state_id_attr(self):
        ct = City()
        self.assertIsInstance(ct.state_id, str)
        self.assertIn('state_id', dir(ct))


class TestCity_save(unittest.TestCase):
    """ Unittests for testing save method for City Class """

    def test_save(self):
        ct = City()
        first_update = ct.updated_at
        ct.save()
        self.assertLess(first_update, ct.updated_at)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            City().save("Save Now")

    def test_write_to_file(self):
        ct = City()
        ct.save()
        ct_id = 'City.' + ct.id
        with open('objects.json', 'r') as f:
            self.assertIn(ct_id, f.read())


class TestCity_to_dict(unittest.TestCase):
    """ Unittests for the to_dict method of City class """

    def test_to_dict_type(self):
        self.assertIsInstance(City().to_dict(), dict)

    def test_to_dict_keys(self):
        ct = City()
        self.assertIn('id', ct.to_dict())
        self.assertIn('created_at', ct.to_dict())
        self.assertIn('updated_at', ct.to_dict())
        self.assertIn('__class__', ct.to_dict())

    def test_to_dict_values_type(self):
        ct = City()
        ct_dict = ct.to_dict()
        self.assertIsInstance(ct_dict['id'], str)
        self.assertIsInstance(ct_dict['created_at'], str)
        self.assertIsInstance(ct_dict['updated_at'], str)

    def test_to_dict_new_attr(self):
        ct = City()
        ct.name = "My name"
        self.assertIn('name', ct.to_dict())

    def test_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            City().to_dict(555)


if __name__ == "__main__":
    unittest.main()
