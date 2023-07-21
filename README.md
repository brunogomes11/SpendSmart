# :moneybag:SpendSmart:moneybag:

## created by Bruno Gomes

<img src="static/banner.png" width="600" height="300">

My project is called SpendSmart, a user-friendly web application designed to help individuals effectively manage their personal finances. With its intuitive interface and comprehensive features, users can easily track their expenses, record income, and gain valuable insights into their spending habits. The app allows users to create, edit, and delete expense records, view detailed graphs, and effortlessly monitor their financial progress. **SpendSmart** empowers users to take control of their finances and make informed decisions, ensuring a more organized and efficient approach to managing their day-to-day expenses.

# Documentation

-   **full-stack database-backed application** with full **CRUD** (Create, Read, Update, Delete) functionality

## Technologies Used

1. HTML <img src="img/html-5.png" width="30" height="30">
2. CSS <img src="img/css-3.png" width="30" height="30">
3. Javascript <img src="img/js.png" width="30" height="30">
4. Python
5. Flask
6. postgreSQL
7. SQLAlchemy
8. WTForms
9. Chart.js
10. Bcrypt
11. Git
12. VSCode

## Main Features

1.  User can create an account (**signup**) with email, name and password.
2.  Secure **login** with email and password.
3.  Expenses page displaying **total income**, **total expenses**, **net balance**, and **all transactions** (add/edit/delete).
4.  **Insert, update or delete expenses** (date, payee, category, description, amount)
5.  Dashboard with graphs: **Income/Expenses**, **Expenses Over Time**, **Category Expenses.**
6.  Expenses by Category graph clickable to view detailed expense for each category
7.  Logout

## User Stories

PICTURE

## Data Model

The following diagram shows which tables will be created and what is their relationship (One to Many).

The application has two tables: Users and Expenses.

-   **Users** will store the personal data of our user such as their name and email
-   **Expenses** will store the information about the type of expenses of each user, a description, the date of purchase/expense and finally the amount spent.

PICTURE

## Approach Taken

In my Expense Tracker project, I utilized Flask, a lightweight Python web framework, which provides essential tools and features for developing web applications using the Python language.

1. Database Modeling and Setup:

-   I began the project by designing the database schema. Using PostgreSQL via the terminal, I created two tables: Users and Expenses. To interact with the database in a more Pythonic way, I chose SQLAlchemy, an Object Relational Mapper (ORM). SQLAlchemy allows developers to work with Python objects instead of writing raw SQL queries. This combination of Flask and SQLAlchemy proved highly efficient for database interactions, ensuring a smooth experience.

2. Signup/Login Forms using WTForms:

-   To implement secure and flexible form validation, I adopted WTForms, a library that guards against potential vulnerabilities like CSRF attacks. I structured my forms as classes, creating Signup, Login, AddExpense, EditExpense, and DateRange classes. To store passwords safely in the database, I integrated the bcrypt library.

3. Code example for Editing Expenses:

-   One of the highlights of my project was the seamless expense editing process. To achieve this, I employed SQLAlchemy and WTForms together. Here's the process:
    -   I retrieved the expense to edit using SQLAlchemy with a SQL query based on the expense_id
    -   Once I confirmed the existence of the expense, I populated the EditExpense form with the expense's data using the `obj` parameter. Matching form field names to database columns facilitated automatic form population.
    -   By validating the form on submission with `form.validate_on_submit()`, I ensured proper data validation and processing when the form is submitted via the "POST" method.
    -   When the user clicked to save the edited expense (`form.save.data`), I updated the expense object with the data from the submitted form using `form.populate_obj(expense)`.
    -   To permanently save the changes to the expense in the database, I committed the transaction with `db.session.commit()`.
    -   Finally, after successfully saving the edited expense, I redirected the user to the "/expenses" URL or page.

```
expense  = (db.session.query(Expenses).filter(Expenses.expense_id  ==  expense_id).first())

if  expense:
	form  =  EditExpense(obj=expense)

	if  form.validate_on_submit():
		if  form.save.data:
		form.populate_obj(expense)
		db.session.commit()
		return  redirect("/expenses")
```

4. Different Approaches for Data Handling:

-   I used two distinct methods for handling form data and pushing it to the database based on the context:
    -   For user signup, I extracted the form values using `email=request.form.get("email")`.
    -   For adding expenses, I utilized `payee=form.payee.data` to retrieve the corresponding data.

5. Dashboard and Visualization:

-   The application's dashboard presented an appealing visualization of expenses. Using Chart.js, a JavaScript library, I created interactive graphs that allowed users to explore their expenses in detail. Clickable charts provided more in-depth insights into a user's financial data.

6. Sorting and Financial Summary:

-   To facilitate better analysis, I implemented a sorting feature in the table to view expenses by date. Additionally, I displayed essential financial metrics like "total income," "total expenses," and "net balance" for a quick overview of one's finances.

7. Styling:

-   I followed a functional-first approach and prioritized implementing core functionalities before focusing on styling. Once the core elements were working, I styled the application using CSS. I applied styling to various components, including the navigation bar, home banner, footer, tables, forms, and graphs, enhancing the user experience.
-   Colours used from [Coolors](https://coolors.co/306b34-222e50-573112-bfd7ea-ff5a5f) : - ![#573112](https://placehold.co/15x15/573112/573112.png) `#573112` - ![#306B34](https://placehold.co/15x15/306B34/306B34.png) `#306B34` - ![#222E50](https://placehold.co/15x15/222E50/222E50.png) `#222E50` - ![#BFD7EA](https://placehold.co/15x15/BFD7EA/BFD7EA.png) `#BFD7EA` - ![#FF5A5F](https://placehold.co/15x15/FF5A5F/FF5A5F.png) `#FF5A5F` - ![#C5C51D](https://placehold.co/15x15/C5C51D/C5C51D.png) `#C5C51D`
-   Font Family from [FontSpace](https://www.fontspace.com/):
    -   [Game Played](https://www.fontspace.com/game-played-font-f31380)
    -   [Nintendo](https://www.fontspace.com/snes-font-f26537)

## Unsolved Problems

## Future Improviments

1. Improve CSS responsiveness - The button and banner on the home page its not responsive for smaller screens.
2. Signup/Login button on home page appear on the burger icon for smaller screen.
3. Create a guest user on the login form.
4. Implement forgot password on login form
5. Implement API for signing in with different methods
6. Implement Admin functionalities for manage users and expenses.
