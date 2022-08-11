from aiogram import types
from loader import dp
from keyboards import commands_default_keyboard
from keyboards import see_commands_default_keyboard
from keyboards import items_commands_kyeboard
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(text=['привет', 'Привет', 'Начать'])  # Message_handler - обрабатывет сообщения
@dp.message_handler(commands=['start'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'''
Привет, {message.from_user.first_name}!\n 
Добро пожаловать в Магазин эстетичного текстиля собственного производства для малышей .\n
Действительно нужные товары из натуральных дышащих гиппоаллергенных материалов.\n
(/help - для просмотра доступных команд)
    ''',
                         reply_markup=see_commands_default_keyboard)


@dp.message_handler(text=['Показать меню', 'Назад'])
@dp.message_handler(commands=['help'])
async def answer_help_command(message: types.Message):
    await message.answer(text='Список, доступных комманд представлен в меню',
                         reply_markup=commands_default_keyboard)


@dp.message_handler(text=['Каталог'])
@dp.message_handler(commands=['items'])
async def answer_items_command(message: types.Message):
    # items = ['Пледы', 'Одеяла', 'Пеленки', 'Полотенца', 'Аксессуары']
    # i = 1
    # text = ''
    # for item in items:
    #     text += f'\n {i}- {item}'
    #     i += 1
    await message.answer(text=f'Выбери интересующий тебя раздел',
                         reply_markup=items_commands_kyeboard)


@dp.message_handler(commands=['add'])
async def answer_items_command(message: types.Message):
    await message.answer(text=f'''
    Данный раздел в разработке...
    ''')


@dp.message_handler(text=['Наши контакты'])
async def answer_items_command(message: types.Message):
    await message.answer(text=f'''
instagram (запрещенная в России организация): 
https://instagram.com/heyma.ru?igshid=YmMyMTA2M2Y=
Место нахождения: г. Обнинск, Калужская область
     ''')


@dp.message_handler(text=['Скрыть меню'])
async def answer_items_command(message: types.Message):
    await message.answer(text='Я скрыл меню',
                         reply_markup=see_commands_default_keyboard)


@dp.message_handler(content_types=['location'])
async def answer_items_command(message: types.Message):
    print(message)
    if message.from_user.id == message.contact.user_id:
        await message.answer(text=f'Спасибо! Теперь мне известно твое местоположение :)',
                             reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text=f'А это чей телефон?',
                             reply_markup=ReplyKeyboardRemove())


@dp.message_handler()
async def answer_items_command(message: types.Message):
    await message.answer(text=f'Я пока такой команды не знаю :(')


