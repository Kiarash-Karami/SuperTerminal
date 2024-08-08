import subprocess
from api_call import Command_Generator
from system_run import System_Run
from const_var import Color
from failed_command import Command_corrector

def Main_Run():

    print('''Welcome to SuperTerminal!\n''')

    User_prompt = input("$ ")


    while User_prompt.lower() != "q":
        Terminal_Command = str(Command_Generator(User_prompt))

        result = subprocess.run(Terminal_Command , shell=True, capture_output=True, text=True)
        New_Command = ""
        while result.returncode != 0:
            New_Command = str(Command_corrector(f"Command '{Terminal_Command}' failed with exit code {result.returncode}: {result.stderr}"))
            result = subprocess.run(New_Command , shell=True, capture_output=True, text=True)

        if New_Command == "":
            print(Color.GRAY.value + "> " + Terminal_Command + Color.RESET.value)
            System_Run(Terminal_Command)
        else:
            print(Color.GRAY.value + "> " + New_Command + Color.RESET.value)
            System_Run(New_Command)
        User_prompt = input("$ ")
