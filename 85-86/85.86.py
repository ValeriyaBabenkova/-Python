
from sqlalchemy import create_engine
from  typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy import select, ForeignKey, delete

class Base(DeclarativeBase):
    pass

class Note(Base):
    __tablename__ = 'note'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str]
    raiting: Mapped[int]

    # user: Mapped["User"] = relationship(back_populates='notes')

    def __repr__(self):
        return f"{self.id} - {self.name_user}"

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name_user: Mapped[str]
    password: Mapped[str]

    # tasks: Mapped[List["Note"]] = relationship(back_populates='user')

    def __repr__(self):
        return f"{self.id}"

class NoteModelORM:
    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}')

    def get_notes(self, user_id):
        with Session(self.engine) as session:
            notes = session.scalars(select(Note).where(Note.user_id == user_id)).all()
            return notes

    def add_note(self, user_id,name, raiting):
        with Session(self.engine) as session:
            note = Note(user_id=user_id, name=name, raiting=raiting)
            session.add(note)
            session.commit()

    def get_notes_popular(self):
        with Session(self.engine) as session:
            notes_pop = session.scalars(select(Note).where(Note.raiting > 3)).all()
            return notes_pop

    def get_user(self, name, password):
        with Session(self.engine) as session:
            res = session.scalars(select(Users).where(Users.name_user == name, Users.password == password)).one_or_none()
            print(res)
            return res

    @staticmethod
    def _dict_factory(cursor, row):
        d = {}
        # cursor = self.connection.cursor()
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

class UserORM:
    def __init__(self, name: str, password: str, db: NoteModelORM):
        self.name = name
        self.password = password
        self.db = db

    def auth(self):
        user = self.db.get_user(self.name, self.password)
        if user:
            return user
        return None

db = NoteModelORM('notes.db')

name = input('Введите имя: ')
password = input('Введите пароль: ')
auth = False

user_id = UserORM(name, password, db).auth()

if user_id:
    auth = True
    print('Авторизация успешна')
else:
    print('неверный логин или пароль')

while True and auth:
    print('Что хотите сделать?')
    print('1 - Добавить заметку')
    print('2 - Прочитать заметки')
    print('3 - Вывести популярные заметки')

    res = input('Вводи номер: ')

    if res == '1':
        text = input('Введите название заметки: ')
        raiting = int(input('Введите рейтинг заметки: '))
        db.add_note(user_id,text, raiting)
        print('Заметка добавлена!')
        print('\n')

    elif res == '2':
        notes = db.get_notes(user_id)
        print('\n Список ваших заметок:')
        for note in notes:
            task_string = f'{note['id']}. {note['name']}. Рейтинг: {note['raiting']}'
            print(task_string)

    elif res == '3':
        notes = db.get_notes_popular()
        print('\n Список популярных заметок: ')
        for note in notes:
            task_string = f'{note['id']}. {note['name']}. Рейтинг: {note['raiting']}'
            print(task_string)
    if res == 'q':
        break
