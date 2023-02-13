import telebot
from telebot import types

bot = telebot.TeleBot("6251973043:AAFoQXF6XW2WqT1MyScWillM52OyzWlBRfg")

@bot.message_handler(commands = ["start"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("узнать правило игры") 
    but2 = types.KeyboardButton("играть")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id,"Выбери ниже",reply_markup=markup)

@bot.message_handler(content_types = "text")
def controller(message):
    print(message.text)
    if message.text == "узнать правило игры":
        bot.send_message(message.chat.id,"За один ход можно забрать не более чем 28 конфет")
    elif message.text == "играть":
        bot.send_message(message.chat.id,"На столе лежит 221 конфета")
        bot.send_message(message.chat.id,"делайте ход")
        
        
     
bot.infinity_polling()