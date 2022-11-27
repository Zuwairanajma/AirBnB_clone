#!/usr/bin/env python3
# test_place.py

""" Defines unitests for the Place Class
    Test Classes:
        TestPlace_instantiation
        TestPlace_save
        TestPlace_to_dict
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace_instatiation(unittest.TestCase):
    """ Unittests for testing the instatiation of the class Place """

    def test_place_class(self):
        self.assertIsInstance(Place(), Place)

    def test_place_subclass(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_with_kwargs(self):
        pl = Place()
        pl_dict = pl.to_dict()
        pl_new = Place(**pl_dict)
        self.assertEqual(pl.id, pl_new.id)
        self.assertEqual(pl.created_at, pl_new.created_at)
        self.assertEqual(pl.updated_at, pl_new.updated_at)

    def test_created_at(self):
        self.assertIsInstance(Place().created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(Place().updated_at, datetime)

    def test_name_attr(self):
        pl = Place()
        self.assertIsInstance(pl.name, str)
        self.assertIn('name', dir(pl))

    def test_city_id_attr(self):
        pl = Place()
        self.assertIsInstance(pl.city_id, str)
        self.assertIn('city_id', dir(pl))

    def test_user_id_attr(self):
        pl = Place()
        self.assertIsInstance(pl.user_id, str)
        self.assertIn('user_id', dir(pl))

    def test_description_attr(self):
        pl = Place()
        self.assertIsInstance(pl.description, str)
        self.assertIn('description', dir(pl))

    def test_number_rooms_attr(self):
        pl = Place()
        self.assertIsInstance(pl.number_rooms, int)
        self.assertIn('number_rooms', dir(pl))

    def test_number_bathrooms_attr(self):
        pl = Place()
        self.assertIsInstance(pl.number_bathrooms, int)
        self.assertIn('number_bathrooms', dir(pl))

    def test_max_guest_attr(self):
        pl = Place()
        self.assertIsInstance(pl.max_guest, int)
        self.assertIn('max_guest', dir(pl))

    def test_price_by_night_attr(self):
        pl = Place()
        self.assertIsInstance(pl.price_by_night, int)
        self.assertIn('price_by_night', dir(pl))

    def test_latitude_attr(self):
        pl = Place()
        self.assertIsInstance(pl.latitude, float)
        self.assertIn('latitude', dir(pl))

    def test_longitude_attr(self):
        pl = Place()
        self.assertIsInstance(pl.longitude, float)
        self.assertIn('longitude', dir(pl))

    def test_amenity_ids_attr(self):
        pl = Place()
        self.assertIsInstance(pl.amenity_ids, list)
        self.assertIn('amenity_ids', dir(pl))


class TestPlace_save(unittest.TestCase):
    """ Unittests for save method of the Place class """

    def testplace_save(self):
        pl = Place()
        first_update = pl.updated_at
        pl.save()
        self.assertLess(first_update, pl.updated_at)

    def test_place_with_args(self):
        with self.assertRaises(TypeError):
            Place().save("update the class")

    def test_place_save_wrote_to_file(self):
        pl = Place()
        pl.save()
        pl_id = 'Place.' + pl.id
        with open('objects.json', 'r') as f:
            self.assertIn(pl_id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """ Unittest for to_dict method of Place Class """

    def test_place_to_dict_type(self):
        self.assertIsInstance(Place().to_dict(), dict)

    def test_place_to_dict_keys(self):
        pl = Place()
        self.assertIn('id', pl.to_dict())
        self.assertIn('created_at', pl.to_dict())
        self.assertIn('updated_at', pl.to_dict())

    def test_place_to_dict_values_type(self):
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertIsInstance(pl_dict['id'], str)
        self.assertIsInstance(pl_dict['created_at'], str)
        self.assertIsInstance(pl_dict['updated_at'], str)

    def test_place_to_dict_new_attr(self):
        pl = Place()
        pl.name = "Place name"
        self.assertIn('name', pl.to_dict())

    def test_place_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            Place().to_dict([])


if __name__ == "__main__":
    unittest.main()
