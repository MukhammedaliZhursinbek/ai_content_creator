import argparse
import os
from src.generator import TextGenerator
from src.utils import validate_input
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

MAX_WORDS = 500  # Устанавливаем максимальное количество слов


def parse_args():
    parser = argparse.ArgumentParser(description="Генератор контента с использованием ИИ")
    parser.add_argument('--topic', type=str, help="Тема для генерации контента")
    parser.add_argument('--style', type=str, choices=['рекламный', 'формальный', 'разговорный'], help="Стиль текста")
    parser.add_argument('--length', type=int, help="Длина текста в словах")
    return parser.parse_args()


def interactive_input():
    print("Выберите вашу тему:")
    topic = input("Тема: ")

    print("Выберите стиль:")
    style = input("Стиль (рекламный, формальный, разговорный): ")

    while True:
        try:
            length = int(input(f"Количество слов (до {MAX_WORDS}): "))
            if 0 < length <= MAX_WORDS:
                break
            else:
                print(f"Введите число от 1 до {MAX_WORDS}.")
        except ValueError:
            print("Введите целое число.")

    return topic, style, length


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Не найден API-ключ. Установите OPENAI_API_KEY в .env.")

    args = parse_args()

    if not args.topic or not args.style or not args.length:
        topic, style, length = interactive_input()
    else:
        topic = args.topic
        style = args.style
        length = args.length

    try:
        validate_input(topic, style, length)

        # Просто формирование промпта без языка
        if style == "формальный":
            prompt_prefix = "Напишите формальную статью на тему"
        elif style == "рекламный":
            prompt_prefix = "Создайте рекламный текст о"
        else:
            prompt_prefix = "Напишите разговорный текст на тему"

        prompt = f"{prompt_prefix} {topic}."

        generator = TextGenerator(api_key)
        generated_text = generator.generate_text(topic, style, length)

        print("\nСгенерированный текст:")
        print(generated_text)

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()

