# config.py
import os
from dotenv import load_dotenv

def load_api_key():
    """Загружает API-ключ из переменных окружения."""
    load_dotenv()  # Загружаем переменные из .env
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Необходимо указать API-ключ. Установите его в переменную окружения OPENAI_API_KEY.")
    return api_key
