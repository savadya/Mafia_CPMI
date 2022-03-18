from email import message
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import Players

TOKEN = "5157675817:AAHaPRDsp2Qem1ZCHnYeVOmSavWcKz9DUXY"
list_players = list()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Стартуем! Сколько игроков?")
    @dp.message_handler(content_types=["text"])
    async def get_text_messages(message):
        try:
            number_of_players = int(message.text)
        except Exception:
            print(f'Incorrect response, the user\'s response: "{message.text}"')
        else:
            print('Сorrect user response')
                
    message.answer("Отлично")

if __name__ == '__main__':
    executor.start_polling(dp)