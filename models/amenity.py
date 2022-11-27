menity.py

""" Defines the Amenity class """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Subclass of BaseModel class

        Args:
            name(str): name of the amenity

    """
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initialises the Amenity class

            Args:
                args(tuple): Not used
                kwargs(dictionary): Dictionary representation of instance

        """
        super().__init__(**kwargs)
