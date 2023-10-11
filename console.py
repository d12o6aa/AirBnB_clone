#!/usr/bin/python3
"""
Models
"""
import cmd
import sys
from datetime import datetime
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        empty lines
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
