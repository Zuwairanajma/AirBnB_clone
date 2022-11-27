#!/usr/bin/env python3
# test_state.py

""" Defines unitests for the State Class
    Test Classes:
        TestState_instantiation
        TestState_save
        TestState_to_dict
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState_instatiation(unittest.TestCase):
    """ Unittests for testing the instatiation of the class State """

    def test_obj_is_state(self):
        self.assertIsInstance(State(), State)

    def test_state_subclass(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_with_kwargs(self):
        st = State()
        st_dict = st.to_dict()
        st_new = State(**st_dict)
        self.assertEqual(st.id, st_new.id)
        self.assertEqual(st.created_at, st_new.created_at)
        self.assertEqual(st.updated_at, st_new.updated_at)

    def test_created_at(self):
        self.assertIsInstance(State().created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(State().updated_at, datetime)

    def test_name_attr(self):
        st = State()
        self.assertIsInstance(st.name, str)
        self.assertIn('name', dir(st))


class TestState_save(unittest.TestCase):
    """ Unittests for save method of the State class """
    def teststate_save(self):
        st = State()
        first_update = st.updated_at
        st.save()
        self.assertLess(first_update, st.updated_at)

    def test_state_with_args(self):
        with self.assertRaises(TypeError):
            State().save("update the class")

    def test_state_save_wrote_to_file(self):
        st = State()
        st.save()
        st_id = 'State.' + st.id
        with open('objects.json', 'r') as f:
            self.assertIn(st_id, f.read())


class TestState_to_dict(unittest.TestCase):
    """ Unittest for to_dict method of State Class """
    def test_state_to_dict_type(self):
        self.assertIsInstance(State().to_dict(), dict)

    def test_state_to_dict_keys(self):
        st = State()
        self.assertIn('id', st.to_dict())
        self.assertIn('created_at', st.to_dict())
        self.assertIn('updated_at', st.to_dict())

    def test_state_to_dict_values_type(self):
        st = State()
        st_dict = st.to_dict()
        self.assertIsInstance(st_dict['id'], str)
        self.assertIsInstance(st_dict['created_at'], str)
        self.assertIsInstance(st_dict['updated_at'], str)

    def test_state_to_dict_new_attr(self):
        st = State()
        st.name = "State name"
        self.assertIn('name', st.to_dict())

    def test_state_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            State().to_dict([])


if __name__ == "__main__":
    unittest.main()
