#!/usr/bin/python3
"""
Defines a base model class.
"""


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
