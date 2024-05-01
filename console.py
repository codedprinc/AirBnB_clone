#!/usr/bin/python3
"""
Module : console.py
Console 0.0.1

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command processor for the hbnb 's console.
    """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF
        Closes the console"""
        return True

    def do_quit(self, line):
        """quit
        Closes the console"""
        return True
    def emptyline(self):
        """do nothing when an
        Empty line or ENTER key is entered"""
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
