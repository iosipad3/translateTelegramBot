import telebot
import Yandex # pip install pyyandextranslateapi
import keys # File with bot_token and yandex_api_key
from database import UsersDBase # Importing our database

try: # Main bot handling block
	translater = Yandex.Translate(keys.yandex_api_key)
	bot = telebot.TeleBot(keys.bot_token)
	@bot.message_handler(commands=['start'])
	def start(message):
		bot.reply_to(message, "Hello, I'm TranslateBot! \
		If you want me to translate something for you, use /help command")

	@bot.message_handler(commands=['help'])
	def help(message):
		bot.reply_to(message, "Any translation have directions. \
		Make me know what language to should I translate by using /settings command")

	@bot.message_handler(commands=['settings'])
	def settings(message):
		bot.reply_to(message, "For setting in what language to translate, use: /set_to command")

	@bot.message_handler(commands=['set_to'])
	def set_to(message):
		message_text = message.text[8:]
		if message_text in translater.getLangs()['langs'].keys():
			UsersDBase.setData(id=message.from_user.id, lang_to=message_text)
			bot.reply_to(message, "Successful")
		else:
			bot.reply_to(message, "Fail. \
			Please, check available languages by using /languages command")

	@bot.message_handler(commands=['languages'])
	def languages(message):
		bot.reply_to(message, str(translater.getLangs()['langs']))

	@bot.message_handler(func=lambda message: True)
	def echo_all(message):
		data = UsersDBase.getData(id=message.from_user.id)
		if data[2]:
			bot.reply_to(message, translater.translate(text=message.text, lang_to=data[2], lang_from=data[1]))
		else:
			bot.reply_to(message, "Please, check your settings. \
			Translation direction should be specified")

	bot.polling(none_stop=True)
finally: # If something happened. KeyboardInterrupt, for example
	UsersDBase.disconnect()
