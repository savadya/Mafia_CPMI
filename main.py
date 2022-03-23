from email import message
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from Players import Players

bot = Bot(token="5157675817:AAHaPRDsp2Qem1ZCHnYeVOmSavWcKz9DUXY")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

list_players = list()
aware_number_players = False
aware_id_mafia = False

class InputData(StatesGroup):
    number_players = State()
    id_mafia = State()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await InputData.number_players.set()
    await message.answer("Стартуем! Сколько игроков?")

@dp.message_handler(state=InputData.number_players)
async def input_number_players(message: types.Message):
    global list_players
    global aware_number_players
    if aware_number_players:
        return
    try:
        number_players = int(message.text)
    except Exception:
        print(f'Incorrect number of players, the user\'s response: "{message.text}"')
        await message.answer("Введи число")
    else:
        print('Сorrect number of players')
        for i in range(number_players):
            list_players.append(Players(i, ""))
        aware_number_players = True
        await InputData.id_mafia.set()
        await message.answer("Кто мафия?")


@dp.message_handler(state=InputData.id_mafia)
async def input_number_players(message: types.Message):
    global list_players
    global aware_id_mafia
    if aware_id_mafia:
        return
    try:
        id_mafia = message.text
        mafia = [int(i) for i in id_mafia.split(" ")]
        for i in mafia:
            player = list_players[i - 1]
            list_players[i - 1] = player.role_replacement("mafia")
    except Exception:
        print(f'Incorrect id mafia, the user\'s response: "{message.text}"')
        await message.answer("Введи числа, через пробел")
    else:
        print('Сorrect id mafia')
        aware_id_mafia = True


if __name__ == '__main__':
    executor.start_polling(dp)