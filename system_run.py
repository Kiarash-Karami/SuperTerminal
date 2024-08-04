from os import system

def System_Run(Command):
    response = system(Command).bit_count()
    if response == 1:
        system(f"sudo {Command}")
