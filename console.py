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
            data = models.storage.all().get(command + '.' + arg)
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
            data = models.storage.all().get(key)
            if data is None:
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        command = self.parseline(line)[0]
        objs = models.storage.all()

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
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
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
                models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
