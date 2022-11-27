#!/usr/bin/env python3
# city.py

""" Defines the City Class """
from models.base_model import BaseModel


class City(BaseModel):
    """ Iherits from BaseModel class

        Attributes:
            state_id(str): id of state <State.id>
            name(str): name of city

    """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initialises the class City

            Args:
                args(tuple): Not used
                kwargs(dictionary): Dictionary representation of class
        """
        super().__init__(**kwargs)
