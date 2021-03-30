#!/usr/bin/python3
""" Console Test Module """
import cmd
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class test_console(unittest.TestCase):
    """test cases for console"""

    def test_help_create(self):
        """tests help of create method"""
        answer = "Creates a class of any type\n[Usage]: create <className>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(answer, f.getvalue().strip())

    def test_create_error(self):
        """tests error message appear when incorrect create"""
        answer = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Potato")
            self.assertEqual(answer, f.getvalue().strip())
