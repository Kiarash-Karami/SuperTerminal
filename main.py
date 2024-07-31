from groq import Groq
from os import system


# replace 'your_api_key' with your Groq actual API key
client = Groq(api_key='your_api_key')

def Command_Generator(Prompt):

    System_Prompt = "You are a Mac terminal expert who only provides the exact command for a given task. Do not provide any explanations or additional information, only the command. Make sure your response is in the format of text."

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": System_Prompt
            },
            {
                "role": "user",
                "content": Prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    Command_Text = ""
    for chunk in completion:
            chunk_content = chunk.choices[0].delta.content or ""
            Command_Text += chunk_content
    return Command_Text


def System_Run(Command):
    system(Command)


print('''Welcome to SuperTerminal! For quick navigation:
 - Enter 'q' to quit.

Enjoy your experience!\n''')
User_prompt = input("$ ")

while User_prompt.lower() != "q":
    final_command = Command_Generator(User_prompt)
    print(f"Command: {final_command}")
    System_Run(final_command)

    User_prompt = input("$ ")
