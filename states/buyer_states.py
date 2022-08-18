from aiogram.dispatcher.filters.state import StatesGroup, State


class BuyerState(StatesGroup):
    wait_item_name = State()
    first_question = State()
    second_question = State()
    third_question = State()
