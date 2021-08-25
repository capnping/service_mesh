from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(60))
    book_price = db.Column(db.Float(precision=2))

    def __repr__(self):
        return self.name
    
