#!/usr/bin/env python

import os

from flask import Flask
from flask import render_template

from database import db, Book, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    # fill DB with testing data(fixtures)
    novel = Genre(title="Роман")
    db.session.add(novel)
    fantasy = Genre(title="Фантастика")
    db.session.add(fantasy)
    detective = Genre(title="Детектив")
    db.session.add(detective)

    island = Book(title="'Остров Сокровищ' Роберт Льюис Стивенсон", genre=novel)
    db.session.add(island)
    war = Book(title="'Война и мир' Лев Толстой", genre=novel)
    db.session.add(war)
    outcasts = Book(title="'Отверженные' Виктор Гюго", genre=novel)
    db.session.add(outcasts)
    master = Book(title="'Мастер и Маргарита' Михаил Булгаков", genre=novel)
    db.session.add(master)
    crime = Book(title="'Преступление и наказание' Фёдор Достоевский", genre=novel)
    db.session.add(crime)
    fellow = Book(title="'Три товарища' Эрих Мария Ремарк", genre=novel)
    db.session.add(fellow)
    mars = Book(title="'Марсианские хроники' Рей Бредбери", genre=fantasy)
    db.session.add(mars)
    worlds = Book(title="'Война миров' Герберт Уэллс", genre=fantasy)
    db.session.add(worlds)
    witcher = Book(title="'Ведьмак' Анджей Сапковский", genre=fantasy)
    db.session.add(witcher)
    game = Book(title="'Игра престолов' Джордж Мартин", genre=fantasy)
    db.session.add(game)
    wizard = Book(title="'Волшебник Земноморья' Урсула Гуин", genre=fantasy)
    db.session.add(wizard)
    riddle = Book(title="'Загадка Эндхауза' Агата Кристи", genre=detective)
    db.session.add(riddle)
    azazel = Book(title="'Азазель' Борис Акунин", genre=detective)
    db.session.add(azazel)
    black = Book(title="'Чёрная орхидея' Джеймс Эллрой", genre=detective)
    db.session.add(black)
    broker = Book(title="'Брокер' Джон Гришем", genre=detective)
    db.session.add(broker)
    dangerous = Book(title="'Особо опасен' Джон Ле Карре", genre=detective)
    db.session.add(dangerous)

    db.session.commit()


@app.route("/")
def all_books():
    books = Book.query.all()
    return render_template("all_books.html", books=books)


@app.route("/genre/<int:genre_id>")
def books_by_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template(
        "books_by_genre.html",
        genre_title=genre.title,
        books=genre.books,
    )


if __name__ == '__main__':
    app.run()
