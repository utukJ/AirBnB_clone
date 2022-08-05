#!/usr/bin/python3

"""Console for airbnb"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) " 

    def do_quit(self, arg):
        """exit the console. Usage: quit"""
        return True
    
    def do_EOF(self, arg):
        """same as quit"""
        return self.do_quit(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()