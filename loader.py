from aiogram import Bot, Dispatcher
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)  # Диспетчер, который слушает определенного бота