#!/usr/bin/env python3
# test_file_storage.py

""" Defines unittests for file_storage.py.
    Unittests classes:
        TestStorage_instantiation
        TestStorage_all
        TestStorage_new
        TestStorage_save
        TestStorage_reload
"""

import os
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestStorage_instantiation(unittest.TestCase):
    """ Unittests for testing the instantiation of the FileStorage Class. """

    def test_storage_is_file_storage(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_no_args_passed(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage("string arg")
        with self.assertRaises(TypeError):
            FileStorage(99, [])

    def test_objects(self):
        with self.assertRaises(AttributeError):
            FileStorage().objects

    def test_objects_private(self):
        with self.assertRaises(AttributeError):
            FileStorage().__objects

    def test_file_path(self):
        with self.assertRaises(AttributeError):
            FileStorage().file_path

    def test_file_path_private(self):
        with self.assertRaises(AttributeError):
            FileStorage().__file_path


class TestStorage_all(unittest.TestCase):
    """ Unittests for testing `all` method in FileStorage Class """

    def test_all_no_args(self):
        self.assertIsNotNone(FileStorage().all())

    def test_all_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage().all({})

    def test_all_return_type(self):
        self.assertIsInstance(FileStorage().all(), dict)


class TestStorage_new(unittest.TestCase):
    """ Unitests for testing the `new` method in FileStorage class """

    def test_new_with_no_args(self):
        with self.assertRaises(TypeError):
            FileStorage().new()

    def test_new_with_one_args(self):
        self.assertIsNone(FileStorage().new(BaseModel()))

    def test_new_with_more_than_one_args(self):
        with self.assertRaises(TypeError):
            FileStorage().new({}, BaseModel())

    def test_new_key_stored(self):
        b1 = BaseModel()
        file1 = FileStorage()
        file1.new(b1)
        all_obj = file1.all()
        key = "{}.{}".format(b1.__class__.__name__, b1.id)
        self.assertIsNotNone(all_obj.get(key, None))

    def test_new_val_stored(self):
        b1 = BaseModel()
        file1 = FileStorage()
        file1.new(b1)
        all_obj = file1.all()
        key = "{}.{}".format(b1.__class__.__name__, b1.id)
        self.assertIs(b1, all_obj.get(key))


class TestStorage_save(unittest.TestCase):
    """ Unittests for testing the save method in FileStorage class."""

    @staticmethod
    def setUp():
        try:
            pass
        except BaseException:
            pass

    @staticmethod
    def tearDown():
        try:
            os.remove('objects.json')
        except IOError:
            pass

    def test_save_more_than_zero_args(self):
        with self.assertRaises(TypeError):
            FileStorage().save(BaseModel())

    def test_save_one_obj(self):
        base = BaseModel()
        storage.save()
        with open('objects.json', 'r') as f:
            txt = f.read()
            self.assertIn("BaseModel." + base.id, txt)

    def test_save_two_or_more_obj(self):
        pass

    def test_save_append_obj(self):
        pass
