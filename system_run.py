from os import system
from const_var import Color

def System_Run(Command):
    response = system(Command).bit_count()
    if response == 1:
        system(f"sudo {Command}")
        print(Color.GRAY.value + "> sudo" + Command + Color.RESET.value)
