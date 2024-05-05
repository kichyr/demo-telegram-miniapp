import os

import telebot
from telebot import types
from telebot.types import LabeledPrice, ShippingOption

BOT_TOKEN = "6798029979:AAEQ1UPbgbFFykvYuV7n2Cgk4AHLJwqJ6f4"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    webUrl = types.WebAppInfo("https://www.ozon.ru/?miniapp=supermarket")
    web_btn = types.InlineKeyboardButton(text='Название для кнопки', web_app=webUrl)
    markup.add(web_btn)
    bot.send_message(message.from_user.id, "Перейти к оплате", reply_markup = markup)


bot.infinity_polling()