#!/usr/bin/python3
"""
Models
"""
import cmd
import sys
from datetime import datetime
import models
from models.base_model import BaseModel
#from models.user import User
#from models.state import State
#from models.city import City
#from models.amenity import Amenity
#from models.place import Place
#from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb)'
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

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

    def do_create(self, line):
        """
         Creates a new instance of BaseModel
        """
        command = self.parseline(line)[0]
        if command is None:
            print("** class name missing **")
        elif command not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)
            new_obj.save()
            print(new_obj.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
