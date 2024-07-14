from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete='SET NULL'))
    genre = relationship("Genre", back_populates="books")

    def __repr__(self):
        return f"User(title={self.title!r})"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    books = relationship(
        "Book", back_populates="genre"
    )


