#!/usr/bin/env python3
# user.py

""" Defines the User Class """

from models.base_model import BaseModel


class User(BaseModel):
    """ Inherits from BaseModel and defines a user object """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """ Initialises the User object

            Args:
                args: Not used
                kwargs: dictionary representation of the object
        """
        super().__init__(**kwargs)

