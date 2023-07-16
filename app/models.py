from app import db
import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String)
    admin = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String, nullable=False)


class Expenses(db.Model):
    expense_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    date = db.Column(db.String, nullable=False)
    payee = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)
