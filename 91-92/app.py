from flask import Flask, render_template
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy import ForeignKey
from typing import List
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    user: Mapped["User"] = relationship(back_populates='tasks')

    def __repr__(self):
        return f"{self.id} - {self.name}"


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    telegram_id: Mapped[int]

    tasks: Mapped[List["Task"]] = relationship(back_populates='user')

    def __repr__(self):
        return f"{self.telegram_id}"

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    def __repr__(self):
        return f"{self.id} - {self.name}"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///D:\\БВВ\\IT\\ДЗ Python\\91-92\\bot_todo.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

@app.route('/')
def main():
    todo_db = db.session.execute(db.select(Task)).scalars().all()
    users = db.session.execute(db.select(User)).scalars().all()

    return render_template('index.html', todo_data=todo_db, users=users)
@app.route('/about')
def about_page():
    return render_template('about.html')
@app.route('/product')
def product():
    products_db = db.session.execute(db.select(Product)).scalars().all()

    return render_template('products.html', products_list = products_db)

if __name__ == '__main__':
    app.run(debug=True)