from email import message
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from Players import Players

TOKEN = "5157675817:AAHaPRDsp2Qem1ZCHnYeVOmSavWcKz9DUXY"
list_players = list()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message):
    global list_players
    await message.answer("Стартуем! Сколько игроков?")
    @dp.message_handler(content_types=["text"])
    async def get_num_players(message):
        global list_players
        try:
            number_of_players = int(message.text)
        except Exception:
            print(f'Incorrect number of players, the user\'s response: "{message.text}"')
            await message.answer("Введи число")
            return
        else:
            print('Сorrect number of players')

            for i in range(number_of_players):
                player = Players(i, "")
                list_players.append(player)


@dp.message_handler(commands=["first_night"])
async def start(message):
    await message.answer("Начинаем первую ночь. Кто мафия?")
    @dp.message_handler(content_types=["text"])
    async def get_mafia_id(message):
        try:
            mafia = message.text
            mafia = mafia.split(" ")
        except Exception:
            print(f'Incorrect mafia id, the user\'s response: "{message.text}"')
            await message.answer("Введи числа через пробел")
            return
        else:
            print('Сorrect mafia id')

if __name__ == '__main__':
    executor.start_polling(dp)