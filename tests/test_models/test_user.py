#!/usr/bin/env python3
# test_user.py

""" Defines unitests for the User Class
    Test Classes:
        TestUser_instantiation
        TestUser_save
        TestUser_to_dict
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser_instatiation(unittest.TestCase):
    """ Unittests for testing the instatiation of the class User """

    def test_obj_is_user(self):
        self.assertIsInstance(User(), User)

    def test_user_subclass(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_with_kwargs(self):
        us = User()
        us_dict = us.to_dict()
        us_new = User(**us_dict)
        self.assertEqual(us.id, us_new.id)
        self.assertEqual(us.created_at, us_new.created_at)
        self.assertEqual(us.updated_at, us_new.updated_at)

    def test_created_at(self):
        self.assertIsInstance(User().created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(User().updated_at, datetime)

    def test_email_attr(self):
        us = User()
        self.assertIsInstance(us.email, str)
        self.assertIn('email', dir(us))

    def test_password_attr(self):
        us = User()
        self.assertIsInstance(us.password, str)
        self.assertIn('password', dir(us))

    def test_first_name_attr(self):
        us = User()
        self.assertIsInstance(us.first_name, str)
        self.assertIn('first_name', dir(us))

    def test_last_name_attr(self):
        us = User()
        self.assertIsInstance(us.last_name, str)
        self.assertIn('last_name', dir(us))


class TestUser_save(unittest.TestCase):
    """ Unittests for save method of the User class """
    def testuser_save(self):
        us = User()
        first_update = us.updated_at
        us.save()
        self.assertLess(first_update, us.updated_at)

    def test_user_with_args(self):
        with self.assertRaises(TypeError):
            User().save("update the class")

    def test_user_save_wrote_to_file(self):
        us = User()
        us.save()
        us_id = 'User.' + us.id
        with open('objects.json', 'r') as f:
            self.assertIn(us_id, f.read())


class TestUser_to_dict(unittest.TestCase):
    """ Unittest for to_dict method of User Class """
    def test_user_to_dict_type(self):
        self.assertIsInstance(User().to_dict(), dict)

    def test_user_to_dict_keys(self):
        us = User()
        self.assertIn('id', us.to_dict())
        self.assertIn('created_at', us.to_dict())
        self.assertIn('updated_at', us.to_dict())

    def test_user_to_dict_values_type(self):
        us = User()
        us_dict = us.to_dict()
        self.assertIsInstance(us_dict['id'], str)
        self.assertIsInstance(us_dict['created_at'], str)
        self.assertIsInstance(us_dict['updated_at'], str)

    def test_user_to_dict_new_attr(self):
        us = User()
        us.name = "User name"
        self.assertIn('name', us.to_dict())

    def test_user_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            User().to_dict([])


if __name__ == "__main__":
    unittest.main()
