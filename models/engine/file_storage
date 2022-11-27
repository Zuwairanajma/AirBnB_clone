#!/usr/bin/python3
# file_storage.py

""" Defines the class FileStorage """

import json


class FileStorage:
    """Serialises instances to a JSON file and deserialises JSON
    file to instances

        Attributes:
            __objects: dictionary of objects
            __file_path: path of file where objects are stored in JSON format

    """
    __objects = {}
    __file_path = 'objects.json'

    def all(self):
        """ Returns the dictionary __objects """

        return type(self).__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.<obj id>

            Args:
                obj: object

        """
        obj_class_name = obj.__class__.__name__
        key = '{}.{}'.format(obj_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serialises the __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for k, v in type(self).__objects.items():
            obj_dict[k] = v.to_dict()

        with open(type(self).__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ Deserialises the JSON file to __objects only if JSON file exits.
            It does nothing otherwise
        """
        from models.base_model import BaseModel
        from models.state import State
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        try:
            with open(type(self).__file_path, 'r') as f:
                text = f.read()
                dict_text = json.loads(text)
                for k, v in dict_text.items():
                    type(self).__objects[k] = eval(
                        ''.join([k.split('.')[0], '(**v)']))
        except FileNotFoundError:
            pass
