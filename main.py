# main.py
import argparse
from src.generator import TextGenerator
from src.utils import validate_input, get_max_word_limit
from src.config import load_api_key

def parse_args():
    """Парсинг аргументов командной строки."""
    parser = argparse.ArgumentParser(description="Генератор контента с использованием ИИ")
    parser.add_argument('--topic', type=str, help="Тема для генерации контента")
    parser.add_argument('--style', type=str, choices=['рекламный', 'формальный', 'разговорный'], help="Стиль текста")
    parser.add_argument('--length', type=int, help="Длина сгенерированного контента в словах")
    parser.add_argument('--language', type=str, choices=['русский', 'английский'], help="Язык текста")
    return parser.parse_args()

def interactive_input():
    """Интерактивный ввод для темы, стиля, длины текста и языка."""
    print("Выберите вашу тему:")
    topic = input("Тема (например, 'Как искусственный интеллект меняет маркетинг'): ")

    print("Выберите ваш стиль:")
    style = input("Стиль (рекламный, формальный, разговорный): ")

    # Ввод количества слов с ограничением
    while True:
        try:
            length = int(input(f"Количество слов (максимум {get_max_word_limit()}): "))
            if length <= 0:
                print("Количество слов должно быть положительным числом.")
            elif length > get_max_word_limit():
                print(f"Количество слов не может превышать {get_max_word_limit()}. Попробуйте снова.")
            else:
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    return topic, style, length, language

def main():
    """Основная функция, которая запускает генерацию контента."""
    try:
        # Загружаем API-ключ
        api_key = load_api_key()

        # Парсим аргументы командной строки
        args = parse_args()

        # Если аргументы не переданы, используем интерактивный ввод
        if not args.topic or not args.style or not args.length or not args.language:
            topic, style, length, language = interactive_input()
        else:
            topic = args.topic
            style = args.style
            length = args.length
            language = args.language

        # Валидация входных данных
        validate_input(topic, style, length)

        # Инициализация генератора текста
        generator = TextGenerator(api_key)

        # Генерация текста
        generated_text = generator.generate_text(topic, style, length, language)

        # Вывод сгенерированного текста
        print("\nСгенерированный текст:")
        print(generated_text)

        print(f"\nЯзык текста: {language.capitalize()}")

    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
