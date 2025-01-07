import aiogram
from aiogram.filters import Command
from aiogram.types import Message

__all__ = [
    "router"
]
router = aiogram.Router(name="auth-router")


@router.message(Command(commands=['auth'])) # /auth
async def auth_handler(message: Message) -> None:
    """
    This handler receives messages with /auth command
    """
    # Получаем текст теста из команды
    test_text = ' '.join(message.text.split()[1:])

    if not test_text:
        await message.answer('Пожалуйста, укажите текст теста после команды /auth')
        return

    # Вызываем функцию для обработки теста
    result = process_test(test_text)

    if result is not None:
        await message.answer(f'Результат: {result}')
    else:
        await message.answer('Ошибка: введенный текст не является числом.')

def process_test(test_text: str) -> int:
    try:
        # Пытаемся преобразовать текст в число
        number = float(test_text)
        # Умножаем число на 4
        result = number * 4
        return result
    except ValueError:
        # Если преобразование не удалось, возвращаем None
        return None

