import sqlite3

def add_note(user_id,text, raiting):
    connection = sqlite3.connect('notes.db')
    cursor = connection.cursor()
    cursor.execute('insert into note (user_id, name, raiting) values (?,?,?)', (user_id,text, raiting))
    connection.commit()
    connection.close()
def show_notes(user_id):
    connection = sqlite3.connect('notes.db')
    cursor = connection.cursor()
    cursor.execute('select * from note where user_id = ?', (user_id,))
    rows = cursor.fetchall()
    connection.close()
    return rows
def popular_notes():
    connection = sqlite3.connect('notes.db')
    cursor = connection.cursor()
    cursor.execute('select * from note where raiting > 3')
    rows = cursor.fetchall()
    connection.close()
    return rows

name = input('Введите имя: ')
password = input('Введите пароль: ')

auth = False

connection = sqlite3.connect('notes.db')
cursor = connection.cursor()
rows = cursor.execute("select * from users where name_user = ? and password = ? ", (name, password))
res = rows.fetchone()

if res:
    auth = True
    user_id = res[0]
    print('Авторизация успешна')
else:
    print('Неверный логин или пароль')

while True and auth:
    print('Что хотите сделать?')
    print('1 - Добавить заметку')
    print('2 - Прочитать заметки')
    print('3 - Вывести популярные заметки')

    res = input('Вводи номер: ')

    if res == '1':
        text = input('Введите название заметки: ')
        raiting = int(input('Введите рейтинг заметки: '))
        add_note(user_id,text, raiting)
        print('Заметка добавлена!')
        print('\n')

    elif res == '2':
        rows = show_notes(user_id)
        print('\n Список ваших заметок:')
        for row in rows:
            task_string =  f'{row[0]}. {row[2]}. Рейтинг: {row[3]}'
            print(task_string)
        print('\n')

    elif res == '3':
        rows = popular_notes()
        print('\n Список популярных заметок: ')
        for row in rows:
            task_string = f'{row[0]}. {row[1]}. Рейтинг: {row[2]}'
            print(task_string)
        print('\n')
    if res == 'q':
        break
