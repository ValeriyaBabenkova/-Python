import telebot
import json
import sqlite3
from telebot import types

class TaskModelSQL:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_tasks(self, user_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory
        cursor = connection.cursor()
        cursor.execute('select * from task where user_id = ?', (user_id, ))
        rows = cursor.fetchall()
        connection.close()
        return rows

    def get_user(self, telegram_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory

        cursor = connection.cursor()
        rows = cursor.execute('select * from user where telegram_id = ?', (telegram_id,)).fetchone()
        connection.close()
        return rows

    def add_user(self, user_id):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute('insert into user (user_id) values (?)', (user_id,))
        connection.commit()
        connection.close()

    def add_task(self, text, user_id):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute('insert into task (user_id, name) values (?, ?)', (user_id, text))
        connection.commit()
        connection.close()

    def delete_task(self, task_id):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute('delete from task where id = ?', (task_id,))
        connection.commit()
        connection.close()

    @staticmethod
    def _dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d


token = ' '
bot = telebot.TeleBot(token)

toDoList = []
user_state = ''
ADD_STATE = 'add'
DEL_STATE = 'del'

db_name = 'bot_todo.db'
db = TaskModelSQL(db_name)

@bot.message_handler(commands=['start'])
def start(message):
    description = "Я бот для создания списка дел. Жми кнопку или команду /add для добавления задачи."
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_add = types.KeyboardButton('Добавить задачу')
    button_tasks = types.KeyboardButton('Посмотреть задачи')
    button_del = types.KeyboardButton('Удалить задачу')
    markup.add(button_add, button_tasks, button_del)

    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    print(telegram_id, user)
    if not user:
        db.add_user(telegram_id)
        bot.reply_to(message, 'Вы добавлены в базу')
    bot.send_message(message.chat.id, description, reply_markup=markup)

@bot.message_handler(regexp='Добавить задачу')
@bot.message_handler(commands=['add'])
def add(message):
    global user_state
    user_state = ADD_STATE
    bot.reply_to(message, text='Введи текст задачи')

@bot.message_handler(regexp='Удалить задачу')
@bot.message_handler(commands=['del'])
def delete_task(message):
    global user_state
    user_state = DEL_STATE
    telegram_id = message.chat.id
    user = db.get_user(telegram_id)

    list_tasks = db.get_tasks(user['id'])
    task_string = ''
    for task in list_tasks:
        task_string += f"{task['name']} (id задачи - {task['id']}) \n"
    bot.reply_to(message, text= f'Ваши текущие задачи:\n{task_string} \n Введите id задачи, которую хотите удалить.')

@bot.message_handler(regexp='Посмотреть задачи')
@bot.message_handler(commands=['tasks'])
def get_task_list(message):
    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    if not user:
        return bot.reply_to(message, 'Вас нет в базе')

    list_tasks = db.get_tasks(user['id'])
    if not list_tasks:
        return bot.reply_to(message, 'У вас нет задач')

    task_string = ''
    for task in list_tasks:
        task_string += f"{task['name']} (id задачи - {task['id']}) \n"
    bot.reply_to(message, task_string)

@bot.message_handler(commands=['end'])
def end_state(message):
    global user_state
    user_state = ''
    bot.reply_to(message, 'Вы вышли из сеанса добавления')

@bot.message_handler(commands=['keyboard'])
def keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Добавить задачу')
    markup.add(button)
    bot.send_message(message.chat.id, 'Текст', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def get_task(message):
    global user_state
    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    if user_state == ADD_STATE:
        db.add_task(message.text, user['id'])
        user_state = ''
        bot.reply_to(message, 'Добавил в базу')

    if user_state == DEL_STATE:
        try:
            task_id = int(message.text)
        except Exception:
            print('Ошибка в вводе числа')
            return

        user = db.get_user(telegram_id)
        list_tasks = db.get_tasks(user['id'])

        for task in list_tasks:
            if task_id == task['id']:
                db.delete_task(task['id'])
                bot.reply_to(message, 'Задача удалена')

bot.infinity_polling()
