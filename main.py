from os import system
from api_call import Command_Generator

print('''Welcome to SuperTerminal! For quick navigation:
 - Enter 'q' to quit.\n''')

User_prompt = input("$ ")

while User_prompt.lower() != "q":
    Terminal_Command = Command_Generator(User_prompt)
    print(f"Command: {Terminal_Command}")

    system(Terminal_Command)

    User_prompt = input("$ ")
