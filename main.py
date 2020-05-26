import telebot
import random
import requests
from telebot import types
from Messages import *
from telebot.types import LabeledPrice, ShippingOption
import logging

logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)


chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

access_token = '1235052627:AAFhn3Toc2uotGtyy4InMAkEou-xcD9rPu0'
bot = telebot.TeleBot(access_token)

PRICES = [
    types.LabeledPrice(label='Кейсы до 150р', amount=4900)
]
PRICES1 = [
    types.LabeledPrice(label='Кейсы до 500р', amount=9900)
]
PRICES2 = [
    types.LabeledPrice(label='Кейсы до 700р', amount=12900)
]
PRICES3 = [
    types.LabeledPrice(label='Кейсы до 1500р', amount=29900)
]
PRICES4 = [
    types.LabeledPrice(label='Кейсы до 3000р', amount=99900)
]
PRICES5 = [
    types.LabeledPrice(label='Случайный нож', amount=299900)
]


def inline_menu():
    """
    Create inline menu for new chat
    :return: InlineKeyboardMarkup
    """
    button1 = types.InlineKeyboardButton(text="Кейсы до 150р - 49р🤩", callback_data="1")
    button2 = types.InlineKeyboardButton(text="Кейсы до 500р - 99р🤩", callback_data="2")
    button3 = types.InlineKeyboardButton(text="Кейсы до 700р - 129р🤩", callback_data="3")
    button4 = types.InlineKeyboardButton(text="Кейсы до 1500р - 299р🤩", callback_data="4")
    button5 = types.InlineKeyboardButton(text="Кейсы до 3000р - 999р🤩", callback_data="5")
    button6 = types.InlineKeyboardButton(text="Случайный нож - 2999р🤑", callback_data="6")
    menu = types.InlineKeyboardMarkup(row_width=1)
    menu.add(button1, button2, button3, button4, button5, button6)

    return menu


@bot.message_handler(commands=['start'])
def echo(message):
    user_id = message.chat.id
    try:
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)

        keyboard.row("🗒Каталог🗒", "⚠️Дополнительная информация⚠️")

        bot.send_message(user_id, m_start, reply_markup=keyboard)
    except:
        bot.send_message(user_id, 'ERROR')


@bot.message_handler(content_types=['text'])
def lalala(message):
    user_id = message.chat.id
    try:
        menu = inline_menu()
        if message.text == '🗒Каталог🗒':
            bot.send_message(user_id, '🗒Наш каталог:', reply_markup=menu)

        elif message.text == '⚠️Дополнительная информация⚠️':
            bot.send_message(user_id, m_info)
    except:
        bot.send_message(user_id, 'ERROR')
    
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    user_id = call.message.chat.id

#632593626:TEST:i56982357197
#635983722:LIVE:i78793167431

    try:
        if call.data == "1":
            bot.send_invoice(user_id,
                               title='🤩Кейсы до 150р',
                               description='👑Ссылка действует на 15 кейсов ценой до 150р',
                               provider_token='635983722:LIVE:i78793167431',
                               currency='rub',
                               photo_url="https://sun9-23.userapi.com/c824500/v824500479/82a8c/XsF-LprVsWc.jpg?ava=1",
                               photo_height=400,  # !=0/None or picture won't be shown
                               photo_width=400,
                               photo_size=400,
                               need_email=False,
                               need_phone_number=False,
                               # need_shipping_address=True,
                               is_flexible=False,  # True If you need to set up Shipping Fee
                               prices=PRICES,
                               start_parameter='time-machine-example',
                               invoice_payload='some-invoice-payload-for-our-internal-use')
      
        elif call.data == "2":
            bot.send_invoice(user_id,
                               title='🤩Кейсы до 500р',
                               description='👑Ссылка действует на 10 кейсов ценой до 500р',
                               provider_token='635983722:LIVE:i78793167431',
                               currency='rub',
                               photo_url="https://sun9-23.userapi.com/c824500/v824500479/82a8c/XsF-LprVsWc.jpg?ava=1",
                               photo_height=400,  # !=0/None or picture won't be shown
                               photo_width=400,
                               photo_size=400,
                               need_email=False,
                               need_phone_number=False,
                               # need_shipping_address=True,
                               is_flexible=False,  # True If you need to set up Shipping Fee
                               prices=PRICES1,
                               start_parameter='time-machine-example',
                               invoice_payload='some-invoice-payload-for-our-internal-use')


        elif call.data == "3":
            bot.send_invoice(user_id,
                               title='🤩Кейсы до 700р',
                               description='👑Ссылка действует на 10 кейсов ценой до 700р',
                               provider_token='635983722:LIVE:i78793167431',
                               currency='rub',
                               photo_url="https://sun9-23.userapi.com/c824500/v824500479/82a8c/XsF-LprVsWc.jpg?ava=1",
                               photo_height=400,  # !=0/None or picture won't be shown
                               photo_width=400,
                               photo_size=400,
                               need_email=False,
                               need_phone_number=False,
                               # need_shipping_address=True,
                               is_flexible=False,  # True If you need to set up Shipping Fee
                               prices=PRICES2,
                               start_parameter='time-machine-example',
                               invoice_payload='some-invoice-payload-for-our-internal-use')

      
        elif call.data == "4":
            bot.send_invoice(user_id,
                               title='🤩Кейсы до 1500р',
                               description='👑Ссылка действует на 10 кейсов ценой до 1500р',
                               provider_token='635983722:LIVE:i78793167431',
                               currency='rub',
                               photo_url="https://sun9-23.userapi.com/c824500/v824500479/82a8c/XsF-LprVsWc.jpg?ava=1",
                               photo_height=400,  # !=0/None or picture won't be shown
                               photo_width=400,
                               photo_size=400,
                               need_email=False,
                               need_phone_number=False,
                               # need_shipping_address=True,
                               is_flexible=False,  # True If you need to set up Shipping Fee
                               prices=PRICES3,
                               start_parameter='time-machine-example',
                               invoice_payload='some-invoice-payload-for-our-internal-use')


        elif call.data == "5":
            bot.send_invoice(user_id,
                               title='🤩Кейсы до 3000р',
                               description='👑Ссылка действует на 7 кейсов ценой до 3000р',
                               provider_token='635983722:LIVE:i78793167431',
                               currency='rub',
                               photo_url="https://sun9-23.userapi.com/c824500/v824500479/82a8c/XsF-LprVsWc.jpg?ava=1",
                               photo_height=400,  # !=0/None or picture won't be shown
                               photo_width=400,
                               photo_size=400,
                               need_email=False,
                               need_phone_number=False,
                               # need_shipping_address=True,
                               is_flexible=False,  # True If you need to set up Shipping Fee
                               prices=PRICES4,
                               start_parameter='time-machine-example',
                               invoice_payload='some-invoice-payload-for-our-internal-use')

      
        elif call.data == "6":
            bot.send_invoice(user_id,
                               title='🤩Случайный нож',
                               description='👑Ссылка действует на 5 кейсов: "Случайный нож"',
                               provider_token='635983722:LIVE:i78793167431',
                               currency='rub',
                               photo_url="https://sun9-23.userapi.com/c824500/v824500479/82a8c/XsF-LprVsWc.jpg?ava=1",
                               photo_height=400,  # !=0/None or picture won't be shown
                               photo_width=400,
                               photo_size=400,
                               need_email=False,
                               need_phone_number=False,
                               # need_shipping_address=True,
                               is_flexible=False,  # True If you need to set up Shipping Fee
                               prices=PRICES5,
                               start_parameter='time-machine-example',
                               invoice_payload='some-invoice-payload-for-our-internal-use')
    except:
        bot.send_message(user_id, 'ERROR')

@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                              error_message='О, кажется, наши курьеры сотрудники сейчас обедают. Попробуйте позже!😞')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Инопланетяне пытались украсть CVV вашей карты, но мы успешно защитили ваши учетные данные😎, попробуйте снова заплатить через несколько минут, нам нужен небольшой отдых.")



@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    user_id = message.chat.id
    try:
        for n in range(1):
            url =''
            for i in range(7):
                url += random.choice(chars)


        bot.send_message(user_id, m_thnk + 'http://partner-forcedrop.rf.gd/' + url + m_kak)
    except:
        bot.send_message(user_id, 'ERROR')

try:
    bot.polling(none_stop=True)
except:
    bot.stop_polling()
    bot.polling(none_stop=True)