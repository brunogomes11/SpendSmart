from app import app, db
from flask import render_template, request, url_for, redirect, session
from app.models import Users, Expenses

# from app.forms AddUser, AddExpense, EditExpense
from datetime import date
import os

# import bcrypt


@app.route("/")
def index():
    users = Users.query.all()
    return render_template("home.html", users=users)


@app.route("/login")
def login():
    return render_template("login.html")


# @app.route("/login", methods=["POST"])
# def login_action():
#     email = request.form.get("email")
#     password = request.form.get("password")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_action():
    # pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    ##push to the database
    ##STILL NEED TO CREATE
    # user.signup(name=name, email=email, pw_hash=pw_hash)

    return redirect("/login")
