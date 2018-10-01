import telebot
from Yandex import Translate # pip install pyyandextranslateapi
import keys # File with bot_token and yandex_api_key
from database import UsersDBase # Importing our database

try: # Main bot handling block
	bot = telebot.TeleBot(keys.bot_token)
	@bot.message_handler(commands=['start', 'help', 'settings'])
	def send_welcome(message):
		bot.reply_to(message, "message")

	@bot.message_handler(func=lambda message: True)
	def echo_all(message):
		bot.reply_to(message, message.text)

	bot.polling(none_stop=True)
finally: # If something happened. KeyboardInterrupt, for example
	UsersDBase.disconnect()
