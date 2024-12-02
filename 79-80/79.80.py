import sqlite3

class NoteModelSQL:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = self._dict_factory

    def get_notes(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('select * from note where user_id = ?', (user_id,))
        return cursor.fetchall()

    def add_note(self, user_id,name, raiting):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute('insert into note (user_id, name, raiting) values (?,?,?)', (user_id, name, raiting))

    def get_notes_popular(self):
        cursor = self.connection.cursor()
        cursor.execute('select * from note where raiting > 3')
        return cursor.fetchall()
    @staticmethod
    def _dict_factory(cursor, row):
        d = {}
        # cursor = self.connection.cursor()
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __del__(self):
        print('Закрытие подключения')
        self.connection.close()

name = input('Введите имя: ')
password = input('Введите пароль: ')

auth = False

sqlmodel = NoteModelSQL('notes.db')

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
        sqlmodel.add_note(user_id,text, raiting)
        print('Заметка добавлена!')
        print('\n')

    elif res == '2':
        notes = sqlmodel.get_notes(user_id)
        print('\n Список ваших заметок:')
        for note in notes:
            task_string = f'{note['id']}. {note['name']}. Рейтинг: {note['raiting']}'
            print(task_string)

    elif res == '3':
        notes = sqlmodel.get_notes_popular()
        print('\n Список популярных заметок: ')
        for note in notes:
            task_string = f'{note['id']}. {note['name']}. Рейтинг: {note['raiting']}'
            print(task_string)
    if res == 'q':
        break
