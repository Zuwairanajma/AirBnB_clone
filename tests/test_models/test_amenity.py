#!/usr/bin/env python3
# test_amenity.py

""" Defines unitests for the Amenity Class
    Test Classes:
        TestAmenity_instantiation
        TestAmenity_save
        TestAmenity_to_dict
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity_instatiation(unittest.TestCase):
    """ Unittests for testing the instatiation of the class Amenity """

    def test_amenity_class(self):
        self.assertIsInstance(Amenity(), Amenity)

    def test_amenity_subclass(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_with_kwargs(self):
        am = Amenity()
        am_dict = am.to_dict()
        am_new = Amenity(**am_dict)
        self.assertEqual(am.id, am_new.id)
        self.assertEqual(am.created_at, am_new.created_at)
        self.assertEqual(am.updated_at, am_new.updated_at)

    def test_created_at(self):
        self.assertIsInstance(Amenity().created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(Amenity().updated_at, datetime)

    def test_name_attr(self):
        am = Amenity()
        self.assertIsInstance(am.name, str)
        self.assertIn('name', dir(am))


class TestAmenity_save(unittest.TestCase):
    """ Unittests for save method of the Amenity class """

    def testamenity_save(self):
        am = Amenity()
        first_update = am.updated_at
        am.save()
        self.assertLess(first_update, am.updated_at)

    def test_amenity_with_args(self):
        with self.assertRaises(TypeError):
            Amenity().save("update the class")

    def test_amenity_save_wrote_to_file(self):
        am = Amenity()
        am.save()
        am_id = 'Amenity.' + am.id
        with open('objects.json', 'r') as f:
            self.assertIn(am_id, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """ Unittest for to_dict method of Amenity Class """

    def test_amenity_to_dict_type(self):
        self.assertIsInstance(Amenity().to_dict(), dict)

    def test_amenity_to_dict_keys(self):
        am = Amenity()
        self.assertIn('id', am.to_dict())
        self.assertIn('created_at', am.to_dict())
        self.assertIn('updated_at', am.to_dict())

    def test_amenity_to_dict_values_type(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertIsInstance(am_dict['id'], str)
        self.assertIsInstance(am_dict['created_at'], str)
        self.assertIsInstance(am_dict['updated_at'], str)

    def test_amenity_to_dict_new_attr(self):
        am = Amenity()
        am.name = "Amenity name"
        self.assertIn('name', am.to_dict())

    def test_amenity_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            Amenity().to_dict([])


if __name__ == "__main__":
    unittest.main()
