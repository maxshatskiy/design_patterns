""" Command design pattern.
From Ayeva:

Helps encapsulate an operation (undo, redo, copy, paste, etc...) as an object. We create a class that contains
all the logic and the methods required to implement the operation. The advantages of doing this are as follows:
1. The object that invokes command is decoupled from the obejct that knows how to perform it. The invoker does not
need to know any implementation details about the command.
2. Multiple commands can be grouped that allow invoker to execute them in order.

Use cases:
1. Undo command
2. Actions on buttons and menu items
3. Cut, copy, paste, redo, capitalize text
4. Transactional behaviour and logging
5. Sequence of actions that an be recorded and executed on demand at any point in time.
In general, any operation that can be executed at the user's will at runtime is a good candidate to use the Command
pattern.
"""
import os
verbose = True
class RenameFile:

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        if verbose:
            print(f"[renaming '{self.src}' to '{self.dest}'")
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print(f"[renaming '{self.dest}' to '{self.src}'")
        os.rename(self.dest, self.src)

def delete_file(path):
    if verbose:
        print(f"deleting file {path}")
    os.remove(path)

class CreateFile:

    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        try:
            delete_file(self.path)
        except:
            print('delete action not sucessful...')
            print('... file was probably already deleted.')

class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print(f"[reading file '{self.path}']")
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')

def main():
    orig_name, new_name = 'file1', 'file2'
    commands = (
        CreateFile(orig_name),
        ReadFile(orig_name),
        RenameFile(orig_name, new_name)
    )
    [c.execute() for c in commands]

    answer = input('reverse the executed command? [y/n]')
    if answer not in 'yY':
        print(f"the result is {new_name}")
        exit()
    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            print("Error", str(e))

"""From Dusty Phillips. The command pattern adds a level of abstraction between actions that must be done and 
the object that invokes those actions, normally later at a time. The client code creates a Command object that 
can be executed at a later data. The obeject knows about a reciever object that manages its own internal state when
the command is executed on it. The command object implements a specific interface, e.g. execute(). Invoker objects
execute command at the correct time."""


if __name__=="__main__":
    main()