#!/usr/bin/python3
"""
Models
"""
import cmd
import sys
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
import re
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb) '
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
            print(eval(command).id)
            storage.save()

    def do_show(self, line):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]

        if command is None:
            print("** class name missing **")
        elif command not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            data = storage.all().get(command + '.' + arg)
            if data is None:
                print("** no instance found **")
            else:
                print(data)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]

        if command is None:
            print("** class name missing **")
        elif command not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            key = command + '.' + arg
            data = storage.all().get(key)
            if data is None:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        command = self.parseline(line)[0]
        objs = storage.all()

        if command is None:
            print([str(objs[obj]) for obj in objs])
        elif command not in self.classes:
            key = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        """
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                storage.save()

    def analyze_parameter_value(self, value):
        """Checks a parameter value for an update
        Analyze if a parameter is a string that needs
        convert to a float number or an integer number.

        Args:
            value: The value to analyze

        """
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)

        return value


if __name__ == '__main__':
    shell = HBNBCommand()

# <<<<<<< HEAD

# =======

# >>>>>>> e3fa2e2357489c2fccf2f78c932f93a86bc26afc

    if not sys.stdin.isatty():
        for line in sys.stdin:
            shell.onecmd(line.strip())
    else:
        HBNBCommand().cmdloop()
