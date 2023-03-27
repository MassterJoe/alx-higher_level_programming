#!/usr/bin/python3
"""
Defines a base model class.
"""
import json


class Base:
    """Base model.
    This represents the base for all other classes in this project
    Private class attributes:
        __nb_objects (int): Number of instantiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initailize a new base.
        args:
            id (int): identity of the new base
        """

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """It returns the json string representation
        of list_dictionaries
        args: list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        it writes the json string representation of list_objs
        to a file
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = []
                for i in list_objs:
                    list_dict = [i.to_dictionary()]
                    list_dicts += list_dict
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_to_string(json_string):
        """
        It returns a json string representation of a list
        of dicionaries
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)
