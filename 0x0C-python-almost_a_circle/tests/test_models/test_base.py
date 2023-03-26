#!/usr/bin/python3
"""Defines unittests for base.py
unittest classes
    TestBase_instantiation
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase_instantiation(unittest.TestCase):
    """instantiation of the base class"""
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_uniqie_id(self):
        self.assertEqual(89, Base(89).id)

