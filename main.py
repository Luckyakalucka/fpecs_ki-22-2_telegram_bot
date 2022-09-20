""""
@dp.message_handler(commands=['NAME'])
async def NAME(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    await message.answer()
"""

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.utils import executor
from datetime import datetime

import config
startTime = datetime.now()
bot = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['status'])
async def status(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    status = "I am Alive!\n"
    status += "Uptime: " + str((datetime.now() - startTime))
    await bot.send_photo(chat_id=message.from_user.id, photo=InputFile('assets/timetable/1.jpg'))


@dp.message_handler(commands=['timetable'])
async def timetable(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/timetable.png'))


@dp.message_handler(commands=['monday'])
async def monday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    if int(week) % 2 == 0:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/mon_b.png'))
    else:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/mon_a.png'))


@dp.message_handler(commands=['tuesday'])
async def tuesday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    if int(week) % 2 == 0:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/tue_b.png.png'))
    else:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/tue_a.png'))


@dp.message_handler(commands=['wednesday'])
async def wednesday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    if int(week) % 2 == 0:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/wed_b.png'))
    else:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/wed_a.png'))

@dp.message_handler(commands=['thursday'])
async def thursday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    if int(week) % 2 == 0:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/thu_b.png'))
    else:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/thu_a.png'))


@dp.message_handler(commands=['friday'])
async def friday(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/fri.png'))


if __name__ == '__main__':
    executor.start_polling(dp)