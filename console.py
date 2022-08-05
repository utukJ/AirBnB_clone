#!/usr/bin/python3

"""Console for airbnb"""

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) " 

    ClassNameMissing = "** class name missing **"
    ClassNotExist = "** class doesn't exist **"
    InstanceIDMissing = "** instance id missing **"
    NoInstanceFound = "** no instance found **"
    AttributeNameMissing = "** attribute name missing **"
    ValueMissing = "** value missing **"

    def do_create(self, line):
        """creates a new instance of a given class. Usage create <class_name>"""
        args = line.split()
        if not (class_name := self.validate_class_name(args)):
            return
        obj = eval(class_name)()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """shows an instance of a given class. Usage: show <class_name> <id>"""
        args = line.split()
        if not (class_name := self.validate_class_name(args)):
            return
        if not (id := self.validate_id(args)):
            return
        print(models.storage.all()[class_name + "." + id])

    def do_destroy(self, line):
        """destroys an instance of a given class. Usage destroy <class_name> <id>"""
        args = line.split()
        if not (class_name := self.validate_class_name(args)):
            return
        if not (id := self.validate_id(args)):
            return
        del models.storage.all()[class_name + "." + id]
        models.storage.save()

    def do_all(self, line):
        """shows all stored instances of a given class. Usage: all <class_name>"""
        args = line.split()
        if not (class_name := self.validate_class_name(args)):
            return
        instances = []
        for k, v in models.storage.all().items():
            if k.split(".")[0] == class_name:
                instances.append(str(v))
        print(instances)

    def do_update(self, line):
        """update instance. Usage: update <class_name> <id> <attribute> <value>"""
        args = line.split()
        if not (class_name := self.validate_class_name(args)):
            return
        if not (id := self.validate_id(args)):
            return
        if not (attr := self.validate_attr_name(args)):
            return
        if (val := self.validate_attr_value(args)) is None:
            return
        obj = models.storage.all()[class_name + "." + id]
        setattr(obj, attr, val)
        models.storage.save()

    @classmethod
    def validate_class_name(cls, args):
        if len(args) == 0:
            print(cls.ClassNameMissing)
            return
        try:
            mdl = eval(args[0])
        except NameError:
            print(cls.ClassNotExist)
            return
        return args[0]

    @classmethod
    def validate_id(cls, args):
        if len(args) < 2:
            print(cls.InstanceIDMissing)
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all().keys():
            print(cls.NoInstanceFound)
            return
        return args[1]
        
    @classmethod
    def validate_attr_name(cls, args):
        if len(args) < 3:
            print(cls.AttributeNameMissing)
            return
        return args[2]

    @classmethod
    def validate_attr_value(cls, args):
        if len(args) < 4:
            print(cls.ValueMissing)
            return
        return args[3]

    def do_quit(self, arg):
        """exit the console. Usage: quit"""
        return True
    
    def do_EOF(self, arg):
        """same as quit"""
        return self.do_quit(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()