# generator.py
import openai

class TextGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key  # Устанавливаем API-ключ

    def generate_text(self, topic, style, length, language):
        """Генерирует текст в зависимости от темы, стиля, длины и языка."""
        # Настройка промпта в зависимости от выбранного языка
        if language == "английский":
            prompt_prefix = "Write a formal article about" if style == "формальный" else "Write an advertising copy about"
            prompt = f"{prompt_prefix} {topic}."
        else:
            prompt_prefix = "Напишите формальную статью на тему" if style == "формальный" else "Создайте рекламный текст о"
            prompt = f"{prompt_prefix} {topic}."

        # Запрос к OpenAI API для генерации текста
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Используем модель GPT-3.5
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # Система
                {"role": "user", "content": prompt}  # Запрос пользователя
            ],
            max_tokens=length * 2,  # Преобразуем количество слов в токены (1 слово ≈ 2 токена)
            temperature=0.7,  # Температура генерации
            top_p=1.0,  # Кумулятивная вероятность
            frequency_penalty=0.0,  # Штраф за частоту
            presence_penalty=0.0,  # Штраф за присутствие
        )

        # Получаем текст из ответа
        text = response['choices'][0]['message']['content'].strip()
        return text
