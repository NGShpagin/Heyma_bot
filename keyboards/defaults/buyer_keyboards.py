from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='Каталог'),
            KeyboardButton(text='/add')
        ],
        [
            KeyboardButton(text='Поделиться контактом',
                           request_contact=True),
            KeyboardButton(text='Поделиться геопозицией',
                           request_location=True)
        ],
        [
            KeyboardButton(text='Наши контакты')
        ],
        [
            KeyboardButton(text='Скрыть меню')
        ]
    ],
    resize_keyboard=True
)

see_commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Показать меню')
        ]
    ],
    resize_keyboard=True
)

items_commands_kyeboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пледы'),
            KeyboardButton(text='Одеяла'),
            KeyboardButton(text='Пеленки'),
        ],
        [
            KeyboardButton(text='Полотенца'),
            KeyboardButton(text='Аксессуары'),
        ],
        [
            KeyboardButton(text='Назад'),
        ]
    ],
    resize_keyboard=True
)