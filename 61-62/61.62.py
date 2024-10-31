import telebot
import random
from telebot import types

token = ' '
bot = telebot.TeleBot(token)

user_state = ''
GAME_STATE = 'game'
num_bot = random.randint(1, 15)

@bot.message_handler(commands=['game'])
def game_start(message):
    description = 'Я бот для развлечения. Давай посмотрим, сможешь ли ты угадать число. Жми на кнопку "Играть".'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Играть')
    markup.add(button)
    bot.send_message(message.chat.id, description, reply_markup=markup)
@bot.message_handler(regexp='Играть')
@bot.message_handler(commands=['add'])
def add_num(message):
    global user_state
    bot.send_message(message.chat.id, 'Введи число от 1 до 15')
    user_state = GAME_STATE
@bot.message_handler(func=lambda message: True)
def game_play(message):
    global user_state
    global num_bot
    print(num_bot)
    if user_state == GAME_STATE:
        num_user = int(message.text)
    if num_user != num_bot:
        bot.reply_to(message, 'Вы не угадали, попробуйте ещё')
    else:
        bot.reply_to(message, 'Поздравляю! Вы угадали! До новых встреч)')
        user_state = ''


bot.infinity_polling()