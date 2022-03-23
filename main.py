from email import message
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from Players import Players

TOKEN = "5157675817:AAHaPRDsp2Qem1ZCHnYeVOmSavWcKz9DUXY"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

list_players = list()



if __name__ == '__main__':
    executor.start_polling(dp)