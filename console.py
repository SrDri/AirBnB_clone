#!/usr/bin/python3
""" Class console """
import cmd
import shlex
import readline
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage = models.storage


class HBNBCommand(cmd.Cmd):
    """ class HBNB """

    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "Place", "Amenity", "Review",
               "City", "State"]

    def do_create(self, arg):
        """ Create instance """
        arg = shlex.split(arg)

        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] == "BaseModel":
            new_model = BaseModel()
            print(new_model.id)
            storage.new(new_model)
        elif arg[0] == "User":
            new_model = User()
            print(new_model.id)
            storage.new(new_model)
        elif arg[0] == "State":
            new_model = State()
            print(new_model.id)
            storage.new(new_model)
        elif arg[0] == "City":
            new_model = City()
            print(new_model.id)
            storage.new(new_model)
        elif arg[0] == "Amenity":
            new_model = Amenity()
            print(new_model.id)
            storage.new(new_model)
        elif arg[0] == "Place":
            new_model = Place()
            print(new_model.id)
            storage.new(new_model)
        elif arg[0] == "Review":
            new_model = Review()
            print(new_model.id)
            storage.new(new_model)
        else:
            print("** class doesn't exist **")
            return
        storage.save()

    def do_show(self, arg):

        arg = shlex.split(arg)

        if len(arg) < 1:
            print("** class name missing **")
            return
        if not arg[0] in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
        else:
            obj = storage.find_object(arg[1])
            if obj is None or obj.__class__.__name__ != arg[0]:
                print("** no instance found **")
            else:
                print(str(obj))

    def do_destroy(self, arg):
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
        else:
            if arg[0] in self.classes:
                if len(arg) < 2:
                    print("** instance id missing **")
                else:
                    try:
                        del storage.all()[arg[0] + "." + arg[1]]
                        storage.save()
                    except:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        arg = shlex.split(arg)
        object_dict = storage.all()
        list_print_all = []
        if len(arg) < 1:
            for id_obj in object_dict.keys():
                obj = object_dict[id_obj]
                list_print_all.append("{}".format(obj))
            print(list_print_all)
        else:
            if arg[0] in self.classes:
                for id_obj in object_dict:
                    if arg[0] in id_obj:
                        obj = object_dict[id_obj]
                        list_print_all.append("{}".format(obj))
                print(list_print_all)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
            return
        if not arg[0] in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        obj = storage.find_object(arg[1])
        if obj:
            if len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                setattr(obj, arg[2], arg[3])
                storage.save()
        else:
            print("** no instance found **")

    def do_count(self, arg):
        """print number instance"""
        arg = shlex.split(arg)

        if len(arg) < 1:
            print("** class name missing **")
            return
        count = 0
        objects = storage.all()
        for key in objects:
            if objects[key].__class__.__name__ == arg[0]:
                count += 1
        print(count)

    def default(self, line):
        """ function setup """
        lista_metodos = ["count", "all", "show", "destroy", "update"]

        name_clase = line.split(".", 1)
        if len(name_clase) < 2:
            print("** Unknown syntax:", line)
            return
        if name_clase[0] not in self.classes:
            print("** class doesn't exist **")
            return
        name_method = name_clase[1].split("(", 1)
        if name_method[0] not in lista_metodos or len(name_method) < 2:
            print("** Unknown syntax:", line)
            return
        name_method[1] = name_method[1].strip()
        if len(name_method[1]) < 1 or name_method[1][-1] != ')':
            print("** Unknown syntax:", line)
            return
        args = name_method[1][:-1]
        print("### {} ###".format(name_method[1][:-1]))
        if name_method[0] == "show":
            return self.do_show(name_clase[0] + " " + args)
        if name_method[0] == "all":
            return self.do_all(name_clase[0])
        if name_method[0] == "destroy":
            return self.do_destroy(name_clase[0] + " " + args)
        if name_method[0] == "count":
            return self.do_count(name_clase[0])

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return 1

    def do_EOF(self, arg):
        """exit the shell"""
        print()
        return 1

    def emptyline(self):
        """empty line"""
        return 0


if __name__ == '__main__':
    HBNBCommand().cmdloop()
