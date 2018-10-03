import telebot
import Yandex # pip install pyyandextranslateapi
import keys # File with bot_token and yandex_api_key
from database import UsersDBase # Importing our database
from markups import *

try:
	translater = Yandex.Translate(keys.yandex_api_key)
	bot = telebot.TeleBot(keys.bot_token)

	@bot.message_handler(commands=['start'])
	def start(message):
		bot.reply_to(message, "Hello, I'm TranslateBot! If you want me to translate something for you, use /help command")

	@bot.message_handler(commands=['help'])
	def help(message):
		bot.send_message(chat_id=message.from_user.id, text="Any translation have directions. Set your specifications, please: ", \
		reply_markup=help_markup)
		# Your current languages:

	@bot.callback_query_handler(func=lambda call: True)
	def callback(call):
		if call.data=='settings':
			bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=settings_markup)
		elif call.data=='current':
			pass
		elif call.data=='feed':
			pass
		elif call.data=='from':
			pass
		elif call.data=='to':
			bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=languages_markup)
		else:#it's language code
			bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=help_markup)
			UsersDBase.setData(id=call.from_user.id, lang_to=call.data)
			# Notification of (non-)successful

	@bot.message_handler(commands=['languages'])
	def languages(message):
		bot.reply_to(message, str(translater.getLangs()['langs']))

	@bot.message_handler(func=lambda message: True)
	def echo_all(message):
		data = UsersDBase.getData(id=message.from_user.id)
		if data and data[2]:
			bot.reply_to(message, translater.translate(text=message.text, lang_to=data[2], lang_from=data[1]))
		else:
			bot.reply_to(message, "Please, check your settings. \
			Translation direction should be specified")

	bot.polling(none_stop=True)
finally: # If something happened. KeyboardInterrupt, for example
	UsersDBase.disconnect()
