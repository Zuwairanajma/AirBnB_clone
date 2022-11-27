#!/usr/bin/env python3
# console.py

""" Entry point for the command interpreter """
import cmd
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Defines the HBNB class

        Inherits from Cmd class
    """
    prompt = '(hbnb) '

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id """
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "City": City}
        if arg is None or arg == '':
            print('** class name missing **')
        elif arg not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            obj = class_dict[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based
on the class name and id.
        """
        class_list = [
            "BaseModel",
            "User",
            "State",
            "Place",
            "Amenity",
            "Review",
            "City"]
        if arg is None or arg == '':
            print('** class name missing **')
        else:
            args = arg.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all().get(key, None)
                if obj is None:
                    print("** no instance found **")
                else:
                    print(obj)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file)

            Usage:
                destroy <name of class> <id of object>
        """
        class_list = [
            "BaseModel",
            "User",
            "State",
            "Place",
            "Amenity",
            "Review",
            "City"]
        if arg is None or arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all().get(key, None)
                if obj is None:
                    print("** no instance found **")
                else:
                    storage.all().pop(key)
                    storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based
        or not on the class name.

            Usage:
                all - prints all objects
                all <class name> - prints all instances of <class name>
        """
        class_list = [
            "BaseModel",
            "User",
            "State",
            "Place",
            "Amenity",
            "Review",
            "City"]
        if arg is None or arg == '':
            for k, v in storage.all().items():
                print(v)
        else:
            if arg in class_list:
                for k, v in storage.all().items():
                    class_name = k.split('.')
                    if class_name[0] == arg:
                        print(v)
                    else:
                        pass
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by
        adding or updating attribute(save the chaneg into the JSON file)

            Usage:
                update <class name> <id> <attribute name> "<attribute value>"
        """
        class_list = [
            "BaseModel",
            "User",
            "State",
            "Place",
            "Amenity",
            "Review",
            "City"]
        if arg is None or arg == '':
            print("** class name missing **")
        else:
            args = arg.split(maxsplit=3)
            if args[0] not in class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all().get(key, None)
                if obj is None:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                else:
                    value = obj.__dict__.get(args[2], None)
                    if value is None:
                        print("** value missing **")
                    else:
                        new_val = args[3].split("\"")
                        if len(new_val) != 3 or new_val[2] != '':
                            pass
                        else:
                            obj.__dict__[args[2]] = new_val[1]
                            obj.save()

    def do_EOF(self, arg):
        """ Press ^D(Control + D) to exit the program """
        print('\n')
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ Called when an empty line is entered in the prompt
        If the method is not overridden, it repeates the last
        non-empty command entered.
        Another Implementation:
        if self.lastcmd:
            self.lastcmd = ''
            return self.onecmd("\n")
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
