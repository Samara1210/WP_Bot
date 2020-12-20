import telebot
from telebot import types

bot = telebot.TeleBot("1496630019:AAEMYek1m3C-XcZ1QEiSWr19c0V-h6teFZ8")


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup()
    but1 = types.KeyboardButton("Menu")
    markup.add(but1)
    bot.send_message(message.chat.id, "Choose category", reply_markup=markup)

    @bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == 'Menu':
        markup = types.ReplyKeyboardMarkup()
        button1 = types.KeyboardButton("Aesthetic")
        button2 = types.KeyboardButton("Black")
        button3 = types.KeyboardButton("Autumn")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Choose:", reply_markup=markup)
    if message.text == "Aesthetic":

        bot.send_photo(message.chat.id, 'https://pin.it/65dbTuF')
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, "Choose:", reply_markup=markup)

    if message.text == "Black":
        bot.send_photo(message.chat.id, 'https://pin.it/4FTt9jb')
