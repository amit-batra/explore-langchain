"""
This module performs translation of text using LangChain backed by Google Gemini.
"""

def load_env() -> None:
    """
    Load the environment variables from the .env file.
    """
    try:
        from dotenv import load_dotenv

        # Load environment variables from .env file
        load_dotenv()
    except ImportError:
        print("Unable to load environment variables from .env file")

def get_api_key() -> str:
    """
    Get the API key for Google Gemini from the environment variables.
    If the API key is not set, prompt the user for it.
    """
    import getpass
    import os

    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")
    return os.environ.get("GOOGLE_API_KEY")

from langchain_core.language_models.chat_models import BaseChatModel
def load_model() -> BaseChatModel:
    """
    Load the model for Google Gemini.
    """
    from langchain.chat_models import init_chat_model

    model:BaseChatModel = init_chat_model("gemini-1.5-flash", model_provider="google_genai")
    return model

def translate_text(model:BaseChatModel, text:str) -> str:
    """
    Translate the given text using the model.
    """
    from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
    messages: list[BaseMessage] = [
        SystemMessage("Translate the following from English into French"),
        HumanMessage(text),
    ]
    return model.invoke(messages).content

def main() -> None:
    """
    Main function to perform translation of text using LangChain backed by Google Gemini.
    """
    load_env()
    get_api_key()
    model:BaseChatModel = load_model()

    user_prompt:str = "Enter the text to translate (or 'exit' to quit): ";
    text_to_translate:str = input(user_prompt)
    while (text_to_translate != "exit"):
        translated_text:str = translate_text(model, text_to_translate)
        print(translated_text)
        text_to_translate = input(user_prompt)

if __name__ == "__main__":
    main()