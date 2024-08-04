from api_call import Command_Generator
from system_run import System_Run

print('''Welcome to SuperTerminal!\n''')

User_prompt = input("$ ")

GRAY = "\033[38;5;8m"
RESET = "\033[0m"

while User_prompt.lower() != "q":
    Terminal_Command = Command_Generator(User_prompt)
    print(GRAY + "> " + Terminal_Command + RESET)
    System_Run(Terminal_Command)
    User_prompt = input("$ ")
