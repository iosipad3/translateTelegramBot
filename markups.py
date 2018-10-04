import telebot
from languages import get_langs

help_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
settings = telebot.types.InlineKeyboardButton(text='Settings', callback_data='settings')
current = telebot.types.InlineKeyboardButton(text='Show current settings', callback_data='current')
help_markup.add(settings, current)

settings_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
set_from = telebot.types.InlineKeyboardButton(text='Set from language', callback_data='from')
set_to = telebot.types.InlineKeyboardButton(text='Set to language', callback_data='to')
settings_markup.add(set_to, set_from)

# Markups for laguages list
languages_from_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
languages_to_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
auto = telebot.types.InlineKeyboardButton(text='Auto-detection', callback_data='auto')
languages_from_markup.add(auto)
for lang_code, language in get_langs['langs'].items():
	languages_to_markup.add(telebot.types.InlineKeyboardButton(text=language, callback_data=lang_code))
	languages_from_markup.add(telebot.types.InlineKeyboardButton(text=language, callback_data='from' + lang_code))
