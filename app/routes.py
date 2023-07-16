from app import app, db
from flask import render_template, request, url_for, redirect, session
from app.models import Users, Expenses

from app.forms import Signup
from datetime import date
import os

import bcrypt


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


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = Signup(request.form)

    if form.validate_on_submit():
        form_password = request.values.get("password")
        pw_hash = bcrypt.hashpw(form_password.encode(), bcrypt.gensalt()).decode()
        user = Users(
            email=request.values.get("email"),
            name=request.values.get("name"),
            password_hash=pw_hash,
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")

    else:
        print(form.errors)
        return render_template("signup.html", form=form)
