from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import start_callback, navigation_callback, categories_callback
from .callback_data import blanket_callback, plaid_callback, shroud_callback, accessories_callback, main_callback, \
    store_callback, search_callback, remove_callback

start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='🗂 Главное меню',
                             callback_data=main_callback.new())
    ]
])

main_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='📖 Каталог',
                             callback_data=categories_callback.new()),
    ],
    [
        InlineKeyboardButton(text='🔍 Найти товар',
                             callback_data=search_callback.new()),
    ],
    # [
    #     InlineKeyboardButton(text='Поделиться контактом'),
    #     InlineKeyboardButton(text='Поделиться геопозицией')
    # ],
    [
        InlineKeyboardButton(text='Наша страничка в Instagram',
                             url='https://instagram.com/heyma.ru?igshid=YmMyMTA2M2Y=')

    ]
])

categories_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Одеяла',
                             callback_data=blanket_callback.new()),
        InlineKeyboardButton(text='Пледы',
                             callback_data=plaid_callback.new())
    ],
    [
        InlineKeyboardButton(text='Пеленки',
                             callback_data=shroud_callback.new()),
        InlineKeyboardButton(text='Аксессуары',
                             callback_data=accessories_callback.new())
    ],
    [
        InlineKeyboardButton(text='<< 🗂 Главное меню',
                             callback_data=main_callback.new()),
    ]
])


def get_items_inline_keyboards(item_index='0', status='Left_side') -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    store_btn = InlineKeyboardButton(text='📥 В корзину',
                                     callback_data=store_callback.new(category='blankets'))
    main_menu_btn = InlineKeyboardButton(text='<< 🗂 Главное меню',
                                         callback_data=main_callback.new())
    categories_btn = InlineKeyboardButton(text='< Категории',
                                          callback_data=categories_callback.new())
    match status:
        case 'Right_side':
            index_left = str(int(item_index) - 1)
            btm = InlineKeyboardButton(text='<<<',
                                       callback_data=navigation_callback.new(
                                           for_data='items',
                                           id=index_left)
                                       )
            item_inline_keyboard.add(btm)
        case 'Left_side':
            index_right = str(int(item_index) + 1)
            btm = InlineKeyboardButton(text='>>>',
                                       callback_data=navigation_callback.new(
                                           for_data='items',
                                           id=index_right)
                                       )
            item_inline_keyboard.add(btm)
        case _:
            index_left = str(int(item_index) - 1)
            index_right = str(int(item_index) + 1)
            btm_left = InlineKeyboardButton(text='<<<',
                                            callback_data=navigation_callback.new(
                                                for_data='items',
                                                id=index_left)
                                            )
            btm_right = InlineKeyboardButton(text='>>>',
                                             callback_data=navigation_callback.new(
                                                 for_data='items',
                                                 id=index_right)
                                             )
            item_inline_keyboard.row(btm_left, btm_right)
    item_inline_keyboard.add(store_btn)
    item_inline_keyboard.row(categories_btn, main_menu_btn)
    return item_inline_keyboard


def my_cart_inline_keyboards(status, item_index='0') -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    main_menu_btn = InlineKeyboardButton(text='<< 🗂 Главное меню',
                                         callback_data=main_callback.new())
    remove_btn = InlineKeyboardButton(text='🗑 Убрать из корзины',
                                      callback_data=remove_callback.new())
    if status == 0:
        item_inline_keyboard.add(remove_btn)
        item_inline_keyboard.add(main_menu_btn)
    elif status == -1:
        item_inline_keyboard.add(main_menu_btn)
    else:
        match status:
            case 'Right_side':
                index_left = str(int(item_index) - 1)
                btm = InlineKeyboardButton(text='<<<',
                                           callback_data=navigation_callback.new(
                                               for_data='my_cart',
                                               id=index_left)
                                           )
                item_inline_keyboard.add(btm)
            case 'Left_side':
                index_right = str(int(item_index) + 1)
                btm = InlineKeyboardButton(text='>>>',
                                           callback_data=navigation_callback.new(
                                               for_data='my_cart',
                                               id=index_right)
                                           )
                item_inline_keyboard.add(btm)
            case _:
                index_left = str(int(item_index) - 1)
                index_right = str(int(item_index) + 1)
                btm_left = InlineKeyboardButton(text='<<<',
                                                callback_data=navigation_callback.new(
                                                    for_data='my_cart',
                                                    id=index_left)
                                                )
                btm_right = InlineKeyboardButton(text='>>>',
                                                 callback_data=navigation_callback.new(
                                                     for_data='my_cart',
                                                     id=index_right)
                                                 )
                item_inline_keyboard.row(btm_left, btm_right)
        item_inline_keyboard.add(remove_btn)
        item_inline_keyboard.add(main_menu_btn)
    return item_inline_keyboard
