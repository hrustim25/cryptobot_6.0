import telebot
from telebot import types
import random
import config

import asyncio
from aiocoingecko import AsyncCoinGeckoAPISession

bot = telebot.TeleBot(config.TOKEN)

default_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
button1 = types.KeyboardButton("Криптопикча дня")
button2 = types.KeyboardButton("Купить крипту")
button3 = types.KeyboardButton("Разряд демотивации")
button4 = types.KeyboardButton("Топ 0 криптовалют")
button5 = types.KeyboardButton("Правила криптокомьюнити")
button6 = types.KeyboardButton("Цены BTC, ETH, BNB (coingecko)")
button7 = types.KeyboardButton("Стать семафором")
default_markup.add(button1, button2, button3, button4, button5, button6, button7)

motivation_list_1 = [
    "Ethereum в 2015",
    "Bitcoin в 2011",
    "BNB в 2017",
    "Solana в 2019",
    "Litecoin в 2016",
    "Shiba Inu в 2020",
    "Dogecoin в 2019",
    "NEAR в 2019",
    "Filecoin в 2018",
    "The Sandbox в 2020",
    "Decentraland в 2020",
    "The Graph в 2019",
    "TRON в 2016",
    "1inch в 2018",
    "Polkadot в 2016",
    "Cosmos в 2018",
    "Matic в 2017",
]
motivation_list_2 = [
    "был бы уже далеко отсюда",
    "купался бы на пляжах Майями",
    "жил бы в роскошных отелях Дубая",
    "имел бы свой остров на Мальдивах",
    "отдыхал бы на курортах Испании",
    "наслаждался бы деликатесами Японии",
    "имел бы свой коттедж в США",
    "пил бы изысканные вина Италии",
    "пушествовал бы по всему миру",
]
motivation_list_3 = [
    "считай свои интегралы",
    "решай свои дифференциальные уравнения",
    "умножай свои матрички",
    "решай свои системы линейных уравнений",
    "приводи свои матрицы к Жордановой нормальной форме",
    "расписывай свои булевы схемы",
    "ищи своё условное математическое ожидание",
    "считай свои плотности случайных векторов",
    "пиши свои скриптики на баше",
    "ботай к своим коллоквиумам",
    "ищи свой базис Гребнера",
    "изучай свои детерминированные деревья без штрафа по времени и памяти",
    "генерируй свои строки с одинаковых хешом",
]

images_path = "images/"
images_prefix = "image_"
images_suffix = ".jpg"


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в клуб сомнительных инвестиций",
        reply_markup=default_markup,
    )


async def get_coins_data():
    async with AsyncCoinGeckoAPISession() as cg_session:
        prices = await cg_session.get_price("bitcoin, ethereum, binancecoin", "usd")
        return prices


@bot.message_handler(content_types=["text"])
def message_reply(message):
    global default_markup
    if message.text == "Криптопикча дня":
        pic_number = random.choice(range(1, 23))
        current_image = open(
            images_path + images_prefix + str(pic_number) + images_suffix, "rb"
        )
        bot.send_photo(message.chat.id, current_image)
    elif message.text == "Купить крипту":
        current_image = open(images_path + "return_card.jpg", "rb")
        bot.send_photo(message.chat.id, current_image)
    elif message.text == "Разряд демотивации":
        current_msg = (
            "Если бы ты вложился в "
            + random.choice(motivation_list_1)
            + " году, то сейчас "
            + random.choice(motivation_list_2)
            + ". А ты и дальше "
            + random.choice(motivation_list_3)
        )
        bot.send_message(message.chat.id, current_msg, reply_markup=default_markup)
    elif message.text == "Топ 0 криптовалют":
        bot.send_message(
            message.chat.id,
            "Топ 0, всё верно.\nСредства сбережения лучше матраса до сих пор не придумали",
            reply_markup=default_markup,
        )
    elif message.text == "Правила криптокомьюнити":
        bot.send_message(message.chat.id, "1. Не")
        bot.send_message(message.chat.id, "2. лезь")
        bot.send_message(message.chat.id, "3. сюда,")
        bot.send_message(message.chat.id, "4. оно")
        bot.send_message(message.chat.id, "5. тебя")
        bot.send_message(message.chat.id, "6. сожрёт", reply_markup=default_markup)
    elif message.text == "Цены BTC, ETH, BNB (coingecko)":
        async_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(async_loop)
        data = async_loop.run_until_complete(get_coins_data())
        current_msg = (
            "Текущие цены:\nBitcoin: $"
            + str(data["bitcoin"]["usd"])
            + "\nEthereum: $"
            + str(data["ethereum"]["usd"])
            + "\nBNB: $"
            + str(data["binancecoin"]["usd"])
        )
        bot.send_message(message.chat.id, current_msg, reply_markup=default_markup)
    elif message.text == "Стать семафором":
        bot.send_message(
            message.chat.id,
            "Поздравляю, вы стали семафором!!!",
            reply_markup=default_markup,
        )


while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        print("Error occured")
