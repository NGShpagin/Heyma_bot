from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗂 Главное меню'),
            # KeyboardButton(text='Каталог'),
            # KeyboardButton(text='/add')
        ],
        [
            KeyboardButton(text='🛍 Моя корзина'),
            # KeyboardButton(text='Каталог'),
            # KeyboardButton(text='/add')
            KeyboardButton(text='📝 Оставить отзыв'),
        ],
        [
            KeyboardButton(text='☎ Поделиться \nконтактом',
                           request_contact=True),
            KeyboardButton(text='🌏 Поделиться \nгеопозицией',
                           request_location=True)
        ]
        # [
        #     KeyboardButton(text='Скрыть меню')
        # ]
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
            KeyboardButton(text='Назад в меню'),
        ]
    ],
    resize_keyboard=True
)