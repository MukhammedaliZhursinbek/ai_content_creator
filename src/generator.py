# generator.py
import openai

class TextGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key  # Устанавливаем API-ключ

    def generate_text(self, topic, style, length):
        """Генерирует текст в зависимости от темы, стиля и длины."""

        # Формирование промпта без учета языка
        if style == "формальный":
            prompt = f"Напишите формальную статью на тему {topic}."
        elif style == "рекламный":
            prompt = f"Создайте рекламный текст о {topic}."
        else:
            prompt = f"Напишите разговорный текст на тему {topic}."

        # Запрос к OpenAI API для генерации текста
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Вы — помощник, который пишет текст строго на русском языке."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=length * 2,  # Примерное соответствие слов и токенов
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        # Извлечение текста
        text = response['choices'][0]['message']['content'].strip()
        return text


