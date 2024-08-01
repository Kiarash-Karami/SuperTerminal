from os import system
from api_call import Command_Generator

print('''Welcome to SuperTerminal! For quick navigation:
 - Enter 'q' to quit.\n''')

User_prompt = input("$ ")

while User_prompt.lower() != "q":
    final_command = Command_Generator(User_prompt)
    print(f"Command: {final_command}")

    system(final_command)

    User_prompt = input("$ ")
