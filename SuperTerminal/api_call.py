import platform
from groq import Groq
from .error_handler import Client_Error

# replace 'your_api_key' with your Groq actual API key
client = Groq(api_key='your_api_key')

def Command_Generator(Prompt):

    System_Prompt = f"You are a {str(platform.platform())} terminal expert who only provides the exact command for a given task. Do not provide any explanations or additional information, only the command. Make sure your response is in the format of text."

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
    try:
        Command_Text = ""
        for chunk in completion:
                chunk_content = chunk.choices[0].delta.content or ""
                Command_Text += chunk_content

        return Command_Text

    except:
        error = completion.response
        if error == Client_Error.Error_400.value:
            print("The server could not understand the request due to invalid syntax. Review the request format and ensure it is correct.")
        elif error == Client_Error.Error_404.value:
            print("The requested resource could not be found. Check the request URL and the existence of the resource.")
        elif error == Client_Error.Error_422.value:
            print("The request was well-formed but could not be followed due to semantic errors. Verify the data provided for correctness and completeness.")
        elif error == Client_Error.Error_429.value:
            print("Too many requests were sent in a given timeframe. Implement request throttling and respect rate limits.")
