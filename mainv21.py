from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import config
from aiogram.types import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
import json

from sql import BotDB

storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=storage)
BotDB = BotDB('mbase.db')
logging.basicConfig(level=logging.INFO)

# to_chat = '-858407358'
to_chat = '-899126118'


################################################################################

class Form(StatesGroup):
    main = State()
    usl = State()
    lan = State()
    op1n = State()
    op2n = State()
    op3n = State()
    opl = State()
    opa = State()
    opn = State()
    opb = State()
    opbon = State()
    obr = State()
    ind = State()
    vg = State()
    vp = State()
    pred = State()
    zam = State()


################################################################################
markup4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item17 = KeyboardButton("Предложения")
item18 = KeyboardButton("Замечания")
item12 = KeyboardButton("🏠 Возвращение в меню")
markup4.add(item12, item17, item18)
item55 = KeyboardButton("Настройки")
item55e = KeyboardButton("Settings")
markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item8 = KeyboardButton("Наши услуги")
item9 = KeyboardButton("🔁 Обратная связь")
markup.add(item8, item9, item55)

markup5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup5.add(item17, item18)

markup2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup2.add(item12)

markup3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item14 = KeyboardButton("Индивидуальный комплекс")
item15 = KeyboardButton("Комплекс на все группы мышц")
item16 = KeyboardButton("Ваши предложения")
markup3.add(item14, item15, item16)

markup1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item1 = KeyboardButton("Индивидуальная тренировочная программа 🏋️‍♂️")
item2 = KeyboardButton("Релакс программа 💆‍♂️")
item3 = KeyboardButton("Мотивационная программа 💪")
item4 = KeyboardButton("Психологическая программа 🧠")
item5 = KeyboardButton("Комплексы")
item6 = KeyboardButton("Заказать на 1 неделю")
item7 = KeyboardButton("Заказать на 2 неделю")
item20 = KeyboardButton("Заказать на 3 неделю")
markup11 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item21 = KeyboardButton("Заказать комплекс на шею")
item22 = KeyboardButton("Заказать комплекс на руки")
item23 = KeyboardButton("Заказать комплекс на ноги")
item24 = KeyboardButton("Заказать комплекс на спину")
item25 = KeyboardButton("Заказать комплекс на руки")
item26 = KeyboardButton("Заказать комплекс на все группы мышц")
# item1 = KeyboardButton("ИТ программа 🏋️‍♂️")
# item2 = KeyboardButton("Инд. программа на 2 недели")
# item3 = KeyboardButton("Инд. программа на 3 недели")
# item4 = KeyboardButton("Комплекс на спину")
# item5 = KeyboardButton("Комплекс на ноги")
# item6 = KeyboardButton("Комплекс на руки")
# item7 = KeyboardButton("Комплекс на шею")
# item13 = KeyboardButton("Специальные предложения")
markup1.row(item1)
markup1.row(item4, item2)
markup1.row(item3, item5, item12)
markup11.row(item21, item22)
markup11.row(item24, item25)
markup11.row(item23, item26)
# markup1.row(item5, item6)
# markup1.row(item7, item12, item13)

markup4e = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item17e = KeyboardButton("Suggestions")
item18e = KeyboardButton("Remarks")
item12e = KeyboardButton(" 🏠 Return to Menu")
markup4e.add(item12e, item17e, item18e)

markupe = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item8e = KeyboardButton("Our services")
item9e = KeyboardButton("🔁 Feedback")
markupe.add(item8e, item9e, item55e)

markup5e = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup5e.add(item17e, item18e)

markup2e = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup2e.add(item12e)

markup3e = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item14e = KeyboardButton("Individual complex")
item15e = KeyboardButton("Complex for all muscle groups")
item16e = KeyboardButton("Your suggestions")
markup3e.add(item14e, item15e, item16e)

markup1e = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item1e = KeyboardButton("Individual training program 🏋️‍♂️")
item2e = KeyboardButton("Relax program 💆‍♂️")
item3e = KeyboardButton("Motivational program 💪")
item4e = KeyboardButton("Psychological program 🧠")
item5e = KeyboardButton("Complexes")
item6e = KeyboardButton("Order for 1 week")
item7e = KeyboardButton("Order for week 2")
item20e = KeyboardButton("Order for week 3")
markup11e = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item21e = KeyboardButton("Order a neck complex")
item22e = KeyboardButton("Order complex in hand")
item23e = KeyboardButton("Order a complex for legs")
item24e = KeyboardButton("Order complex for back")
item25e = KeyboardButton("Order complex in hand")
item26e = KeyboardButton("Order a complex for all muscle groups")
markup12 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item28e = KeyboardButton("English")
item28 = KeyboardButton("Русский")
markup12.add(item28, item28e)

markup1e.row(item1e)
markup1e.row(item4e, item2e)
markup1e.row(item3e, item5e, item12e)
markup11e.row(item21e, item22e)
markup11e.row(item24e, item25e)
markup11e.row(item23e, item26e)

inf_usl = {}
inf_cos = {}
user_per = {}


# markup1 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
# item1 = KeyboardButton("Индивидуальные программы")
# item4 = KeyboardButton("Комплексы")
# markup1.add(item1, item4)


################################################################################

##Перед стартом
@dp.message_handler(content_types=["text"], state=None)
async def dla_debilov(message: types.Message, state: FSMContext):
    if message.text != '/start':
        await message.answer(
            "Для начала работы введите /start\nЕсли вы уже вводили эту команду, значит произошло обновление. Все ваши данные сохранены.")
    else:
        await starter(message)


##start
async def ph(message: types.Message):
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    user_per[str(user[0])] = 0
    postt = user[3]
    if int(postt) >= user[4]:
        postt = 0
    ppppp = ""
    ppppp += str('phot/')
    ppppp += str(postt)
    ppppp += str('.jpg')
    photo = InputFile(str(ppppp))
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    postt = int(postt) + 1
    if int(postt) >= user[4]:
        postt = 0
    BotDB.update_phot(postt, user[1])


@dp.message_handler(commands=['start'],
                    state=[Form.main, Form.op1n, Form.op2n, Form.op3n, Form.opa, Form.opb, Form.opn, Form.opl,
                           Form.opbon, Form.obr, Form.vg, Form.ind, Form.vp, Form.usl, Form.zam, Form.pred])
async def dla_platonov(message: types.Message, state: FSMContext):
    await starter(message)


async def starter(message: types.Message):
    global inf_usl, inf_cos
    try:
        BotDB.add_user(message.from_user.id,
                       str(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)))
    except Exception:
        pass
    try:
        with open('data.json', encoding='utf-8') as json_file:
            inf_usl = json.load(json_file)
    except:
        pass
    try:
        with open('cost.json', encoding='utf-8') as json_file:
            inf_cos = json.load(json_file)
    except:
        pass
    await ph(message)
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    if user[2]:
        await message.answer('Hello!')
        await message.answer(
            'In this application you can purchase: \n 1) Individual training program 🏋️‍♂️\n 2) Complexes for certain muscle groups (back, legs, arms, neck) \n 3) Relax program 💆♂ ️\n 4) Motivational program 💪 \n 5) Psychological program 🧠 \n',
            reply_markup=markupe)
    else:
        await message.answer('Здравствуйте!')
        await message.answer(
            'В данном приложении вы можете приобрести: \n 1) Индивидуальную тренировочную программу 🏋️‍♂️\n 2) Комплексы на определенные группу мышц (спины, ног, рук, шеи) \n 3) Релакс программу 💆‍♂️\n 4) Мотивационную программу 💪 \n 5) Психологическая программа 🧠 \n',
            reply_markup=markup)
    markup111 = types.ReplyKeyboardMarkup()
    markup111.add(types.KeyboardButton('Открыть web страницу', web_app=WebAppInfo(url='https://itproger.com')))
    await message.answer('Привет', reply_markup=markup111)
    await Form.main.set()


def gen_markup(message: types.Message):
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if user[2] != 1:
        markup.add(item6, item7, item20, item12)
    else:
        markup.add(item6e, item7e, item20e, item12e)
    return markup


@dp.message_handler(commands=['start'])
async def bot_message(message: types.Message):
    markup = gen_markup(30, "prefix", 5)
    await message.answer("asd", reply_markup=markup)


###back
@dp.message_handler(
    state=[Form.op1n, Form.op2n, Form.op3n, Form.opa, Form.opb, Form.opn, Form.opl, Form.opbon, Form.obr, Form.vg,
           Form.ind, Form.vp, Form.usl], text=['🏠 Возвращение в меню', "🏠 Return to Menu"])
async def f_back0(message: types.Message):
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    if user[2]:
        await message.answer('You are in the main menu.', reply_markup=markupe)
    else:
        await message.answer('Вы в главном меню.', reply_markup=markup)
    await Form.main.set()


@dp.message_handler(state=[Form.main], text=['Настройки', "Settings"])
async def author(message: types.Message):
    await ph(message)
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    if user[2]:
        await message.answer('Choose language', reply_markup=markup12)
    else:
        await message.answer('Выберите язык', reply_markup=markup12)
    await Form.lan.set()


@dp.message_handler(state=[Form.lan], text=['Русский', "English"])
async def author(message: types.Message):
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    if message.text == 'Русский':
        BotDB.update_lan(0, user[1])
    else:
        BotDB.update_lan(1, user[1])
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    if user[2]:
        await message.answer('You are in the main menu.', reply_markup=markupe)
    else:
        await message.answer('Вы в главном меню.', reply_markup=markup)
    await Form.main.set()


@dp.message_handler(state=[Form.main], text=['🔁 Обратная связь', "🔁 Feedback"])
async def author(message: types.Message):
    await ph(message)
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    if user[2]:
        await message.answer(
            'Thank you very much for using my bot. If you have any suggestions or comments, you can write them here',
            reply_markup=markup4e)
    else:
        await message.answer(
            'Большое спасибо за то что пользуететсь моим ботом. Если у вас есть предложения или замечания, то можете их написать тут',
            reply_markup=markup4)
    await Form.obr.set()


@dp.message_handler(state=Form.obr, text=['Предложения', 'Suggestions'])
async def predl(message: types.Message, state: FSMContext):
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    if user[2]:
        await message.answer('Enter your suggestion in one message: ', reply_markup=markup5e)
    else:
        await message.answer('Введите ваше предложение в одном сообщение: ', reply_markup=markup5)
    await Form.pred.set()


@dp.message_handler(state=Form.pred)
async def dobpredl(message: types.Message, state: FSMContext):
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    uidd = message.from_user.id
    with open('predlog.txt', "a+") as f:
        ttt = str(uidd) + ' ' + str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ') ' + str(
            message.text) + str('\n')
        f.write(ttt)
    if user[2]:
        await message.answer('You are in the feedback block', reply_markup=markup4)
    else:
        await message.answer('Вы в блоке обратной связи', reply_markup=markup4e)
    await Form.obr.set()


@dp.message_handler(state=Form.obr, text=['Remarks', 'Замечания'])
async def zamech(message: types.Message, state: FSMContext):
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    if user[2]:
        await message.answer('Enter your comment in one message: ', reply_markup=markup5e)
    else:
        await message.answer('Введите ваше замечание в одном сообщении: ', reply_markup=markup5)
    await Form.zam.set()


@dp.message_handler(state=Form.zam)
async def dodzam(message: types.Message, state: FSMContext):
    uidd = message.from_user.id
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    with open('zamechanya.txt', "a+") as f:
        ttt = str(uidd) + ' ' + str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ') ' + str(
            message.text) + str('\n')
        f.write(ttt)
    if user[2]:
        await message.answer('You are in the feedback block', reply_markup=markup4e)
    else:
        await message.answer('Вы в блоке обратной связи', reply_markup=markup4)
    await Form.obr.set()


@dp.message_handler(state=[Form.main], text=['Наши услуги', "Our services"])
async def usl(message: types.Message):
    await ph(message)
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    if user[2]:
        await message.answer('You are in the service block', reply_markup=markup1e)
    else:
        await message.answer('Вы в блоке услуг', reply_markup=markup1)
    await Form.usl.set()


@dp.message_handler(state=[Form.usl], text=['Комплексы', 'Complexes'])
async def ind_1n(message: types.Message):
    global inf_usl, inf_cos
    await ph(message)
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    global user_per
    st = str('Пользователь: @' + str(message.from_user.username) + ' ' + str(
        str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)) + ' &11%91%1%07& ')
    user_per[str(user[0])] = st
    await message.answer(inf_usl[str(message.text)])
    await message.answer(inf_cos[str(message.text)], reply_markup=markup11)
    await Form.opl.set()


@dp.message_handler(state=[Form.usl])
async def ind_1n(message: types.Message):
    # await message.answer(inf_usl['Individual training program 🏋♂️️'])
    try:
        global inf_usl, inf_cos
        await ph(message)
        markup444 = gen_markup(message)
        await message.answer(inf_usl[str(message.text)])
        await message.answer(inf_cos[str(message.text)], reply_markup=markup444)
        user = []
        user = BotDB.get_user_id(message.from_user.id)
        global user_per
        st = str('Пользователь: @' + str(message.from_user.username) + ' ' + str(
            str(message.from_user.first_name) + ' ' + str(
                message.from_user.last_name)) + ' &11%91%1%07& ' + message.text)
        user_per[str(user[0])] = st
        await Form.opl.set()
    except:
        pass


@dp.message_handler(state=[Form.opl], text=["Заказать на 1 неделю", "Заказать на 2 неделю", "Заказать на 3 неделю",
                                            "Заказать комплекс на шею", "Заказать комплекс на руки",
                                            "Заказать комплекс на ноги", "Заказать комплекс на спину",
                                            "Заказать комплекс на руки", "Заказать комплекс на все группы мышц",
                                            "Order for 1 week", "Order for 2 week", "Order for 3 week",
                                            "Order a complex for the neck", "Order a complex for the arms",
                                            "Order a complex for the legs", "Order a complex for the back",
                                            "Order a complex for your hands", "Order a complex for all muscle groups"])
async def ind_1n(message: types.Message):
    user = []
    user = BotDB.get_user_id(message.from_user.id)
    global user_per
    st1 = user_per[str(user[0])].replace('&11%91%1%07&', str(message.text))
    st = st1
    await bot.send_message(to_chat, st)
    await message.answer(
        'В ближайшее время с вами свяжется тренер, если через 2 часа с вами не свяжется наш администратор, то пишите на этот аккаунт: @platon505',
        reply_markup=markup2)


# @dp.message_handler(state=[Form.usl], text = 'Инд. программа на 2 недели')
# async def ind_2n(message : types.Message):
#     await ph(message)
#     await message.answer('В индивидуальную тренировочную программу входит: \n 1) постановление цели и составления плана для её достижения \n 2) выполнение полной диагностики организма для выявления недостатков и проблем. \n 3) Индивидуальные рекомендации по питанию. \n 4) Поддержание связи с клиентом для того, чтобы понимать его тенденцию развития.')
#     await message.answer('Её стоимость : 1000 рублей', reply_markup = markup2)
#     await Form.op2n.set()
#
# @dp.message_handler(state=[Form.usl], text = 'Инд. программа на 3 недели')
# async def ind_3n(message : types.Message):
#     await ph(message)
#     await message.answer('В индивидуальную тренировочную программу входит: \n 1) постановление цели и составления плана для её достижения \n 2) выполнение полной диагностики организма для выявления недостатков и проблем. \n 3) Индивидуальные рекомендации по питанию. \n 4) Поддержание связи с клиентом для того, чтобы понимать его тенденцию развития.')
#     await message.answer('Её стоимость : 1500 рублей', reply_markup = markup2)
#     await Form.op3n.set()
#
# @dp.message_handler(state=[Form.usl], text = 'Комплекс на руки')
# async def ind_a(message : types.Message):
#     await ph(message)
#     await message.answer('Стоимость этого комплекса : 400 рублей', reply_markup = markup2)
#     await Form.opa.set()
#
# @dp.message_handler(state=[Form.usl], text = 'Комплекс на ноги')
# async def ind_l(message : types.Message):
#     await ph(message)
#     await message.answer('Стоимость этого комплекса : 400 рублей', reply_markup = markup2)
#     await Form.opl.set()
#
# @dp.message_handler(state=[Form.usl], text = 'Комплекс на спину')
# async def ind_b(message : types.Message):
#     await ph(message)
#     await message.answer('Стоимость этого комплекса : 400 рублей', reply_markup = markup2)
#     await Form.opb.set()
#
# @dp.message_handler(state=[Form.usl], text = 'Комплекс на шею')
# async def ind_n(message : types.Message):
#     await ph(message)
#     await message.answer('Стоимость этого комплекса : 400 рублей', reply_markup = markup2)
#     await Form.opn.set()
#
# @dp.message_handler(state=[Form.usl], text = 'Специальные предложения')
# async def ind_bon(message : types.Message):
#     await ph(message)
#     await message.answer('Индивидуальный комплекс - 450 рублей \n Комплекс на все группы мышц - 550 рублей \n Ваши предложения ', reply_markup = markup3)
#     await Form.opbon.set()
#
# @dp.message_handler(state=[Form.opbon], text = "Индивидуальный комплекс")
# async def buy_ind(message: types.Message, state: FSMContext):
#     await ph(message)
#     await message.answer('Стоимость этого комплекса : 450 рублей', reply_markup = markup2)
#     await Form.ind.set()
#
# @dp.message_handler(state=[Form.opbon], text = "Комплекс на все группы мышц")
# async def buy_vg(message: types.Message, state: FSMContext):
#     await ph(message)
#     await message.answer('Стоимость этого комплекса : 550 рублей', reply_markup = markup2)
#     await Form.vg.set()
#
# @dp.message_handler(state=[Form.opbon], text = "Ваши предложения")
# async def buy_vp(message: types.Message, state: FSMContext):
#     await ph(message)
#     await message.answer('Для ваших предложений напишите пользователю @platon505', reply_markup = markup2)
#     await Form.vp.set()
#
# @dp.message_handler(state=[Form.op1n, Form.op2n, Form.op3n, Form.opa, Form.opb, Form.opn, Form.opl, Form.vg, Form.ind], text = 'Оплатить')
# async def buy(message: types.Message, state: FSMContext):
#     await ph(message)
#     current_state = await state.get_state()
#     if current_state == 'Form:op1n':
#         user = []
#         user = BotDB.get_user_id(message.from_user.id)
#         per = int(user[2])
#         per += 1
#         BotDB.update_one(per, user[1])
#         st = str('Пользователь: @' + str(message.from_user.username) + ' ' + str(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)) + ' заказал индивидуальную недельную программу')
#         await bot.send_message(to_chat, st)
#         await message.answer('В ближайшее время с вами свяжется тренер', reply_markup = markup2)
#     if current_state == 'Form:op2n':
#         user = []
#         user = BotDB.get_user_id(message.from_user.id)
#         per = int(user[3])
#         per += 1
#         BotDB.update_two(per, user[1])
#         st = str('Пользователь: @' + str(message.from_user.username) + ' ' + str(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)) + ' заказал индивидуальную 2х недельную программу')
#         await bot.send_message(to_chat, st)
#         await message.answer('В ближайшее время с вами свяжется тренер', reply_markup = markup2)
#     if current_state == 'Form:op3n':
#         user = []
#         user = BotDB.get_user_id(message.from_user.id)
#         per = int(user[4])
#         per += 1
#         BotDB.update_three(per, user[1])
#         st = str('Пользователь: @' + str(message.from_user.username)  + ' ' + str(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)) + ' заказал индивидуальную 3х недельную программу')
#         await bot.send_message(to_chat, st)
#         await message.answer('В ближайшее время с вами свяжется тренер', reply_markup = markup2)
#     if current_state == 'Form:opa':
#         user = []
#         user = BotDB.get_user_id(message.from_user.id)
#         per = int(user[6])
#         per += 1
#         BotDB.update_arm(per, user[1])
#         st = str('Пользователь: @' + str(message.from_user.username) + ' ' + str(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)) + ' заказал комплекс на руки')
#         await bot.send_message(to_chat, st)
#         await message.answer('В ближайшее время с вами свяжется тренер', reply_markup = markup2)
#     if current_state == 'Form:opb':
#         user = []
#         user = BotDB.get_user_id(message.from_user.id)
#         per = int(user[4])
#         per += 1
#         BotDB.update_back(per, user[1])
#         st = str('Пользователь: @' + str(message.from_user.username) + ' ' + str(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)) + ' заказал комплекс спину')
#         await bot.send_message(to_chat, st)
#         await message.answer('В ближайшее время с вами свяжется тренер', reply_markup = markup2)
#     if current_state == 'Form:opn':
#         user = []
#         user = BotDB.get_user_id(message.from_user.id)
#         per = int(user[7])
#         per += 1
#         BotDB.update_neck(per, user[1])
#         st = str('Пользователь: @' + str(message.from_user.username) + ' ' + str(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)) + ' заказал комплекс на шею')
#         await bot.send_message(to_chat, st)
#         await message.answer('В ближайшее время с вами свяжется тренер', reply_markup = markup2)
#     if current_state == 'Form:opl':
#         user = []
#         user = BotDB.get_user_id(message.from_user.id)
#         per = int(user[5])
#         per += 1
#         BotDB.update_leg(per, user[1])
#         st = str('Пользователь: @' + str(message.from_user.username)+ ' ' + str(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)) + ' заказал комплекс ноги')
#         await bot.send_message(to_chat, st)
#         await message.answer('В ближайшее время с вами свяжется тренер', reply_markup = markup2)
#     if current_state == 'Form:vg':
#         user = []
#         user = BotDB.get_user_id(message.from_user.id)
#         per = int(user[8])
#         per += 1
#         BotDB.update_vg(per, user[1])
#         st = str('Пользователь: @' + str(message.from_user.username) + ' ' + str(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)) + ' заказал комплекс все группы мышц')
#         await bot.send_message(to_chat, st)
#         await message.answer('В ближайшее время с вами свяжется тренер', reply_markup = markup2)
#     if current_state == 'Form:ind':
#         user = []
#         user = BotDB.get_user_id(message.from_user.id)
#         per = int(user[9])
#         per += 1
#         BotDB.update_ind(per, user[1])
#         st = str('Пользователь: @' + str(message.from_user.username) + ' ' + str(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)) + ' заказал индивидуальный комплекс')
#         await bot.send_message(to_chat, st)
#         await message.answer('В ближайшее время с вами свяжется тренер', reply_markup = markup2)
#


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
