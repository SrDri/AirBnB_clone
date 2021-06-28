#!/usr/bin/python3
""" Class console """
import cmd
import readline


class HBNBCommand(cmd.Cmd):
    """ class HBNB """

    prompt = '(hbnb) '

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
