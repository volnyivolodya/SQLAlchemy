#!/usr/bin/env python

import os

from flask import Flask
from flask import render_template

from database import db, Book, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db" # тут свое название
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

    island = Book(title="Остров Сокровищ", genre=novel)
    db.session.add(island)
    war = Book(title="Война и мир", genre=novel)
    db.session.add(war)
    academy = Book(title="Академия", genre=fantasy)
    db.session.add(academy)

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
