# pip install pyyandextranslateapi
import Yandex
import telebot
import secret

bot = telebot.TeleBot(secret.bot_token)

@bot.message_handler(commands=['start', 'help', 'settings'])
def send_welcome(message):
	bot.reply_to(message, "message")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling(none_stop=True)
