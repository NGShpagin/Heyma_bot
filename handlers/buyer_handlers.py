from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hbold, hunderline, hitalic
from loader import dp, bot, data_manager
from keyboards import commands_default_keyboard
from keyboards import see_commands_default_keyboard
from keyboards import items_commands_kyeboard
from keyboards import start_inline_keyboard, get_items_inline_keyboards, main_inline_keyboard, \
    categories_inline_keyboard, my_cart_inline_keyboards
from keyboards import start_callback, navigation_callback, main_callback, items_callback, blanket_callback, \
    shroud_callback, plaid_callback, accessories_callback, categories_callback, store_callback, search_callback, \
    remove_callback
from aiogram.types import ReplyKeyboardRemove
from states import BuyerState
import json


@dp.message_handler(text=['привет', 'Привет', 'Начать'])  # Message_handler - обрабатывет сообщения
@dp.message_handler(commands=['start'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Привет, {hbold(message.from_user.first_name)}! 👋\n'
                              f'Добро пожаловать в Магазин эстетичного текстиля собственного производства для малышей 👶🏼\n'
                              f'Действительно нужные товары из натуральных дышащих гиппоаллергенных материалов.\n',
                         reply_markup=start_inline_keyboard)
    await message.answer(
        text='Чтобы, перейти в Главное меню нажмите на кнопку выше или воспользуйтесь встроенной клаиатурой',
        reply_markup=commands_default_keyboard)
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)


@dp.message_handler(commands=['main_menu', 'menu'])
@dp.message_handler(text='🗂 Главное меню')
async def answer_main_menu(message: types.Message):
    await message.answer(text='🗂 Главное меню',
                         reply_markup=main_inline_keyboard)


@dp.callback_query_handler(main_callback.filter())
async def call_main_menu(call: types.CallbackQuery):
    await call.message.answer(text='Главное меню',
                              reply_markup=main_inline_keyboard)
    await bot.delete_message(chat_id=call.message.chat.id,
                             message_id=call.message.message_id)


@dp.callback_query_handler(categories_callback.filter())
async def answer_categories_command(call: types.CallbackQuery):
    await call.message.answer(text='Категории товаров',
                              reply_markup=categories_inline_keyboard)
    await bot.delete_message(chat_id=call.message.chat.id,
                             message_id=call.message.message_id)


@dp.message_handler(text=['Показать меню', 'Назад в меню'])
@dp.message_handler(commands=['help', 'menu'])
async def answer_help_command(message: types.Message):
    await message.answer(text='В меню показано то, что я сейчас умею :)',
                         reply_markup=commands_default_keyboard)


@dp.callback_query_handler(blanket_callback.filter())
async def answer_blanket_callback(call: types.CallbackQuery):
    status, item_info = data_manager.get_item(0, 'blankets', 'database/data/items.json')
    item_text = f'{item_info["id"]}' \
                f'\nНазвание товара: {item_info["name"]}' \
                f'\nСтатус: {item_info["status"]}' \
                f'\nКоличество товара: {item_info["amount"]}'
    await call.message.answer(text=item_text,
                              reply_markup=get_items_inline_keyboards())
    await bot.delete_message(chat_id=call.message.chat.id,
                             message_id=call.message.message_id)


@dp.callback_query_handler(search_callback.filter())
async def get_item_name(call: types.CallbackQuery):
    await call.message.answer('Введите название товара')
    await BuyerState.wait_item_name.set()


@dp.message_handler(state=BuyerState.wait_item_name)
async def get_item_name(message: types.Message, state: FSMContext):
    item_info = data_manager.search_items_by_name(message.text)
    if item_info == 0:
        await state.reset_state()
        await message.answer(text='Товара с таким наименованием у нас нет :(')
    else:
        await state.reset_state()
        await message.answer(text=f'{item_info["id"]}' \
                                  f'\nНаименование товара: {item_info["name"]}' \
                                  f'\nСтатус: {item_info["status"]}' \
                                  f'\nКоличество товара: {item_info["amount"]}')


@dp.message_handler(text='📝 Оставить отзыв')
async def get_item_name(message: types.Message):
    await message.answer(text=f'{hbold("Вопрос 1 из 3")}'
                         '\nНасколько вы довольны нашим сервисом?')
    await BuyerState.first_question.set()


@dp.message_handler(state=BuyerState.first_question)
async def get_item_name(message: types.Message, state: FSMContext):
    answer_1 = message.text
    print(answer_1)
    await message.answer(text=f'{hbold("Вопрос 2 из 3")}'
                              '\nНасколько Вам понравился функционал нашего т-бота?')
    await state.update_data(answers=[answer_1])
    await BuyerState.second_question.set()


@dp.message_handler(state=BuyerState.second_question)
async def get_item_name(message: types.Message, state: FSMContext):
    answers = await state.get_data()
    answers['answers'].append(message.text)
    my_list = answers['answers']
    print(my_list)
    await message.answer(text=f'{hbold("Вопрос 3 из 3")}'
                              '\nЧто можно было бы улучшить?')
    await state.update_data(answers=my_list)
    await BuyerState.third_question.set()


@dp.message_handler(state=BuyerState.third_question)
async def get_item_name(message: types.Message, state: FSMContext):
    answers = await state.get_data()
    answers['answers'].append(message.text)
    my_list = answers['answers']
    print(my_list)
    user_id = message.from_user.id
    data_manager.save_anketa(user_id, my_list)
    await state.reset_state()
    await message.answer(text=f'Спасибо за Ваш отзыв!'
                              f'\nБудем рады видеть Вас снова!')


@dp.message_handler(text='🛍 Моя корзина')
async def see_my_cart(message: types.Message):
    user_id = message.from_user.id
    with open('database/data/cart.json', 'r') as file:
        items = json.load(file)
    status = 'Left_side'
    if str(user_id) in items[0]:
        if type(items[0][str(user_id)]) == list and len(items[0][str(user_id)]) > 1:
            status, item_info = data_manager.get_item(0, str(user_id), 'database/data/cart.json')
            item_text = f'{item_info["id"]}' \
                        f'\nНаименование товара: {item_info["name"]}' \
                        f'\nСтатус: {item_info["status"]}' \
                        f'\nКоличество на складе: {item_info["amount"]}'
        else:
            if type(items[0][str(user_id)]) == list and len(items[0][str(user_id)]) == 1:
                status = 0
                item_text = f'{items[0][str(user_id)][0]["id"]}' \
                            f'\nНаименование товара: {items[0][str(user_id)][0]["name"]}' \
                            f'\nСтатус: {items[0][str(user_id)][0]["status"]}' \
                            f'\nКоличество на складе: {items[0][str(user_id)][0]["amount"]}'
            else:
                status = -1
                item_text = 'Корзина пуста'
    else:
        item_text = 'Корзина пуста'
    await message.answer(text=item_text,
                         reply_markup=my_cart_inline_keyboards(status))
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)


@dp.callback_query_handler(remove_callback.filter())
async def remove_position(call: types.CallbackQuery):
    item_id = call.message.text.split('\n')[0]
    print(call)
    user_id = call.from_user.id
    data_manager.remove_pos(user_id, item_id)
    with open('database/data/cart.json', 'r') as file:
        items = json.load(file)
    status = 'Left_side'
    if str(user_id) in items[0]:
        if type(items[0][str(user_id)]) == list and len(items[0][str(user_id)]) > 1:
            status, item_info = data_manager.get_item(0, str(user_id), 'database/data/cart.json')
            item_text = f'{item_info["id"]}' \
                        f'\nНазвание товара: {item_info["name"]}' \
                        f'\nСтатус: {item_info["status"]}' \
                        f'\nКоличество на складе: {item_info["amount"]}'
        else:
            status = 0
            if type(items[0][str(user_id)]) == list:
                item_text = f'{items[0][str(user_id)][0]["id"]}' \
                            f'\nНазвание товара: {items[0][str(user_id)][0]["name"]}' \
                            f'\nСтатус: {items[0][str(user_id)][0]["status"]}' \
                            f'\nКоличество на складе: {items[0][str(user_id)][0]["amount"]}'
            else:
                item_text = f'{items[0][str(user_id)]["id"]}' \
                            f'\nНазвание товара: {items[0][str(user_id)]["name"]}' \
                            f'\nСтатус: {items[0][str(user_id)]["status"]}' \
                            f'\nКоличество на складе: {items[0][str(user_id)]["amount"]}'
    else:
        item_text = 'Корзина пуста'
    await call.message.answer(text='Позиция удалена')
    await call.message.answer(text=item_text,
                              reply_markup=my_cart_inline_keyboards(status))
    # await bot.delete_message(chat_id=call.message.chat.id,
    #                          message_id=call.message.message_id)


@dp.callback_query_handler(navigation_callback.filter(for_data='my_cart'))
async def see_new_item(call: types.CallbackQuery):
    id = call.data.split(':')[-1]
    user_id = call.from_user.id
    status, item_info = data_manager.get_item(int(id), str(user_id), 'database/data/cart.json')
    item_text = f'{item_info["id"]}' \
                f'\nНаименование товара: {item_info["name"]}' \
                f'\nСтатус: {item_info["status"]}' \
                f'\nКоличество товара: {item_info["amount"]}'
    await bot.edit_message_text(text=item_text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id)
    await bot.edit_message_reply_markup(reply_markup=my_cart_inline_keyboards(status, id),
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)


@dp.callback_query_handler(navigation_callback.filter(for_data='items'))
async def see_new_item(call: types.CallbackQuery):
    id = call.data.split(':')[-1]
    status, item_info = data_manager.get_item(int(id), 'blankets', 'database/data/items.json')
    item_text = f'{item_info["id"]}' \
                f'\nНаименование товара: {item_info["name"]}' \
                f'\nСтатус: {item_info["status"]}' \
                f'\nКоличество товара: {item_info["amount"]}'
    await bot.edit_message_text(text=item_text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id)
    await bot.edit_message_reply_markup(reply_markup=get_items_inline_keyboards(id, status),
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)


@dp.callback_query_handler(store_callback.filter(category="blankets"))
async def store_item(call: types.CallbackQuery):
    print(call)
    user_id = call.from_user.id
    item_id = call.message.text.split('\n')[0]
    answer = data_manager.put_in_cart(item_id, "blankets", user_id)
    await call.message.answer(text=f'{answer}')


@dp.message_handler(commands=['add'])
async def answer_items_command(message: types.Message):
    await message.answer(text=f'''
    Данный раздел в разработке...
    ''')


@dp.message_handler(text=['Скрыть меню'])
async def answer_items_command(message: types.Message):
    await message.answer(text='Я скрыл меню',
                         reply_markup=see_commands_default_keyboard)


@dp.message_handler(content_types=['location'])
async def answer_items_command(message: types.Message):
    if message.from_user.id == message.contact.user_id:
        await message.answer(text=f'Спасибо! Теперь мне известно твое местоположение :)',
                             reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text=f'А это чей телефон?',
                             reply_markup=ReplyKeyboardRemove())


@dp.message_handler()
async def answer_items_command(message: types.Message):
    await message.answer(text=f'Я пока такой команды не знаю :(')
