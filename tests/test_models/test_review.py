#!/usr/bin/env python3
# test_review.py

""" Defines unitests for the Review Class
    Test Classes:
        TestReview_instantiation
        TestReview_save
        TestReview_to_dict
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview_instatiation(unittest.TestCase):
    """ Unittests for testing the instatiation of the class Review """

    def test_review_class(self):
        self.assertIsInstance(Review(), Review)

    def test_review_subclass(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_with_kwargs(self):
        rv = Review()
        rv_dict = rv.to_dict()
        rv_new = Review(**rv_dict)
        self.assertEqual(rv.id, rv_new.id)
        self.assertEqual(rv.created_at, rv_new.created_at)
        self.assertEqual(rv.updated_at, rv_new.updated_at)

    def test_created_at(self):
        self.assertIsInstance(Review().created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(Review().updated_at, datetime)

    def test_text_attr(self):
        rv = Review()
        self.assertIsInstance(rv.text, str)
        self.assertIn('text', dir(rv))

    def test_place_id_attr(self):
        rv = Review()
        self.assertIsInstance(rv.place_id, str)
        self.assertIn('place_id', dir(rv))

    def test_user_id_attr(self):
        rv = Review()
        self.assertIsInstance(rv.user_id, str)
        self.assertIn('user_id', dir(rv))


class TestReview_save(unittest.TestCase):
    """ Unittests for save method of the Review class """

    def testreview_save(self):
        rv = Review()
        first_update = rv.updated_at
        rv.save()
        self.assertLess(first_update, rv.updated_at)

    def test_review_with_args(self):
        with self.assertRaises(TypeError):
            Review().save("update the class")

    def test_review_save_wrote_to_file(self):
        rv = Review()
        rv.save()
        rv_id = 'Review.' + rv.id
        with open('objects.json', 'r') as f:
            self.assertIn(rv_id, f.read())


class TestReview_to_dict(unittest.TestCase):
    """ Unittest for to_dict method of Review Class """

    def test_review_to_dict_type(self):
        self.assertIsInstance(Review().to_dict(), dict)

    def test_review_to_dict_keys(self):
        rv = Review()
        self.assertIn('id', rv.to_dict())
        self.assertIn('created_at', rv.to_dict())
        self.assertIn('updated_at', rv.to_dict())

    def test_review_to_dict_values_type(self):
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertIsInstance(rv_dict['id'], str)
        self.assertIsInstance(rv_dict['created_at'], str)
        self.assertIsInstance(rv_dict['updated_at'], str)

    def test_review_to_dict_new_attr(self):
        rv = Review()
        rv.name = "Review name"
        self.assertIn('name', rv.to_dict())

    def test_review_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            Review().to_dict([])


if __name__ == "__main__":
    unittest.main()
