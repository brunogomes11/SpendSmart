from app import app, db
from flask import render_template, request, url_for, redirect, session, flash
from app.models import Users, Expenses
from app.forms import Signup, Login
from datetime import date
import os
import bcrypt

# Flash message
app.secret_key = "hello123"


## HOME ROUTE ##
@app.route("/")
def index():
    return render_template("home.html")


## SIGNUP ##
@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = Signup(request.form)  ## Signup class from WTForms passing the

    ## POST ##
    if form.validate_on_submit():
        form_password = request.values.get("password")  # Getting password from form
        pw_hash = bcrypt.hashpw(
            form_password.encode(), bcrypt.gensalt()
        ).decode()  # Encrypting password
        user = Users(
            email=request.values.get("email"),
            name=request.values.get("name"),
            password_hash=pw_hash,
        )  # Passing objects to class Users from the signup form
        db.session.add(user)  ## SQLAlchemy to add to the table
        db.session.commit()  ##SQLAlchemy to commit changes to database
        return redirect("/login")

    else:
        ## GET ##
        print(form.errors)
        return render_template("signup.html", form=form)


## LOGIN ##
@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login(request.form)

    if request.method == "POST":
        result = Users.query.all()

        email_form = request.values.get("email")
        password_form = request.values.get("password")

        for user in result:
            user_id = user.id
            admin = user.admin
            name = user.name
            email = user.email
            hashed_password = user.password_hash

            check_pw = bcrypt.checkpw(password_form.encode(), hashed_password.encode())

            if email_form == email and check_pw:
                session["id"] = user_id
                session["name"] = name
                session["admin"] = admin
                return redirect("/")
        flash("Email address or password is incorrect. Please try again.", "error")
        return redirect("/login")
    else:
        return render_template("login.html", form=form)


## LOGOUT ##
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
