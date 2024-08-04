from api_call import Command_Generator
from system_run import System_Run

print('''Welcome to SuperTerminal! For quick navigation:
 - Enter 'q' to quit.\n''')

User_prompt = input("$ ")

while User_prompt.lower() != "q":
    Terminal_Command = Command_Generator(User_prompt)
    System_Run(Terminal_Command)
    User_prompt = input("$ ")
