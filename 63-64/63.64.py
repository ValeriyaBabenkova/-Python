import telebot
from telebot import types
from gpt import YandexGPT

token = ''
bot = telebot.TeleBot(token)

user_state = ''
DIALOG_STATE = 'dialog'

y_token = ''
y_catalog = ''

yandex_bot = YandexGPT(y_token, y_catalog)

users = {}

@bot.message_handler(commands=["start"])
def start(message):
    description = 'Я бот - переводчик. Давайте переведём ваш текст на испанский. Жмите кнопку "Ввести текст" или команду /add.'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Ввести текст')
    markup.add(button)
    bot.send_message(message.chat.id, description, reply_markup=markup)
@bot.message_handler(commands=["add"])
@bot.message_handler(regexp='Ввести текст')
def ask(message):
    global user_state
    user_state = DIALOG_STATE
    bot.reply_to(message, 'Введите текст, который вы хотите перевести . Чтобы выйти - жмите команду /end')
@bot.message_handler(commands=["end"])
def end(message):
    global user_state
    user_state = ''
    bot.reply_to(message, 'До новых встреч')
@bot.message_handler(func=lambda message: True)
def get_text(message):
    if user_state == DIALOG_STATE:
        chat_id = message.chat.id
        response = yandex_bot.send_translate(message.text)
        bot.reply_to(message, response)

bot.infinity_polling()