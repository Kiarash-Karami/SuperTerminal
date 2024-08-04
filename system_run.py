from os import system

def System_Run(Command):
    response = system(Command)
    if response == 0:
        system(Command)
    elif response == 256:
        system(f"sudo {Command}")
