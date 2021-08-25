from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60))
    author = db.Column(db.String(60))
    publisher = db.Column(db.String(60))
    is_available = db.Column(db.Boolean)

    def __repr__(self):
        return self.name


class Prices(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #book_id = db.Column(db.Integer)
    book_name = db.Column(db.String(60))

    book_price = db.Column(db.Float(precision=2))

    def __repr__(self):
        return self.name
    