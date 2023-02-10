#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
import re
from shlex import split

import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# CLI Global Constants
CLASSES = [
        "BaseModel",
        "User"
        ]

def parse(argv):
    """
    Convert argument input to argument tuple
    """
    moustache = re.search(r"\{(.*?)\}", argv)
    brac = re.search(r"\[(.*?)\]", argv)

    if moustache is None:
        if brac is None:
            return [i.strip(","), for i in split(argv)]
        else:
            lexer = split(argv[:brac.span()[0]])
            ret1 = [i.strip(",") for i in lexer]
            ret1.append(brac.group())
            return ret1
    else:
        lexer = split(argv[:moustache.span()[0]])
        ret1 = [i.strip(",") for i in lexer]
        ret1.append(moustache.group())
        return ret1

def args_checker(args):
    """ args checker to verify validity

    args (str): contains arguments passed to a command
    returns: error message if class name is missing or class name doesn't exist
    """
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] no in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list

class HBNBCommand(cmd.Cmd):
    """
    Class Implementing the console for AirBnB project
    """
    prompt = "(hbnb)"
    storage = models.storage

    # ---basic interpreter commands---
    def default(self, arg):
        """Default cmd module behaviour when input is invalid"""
        action_map = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "create": self.do_create,
                "update": self.do_update
                }

        match = re.search(r"\.", arg)
        if match:
            arg_1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.serach(r"\((.*?)\)", arg_1[1])
            if match:
                command = [arg_1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(arg_1[0], command[1])
                    return action_map[command[0]](call)
        
        print("*** Unknown syntax: {}".format(arg))
        return False

    def emptyline(self):
        """Command to be executed when empty line + ENTER key is hit"""
        pass

    def do_quit(self, argv):
        """Exit the program: QUIT"""
        print("Thank you for using hbnb CLI")
        return True

    def do_EOF(self, argv):
        """Exit the program: EOF"""
        print("Thank you for using hbnb CLI")
        return True

    def do_create(self, argv):
        """Creates new instance of the BaseModel, save it to JSON file and print the id: create BaseModel"""
        args = args_checker(argv)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, argv):
        """Print the string representation of an instance based on class name and id: show BaseModel 1234-1234-1234"""
        args = args_checker(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in self.storage.all():
                    print("** no instance found  **")
                else:
                    print(self.storage.all()[key])

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id(save the change to a JSON file): destroy BaseModel 1234-1234-1234-1234"""
        args_list = args_checker(argv)
        if args_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_list)
                if key in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def do_all(seld, argv):
        """Prints all string representation of all instances based or not on the class name: all BaseModel or all"""
        arg_list = split(argv)
        objects = self.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in CLASSES:
                print ("** class does not exist **")
            else:
                print([str(obj) for obj in objects if arg_list[0] in str(obj)])

    def do_update(self, argv):
        """Updates an instance based on the class name and id by adding or updating
        attribute(save the change into the JSON file): update BaseModel 1224-1234-1234-1234 email 'aibnb@mail.com'

        Usage:
            update <class name> <id> <attribute name> '<attribute value'
        """
        arg_list = arg_checker(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            value_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], value_type(arg_list[3])
                        else:
                        setattr(obj, arg_list[2], arg_list[3])
                 else:
                    print("** no instance found **")

        self.storage.save()

    def do_count(self, argv):
        """
        Retrieve the number of instances per class"""
        arg_1 = parse(argv)
        icount = 0

        for obj in models.storage.all().values():
            if arg_1[0] == type(obj).__name__:
                icount += 1
        print(icount)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
