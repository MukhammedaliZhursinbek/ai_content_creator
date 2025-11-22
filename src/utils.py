# utils.py

def validate_input(topic, style, length):
    """Проверяет корректность входных данных."""
    if not topic:
        raise ValueError("Тема не может быть пустой")
    if style not in ["рекламный", "формальный", "разговорный"]:
        raise ValueError("Недопустимый стиль. Доступные стили: 'рекламный', 'формальный', 'разговорный'")
    if length <= 0:
        raise ValueError("Длина текста должна быть положительным числом")
        
def get_max_word_limit():
    """Возвращает максимальное количество слов для генерации."""
    return 500
