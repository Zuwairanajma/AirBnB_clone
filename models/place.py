#!/usr/bin/env python3
# place.py

""" Defines the Place Class """

from models.base_model import BaseModel


class Place(BaseModel):
    """ Subclass of BaseModel

        Attributes:
            city_id (str): Contains City.id
            user_id (str): Contains User.id
            name (str): name of place
            description (str): description of place
            number_rooms (int): number of rooms
            number_bathrooms (int): number of bathrooms
            max_guest (int): max number of guests
            price_by_night (int): price per night
            latitude (float): latitude value of the place
            longitude (float): longitude value of the place
            amenity_ids (list of string): list of Amenity.id

    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Initialises the class Place

            Args:
                *args(tuple): Not Used
                **kwargs (dictionary): dictionary of objects

        """
        super().__init__(**kwargs)
