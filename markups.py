import telebot

help_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
settings = telebot.types.InlineKeyboardButton(text='Settings', callback_data='settings')
current = telebot.types.InlineKeyboardButton(text='Show current settings', callback_data='current')
feedback = telebot.types.InlineKeyboardButton(text='Send feedback', callback_data='feed')
help_markup.add(settings, current, feedback)

settings_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
# set_from = telebot.types.InlineKeyboardButton(text='Set from language', callback_data='from')
set_to = telebot.types.InlineKeyboardButton(text='Set to language', callback_data='to')
settings_markup.add(set_to)


# Markup for laguages list
languages_markup = telebot.types.InlineKeyboardMarkup(row_width=2)
l_en = telebot.types.InlineKeyboardButton(text='ENG', callback_data='en')
l_ru = telebot.types.InlineKeyboardButton(text='RUS', callback_data='ru')
languages_markup.add(l_en, l_ru)
# languages_from_markup = languages_markup NEED TO COPY!!! OR in destination add and delete after use
# l_auto = telebot.types.InlineKeyboardButton(text='AUTO', callback_data='auto')
