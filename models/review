#!/usr/bin/env python3
# review.py

""" Defines Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Subclass of BaseModel

        Attributes:
            place_id (string): conatain the Place.id
            user_id (string): contains the User.id
            text (string): Review is writen here

    """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """ Initialises the Review Class

            Args:
                args(tuple): Not used
                kwargs (dictionary): Dictionary representation of an object

        """
        super().__init__(**kwargs)
