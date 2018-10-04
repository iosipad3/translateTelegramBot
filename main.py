import telebot
import Yandex # pip install pyyandextranslateapi
import keys # File with bot_token and yandex_api_key
from database import UsersDBase # Importing our database
from markups import *
from languages import get_langs

try:
	translater = Yandex.Translate(keys.yandex_api_key)
	bot = telebot.TeleBot(keys.bot_token)

	@bot.message_handler(commands=['start'])
	def start(message):
		bot.reply_to(message, "Hello, I'm TranslateBot! If you want me to translate something for you, use /help command")

	@bot.message_handler(commands=['help'])
	def help(message):
		bot.send_message(chat_id=message.from_user.id, text="Any translation have directions. Set your specifications by using the menu below. When you are done with it, just text me anything you want to translate!", \
		reply_markup=help_markup)

	@bot.callback_query_handler(func=lambda call: True)
	def callback(call):
		if call.data=='settings':
			bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=settings_markup)
		elif call.data=='current':
			data = UsersDBase.getData(id=call.from_user.id)
			if data:
				settings="Your current settings: "
				if data[1]:
					if data[1]=='auto-detection':
						settings = settings + "from {} ".format(data[1])
					else:
						settings = settings + "from {} ".format(get_langs['langs'][data[1]])
				if data[2]:
					settings = settings + "to {} ".format(get_langs['langs'][data[2]])
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=settings)
			else:
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="There are no settings yet")
		elif call.data=='from':
			bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=languages_from_markup)
		elif call.data=='to':
			bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=languages_to_markup)
		else: # It's language code
			if call.data=='auto':
				bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=help_markup)
				UsersDBase.setData(id=call.from_user.id, lang_from=None)
			elif call.data[:4]=='from':
				bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=help_markup)
				UsersDBase.setData(id=call.from_user.id, lang_from=call.data[4:])
			else:
				bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=help_markup)
				UsersDBase.setData(id=call.from_user.id, lang_to=call.data)
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Settings has been updated")

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
