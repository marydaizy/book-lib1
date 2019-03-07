from datetime import datetime
from books import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # book = db.relationship('Books', backref='author', lazy=True)
    

   



class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(60), nullable=False)
    year = db.Column(db.Integer, primary_key=True)

    

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reviews= db.Column(db.Integer, nullable=False)
    book_id=db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment=db.Column(db.String(), nullable=False)



    def __str__(self):
        return self.title