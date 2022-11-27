#!/usr/bin/env python3
# base_models.py
""" Defines BaseModel class """

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Initializes the BaseModel objeect

            Args:
                args(tuple): Not used
                kwargs (dictionary): dictionary representation
        """
        if (kwargs is None or len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':

                        self.__dict__[k] = datetime.fromisoformat(v)
                    else:
                        self.__dict__[k] = v

    def save(self):
        """ Updates the public instance attribute `updated_at`"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dic containing all items of __dict__ of the instance.

            Note: created_at and updated_at must be converted to
            string objects in ISO format.
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["updated_at"] = self.updated_at.isoformat()
        base_dict["created_at"] = self.created_at.isoformat()
        return (base_dict)

    def __str__(self):
        """ Overrides the __str__ method and return human readable
        information about object.

            Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
                                    self.__class__.__name__,
                                    self.id, self.__dict__)
