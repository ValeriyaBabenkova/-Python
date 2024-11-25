import sqlite3

def add_note(text, raiting):
    connection = sqlite3.connect('notes.db')
    cursor = connection.cursor()
    cursor.execute('insert into note (name, raiting) values (?,?)', (text, raiting))
    connection.commit()
    connection.close()
def show_notes():
    connection = sqlite3.connect('notes.db')
    cursor = connection.cursor()
    cursor.execute('select * from note')
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


while True:
    print('Что хотите сделать?')
    print('1 - Добавить заметку')
    print('2 - Прочитать заметки')
    print('3 - Вывести популярные заметки')

    res = input('Вводи номер: ')

    if res == '1':
        text = input('Введите название заметки: ')
        raiting = int(input('Введите рейтинг заметки: '))
        add_note(text, raiting)
        print('Заметка добавлена!')
        print('\n')

    elif res == '2':
        rows = show_notes()
        print('\n Список заметок: ')
        for row in rows:
            task_string =  f'{row[0]}. {row[1]}. Рейтинг: {row[2]}'
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
