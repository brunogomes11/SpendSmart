from app import app, db
from flask import render_template, request, redirect, session, flash
from app.models import Users, Expenses
from app.forms import Signup, Login, AddExpense, EditExpense
from datetime import datetime, timedelta
import bcrypt
from sqlalchemy.sql import func
from sqlalchemy import text


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
                return redirect("/expenses")
        flash("Email address or password is incorrect. Please try again.", "error")
        return redirect("/login")  ## DISPLAY EXPENSES
    else:
        return render_template("login.html", form=form)


## LOGOUT ##
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


## SHOW EXPENSES ##
@app.route("/expenses")
def show_expenses():
    user_id = session.get("id")
    user_expenses = (
        db.session.query(Expenses).join(Users).filter(Users.id == user_id).all()
    )

    if user_expenses == []:
        return render_template("expenses.html", user_id=user_id)
    else:
        expenses = (
            db.session.query(Expenses)
            .filter(Expenses.user_id == user_id, Expenses.category != "Income")
            .all()
        )

        income = (
            db.session.query(Expenses)
            .filter(Expenses.user_id == user_id, Expenses.category == "Income")
            .all()
        )

        total_expense = 0
        for data in expenses:
            total_expense += data.amount
        total_expense = round(total_expense, 2)

        total_income = 0
        for data in income:
            total_income += data.amount
        total_income = round(total_income, 2)

        net_balance = total_income - total_expense

        return render_template(
            "expenses.html",
            expenses=user_expenses,
            total_expense=total_expense,
            total_income=total_income,
            net_balance=net_balance,
        )


## ADD EXPENSES ##
@app.route("/add_expense", methods=["GET", "POST"])
def add_expense():
    user_id = session.get("id")

    form = AddExpense()

    # POST
    if form.validate_on_submit():
        new_expense = Expenses(
            date=form.date.data,
            payee=form.payee.data,
            category=form.category.data,
            description=form.description.data,
            amount=form.amount.data,
            user_id=user_id,
        )

        db.session.add(new_expense)
        db.session.commit()

        return redirect("/expenses")
    else:
        ## GET ##
        return render_template("add_expense.html", form=form)


## EDIT ##
@app.route("/edit_expense/<int:expense_id>", methods=["GET", "POST"])
def edit_expense(expense_id):
    # user_id = session.get("id")

    expense = (
        db.session.query(Expenses).filter(Expenses.expense_id == expense_id).first()
    )

    ## Display the form with populate fields
    if expense:
        form = EditExpense(
            obj=expense
        )  ## This is really great, it automatically populate the form with the database obj

        if form.validate_on_submit():
            if form.save.data:
                form.populate_obj(expense)
                db.session.commit()
                return redirect("/expenses")
            elif form.delete.data:
                db.session.delete(expense)
                db.session.commit()
                return redirect("/expenses")
        return render_template("edit_expense.html", form=form, expense_id=expense_id)


@app.route("/dashboard")
def dashboard():
    user_id = session.get("id")

    ## SETUP GRAPH FOR INCOME/EXPENSES

    # Get only the category INCOME and the total amount of incomes
    income = (
        db.session.query(Expenses.category, func.sum(Expenses.amount).label("total"))
        .filter(Expenses.user_id == user_id)
        .filter(Expenses.category == "Income")
        .group_by(Expenses.category)
        .all()
    )

    # Get all the categories excluding Income and sum all the amount
    expenses = (
        db.session.query(func.sum(Expenses.amount).label("total"))
        .filter(Expenses.user_id == user_id)
        .filter(Expenses.category != "Income")
        .all()
    )

    income_values = [row[1] for row in income]  ##TOTAL INCOME
    print(income_values)

    expense_values = [row[0] for row in expenses]  ##TOTAL EXPENSES
    print(expense_values)

    ##SPEND BY DATE
    dates = (
        db.session.query(func.sum(Expenses.amount), Expenses.date)
        .filter(Expenses.category != "Income")
        .group_by(Expenses.date)
        .order_by(Expenses.date)
        .all()
    )

    amount_by_date = []
    date_label = []
    for amount, date in dates:
        amount_by_date.append(amount)
        date_label.append(date.strftime("%d-%m-%Y"))
    print(amount_by_date)
    print(date_label)

    ##INCOME VS CATEGORY

    category_comparison = (
        db.session.query(func.sum(Expenses.amount), Expenses.category)
        .filter(Expenses.category != "Income")
        .group_by(Expenses.category)
        .order_by(Expenses.category)
        .all()
    )

    category_amount = []
    category_names = []
    for amount, name in category_comparison:
        category_amount.append(amount)
        category_names.append(name)

    print(category_amount)
    print(category_names)
    ##DISPLAY TOTAL BY CATEGORY

    results = (
        db.session.query(Expenses.category, func.sum(Expenses.amount).label("total"))
        .filter(Expenses.user_id == user_id)
        .group_by(Expenses.category)
        .order_by(func.sum(Expenses.amount).desc())
        .all()
    )
    return render_template(
        "dashboard.html",
        results=results,
        income_values=income_values,
        expense_values=expense_values,
        amount_by_date=amount_by_date,
        date_label=date_label,
        category_amount=category_amount,
        category_names=category_names,
    )


@app.route("/category/<category>")
def category(category):
    user_id = session.get("id")
    results = (
        db.session.query(Expenses.date, Expenses.payee, Expenses.amount)
        .filter(Expenses.user_id == user_id)
        .filter(Expenses.category == category)
        .all()
    )

    return render_template("category.html", results=results)


@app.route("/weekly")
def weekly():
    user_id = session.get("id")
    today = datetime.today().date()
    end_date = today
    start_date = end_date - timedelta(days=7)

    results = (
        db.session.query(Expenses.date, Expenses.payee, Expenses.amount)
        .filter(Expenses.date >= start_date)
        .filter(Expenses.user_id == user_id)
        .order_by(Expenses.date.asc())
        .all()
    )

    results_expenses = (
        db.session.query(Expenses.date, Expenses.payee, Expenses.amount)
        .filter(Expenses.date >= start_date)
        .filter(Expenses.user_id == user_id)
        .order_by(Expenses.date.asc())
        .filter(Expenses.category != "Income")
        .all()
    )

    results_income = (
        db.session.query(Expenses.date, Expenses.payee, Expenses.amount)
        .filter(Expenses.date >= start_date)
        .filter(Expenses.user_id == user_id)
        .order_by(Expenses.date.asc())
        .filter(Expenses.category == "Income")
        .all()
    )

    total_income = 0
    for data in results_income:
        data.amount
        total_income += data.amount
    total_income = round(total_income, 2)

    total_expense = 0
    for data in results_expenses:
        data.amount
        total_expense += data.amount
    total_expense = round(total_expense, 2)

    total = total_income - total_expense

    return render_template("weekly.html", results=results, total=total)
