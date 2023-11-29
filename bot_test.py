from django.conf import settings
from telebot import TeleBot

bot = TeleBot('6739510180:AAFonXF_QYu1LYMRZ4etK5dUXTTQESXVNEs')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'test')
