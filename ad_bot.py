import aiogram.utils.markdown as md
import aiogram
from aiogram import Bot, Dispatcher, executor, types
import config
from aiogram.types import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from random import randint
import schedule
import threading
import logging
import time
import datetime
from datetime import datetime
from datetime import date
import random
import asyncio
from time import sleep
import json

import schedule
import os
from aiogram.types.message import ContentType
from sql import BotDB


class Form(StatesGroup):
    main = State()
    val = State()
    cost = State()

storage = MemoryStorage()
bot = Bot(token = config.TOKEN)
dp = Dispatcher(bot, storage=storage)
BotDB = BotDB('mbase1.db')
logging.basicConfig(level=logging.INFO)
key = str
sl = {}
cos = {}

@dp.message_handler(content_types = ["text"], state = None)
async def dla_debilov(message: types.Message, state: FSMContext):
    if message.text != '/start':
        await message.answer("Для начала работы введите /start\nЕсли вы уже вводили эту команду, значит произошло обновление. Все ваши данные сохранены.")
    else:
        await starter(message)

async def starter(message: types.Message):
    await message.answer('Введите ключ')
    await Form.main.set()

@dp.message_handler(content_types = ["text"], state = Form.main)
async def add_k(message: types.Message, state: FSMContext):
    global key
    key = str(message.text)
    await message.answer('Введите значение')
    await Form.val.set()

@dp.message_handler(content_types = ["text"], state = Form.val)
async def add_k(message: types.Message, state: FSMContext):
    global sl
    try:
        with open('data.json', encoding='utf-8') as json_file:
            sl = json.load(json_file)
    except:
        pass
    sl[key] = message.text
    with open("data.json", "w", encoding='utf-8') as outfile:
        json.dump(sl, outfile, indent=4, ensure_ascii=False)
    await message.answer('Введите цену')
    await Form.cost.set()
@dp.message_handler(content_types = ["text"], state = Form.cost)
async def add_k(message: types.Message, state: FSMContext):
    global cos
    try:
        with open('cost.json', encoding='utf-8') as json_file:
            cos = json.load(json_file)
    except:
        pass
    cos[key] = message.text
    with open("cost.json", "w", encoding='utf-8') as outfile:
        json.dump(cos, outfile, indent=4, ensure_ascii= False)
    await message.answer('Введите цену')
    await Form.main.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = False)

