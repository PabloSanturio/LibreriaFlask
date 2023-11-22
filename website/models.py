from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    autor = db.Column(db.String(256), nullable=False)
    tema = db.Column(db.String(256), nullable=False)
    idioma = db.Column(db.String(256), nullable=False)
    encuadernacion = db.Column(db.String(256), nullable=False)
    paginas = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
   