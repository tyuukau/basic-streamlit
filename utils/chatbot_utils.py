from hugchat import hugchat
from hugchat.login import Login
from hugchat.message import Message


def generate_response(prompt_input: str, email: str, passwd: str) -> Message:
    """
    Generates a response from the chatbot based on the given prompt input.

    Args:
        prompt_input (str): The input prompt for the chatbot.
        email (str): The email address used for Hugging Face login.
        passwd (str): The password used for Hugging Face login.

    Returns:
        Message: The response generated by the chatbot.
    """
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)
