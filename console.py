#!/usr/bin/python3
"""

Module : console.py
Console 1.0


"""
import re
import models
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command processor for the hbnb 's console.
    """

    present_classes = ["BaseModel"]
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

    def do_create(self, clss):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if clss in models.storage.classes():
            clss = models.storage.classes()[clss]()
            clss.save()
            print(clss.id)
        elif clss is None or clss == "":
            print("** class name missing **")
        elif clss not in self.present_classes:
            print("** class doesn't exist **")

    def help_create(self):
        print('\n'.join([ 'create <class name>',
                          '<id> -- id of the class made is printed out']))

    def do_show(self, clss):
        """
        Prints the string representation
        of an instance based on the class name and id
        """
        if clss == "" or clss is None:
            print("** class name missing **")
        else:
            words = clss.split(' ')
            if words[0] not in models.storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    print(models.storage.all()[key])

    def help_show(self):
        print('\n'.join([ 'show <class name> <class.id>',
                          '--- prints out a string of the instance']))

    def do_destroy(self, clss):
        """
        Deletes an instance based on
        the class name and id (save the change into the JSON file).
        """
        if clss == "" or clss is None:
            print("** class name missing **")
        else:
            words = clss.split(' ')
            if words[0] not in models.storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    del models.storage.all()[key]
                    models.storage.save()


    def help_destroy(self):
        print('\n'.join([ 'destroy <class name> <class.id>',
                          ' ']))

    def do_all(self, clss):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all.
        """
        if clss != "":
            words = clss.split(' ')
            if words[0] not in models.storage.classes():
                print("** class doesn't exist **")
            else:
                ln = [str(obj) for k, obj in models.storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(ln)
        else:
            n_list = [str(obj) for k, obj in models.storage.all().items()]
            print(n_list)

    def help_all(self):
        print('\n'.join([ 'all <class name>',
                          '--prints all string representationof all instances'
                          , 'based or not on the same class']))

    def do_update(self, clss):
        """
         Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        if clss == "" or clss is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, clss)
        cls_name = match.group(1)
        u_id = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if not match:
            print("** class name missing **")
        elif cls_name not in models.storage.classes():
            print("** class doesn't exist **")
        elif u_id is None:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(cls_name, u_id)
            if k not in models.storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = models.storage.attributes()[cls_name]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(models.storage.all()[k], attribute, value)
                models.storage.all()[k].save()

    def help_update(self):
        print('\n'.join([
            'update <class name> <id> <attribute name> "<attribute value>',
                          '//updates an instance ...']))



if __name__ == '__main__':
    HBNBCommand().cmdloop()
