# :moneybag:[SpendSmart](https://spendsmart-2n0e.onrender.com/):moneybag:

## created by Bruno Gomes

-   email: guest@guest.com
-   password: 123456

Application deployed :arrow_forward: [click here](https://spendsmart-2n0e.onrender.com/) :arrow_backward:

<img src="img/banner.png" width="600" height="300">

My project is SpendSmart, a user-friendly web application designed to help individuals manage their finances effectively. Its intuitive interface and comprehensive features allow users to easily track their expenses, record income, and gain valuable insights into their spending habits. The app allows users to create, edit, and delete expense records, view detailed graphs, and monitor their financial progress effortlessly. **SpendSmart** empowers users to take control of their finances and make informed decisions, ensuring a more organized and efficient approach to managing their day-to-day expenses.

# Documentation

-   **Full-stack database-backed application** with full **CRUD** (Create, Read, Update, Delete) functionality

## Technologies Used

1. HTML <img src="img/html-5.png" width="30" height="30">
2. CSS <img src="img/css-3.png" width="30" height="30">
3. Javascript <img src="img/js.png" width="30" height="30">
4. Python <img src="img/python.png" width="30" height="30">
5. Flask <img src="img/flask2.png" width="30" height="30">
6. postgreSQL <img src="img/postgresql.png" width="30" height="30">
7. SQLAlchemy <img src="img/sqlalchemy.png" width="40" height="40">
8. WTForms <img src="img/wt.png" width="30" height="30">
9. Chart.js <img src="img/chart.png" width="30" height="30">
10. Bcrypt <img src="img/bcrypt2.png" width="30" height="30">
11. Git <img src="img/git.png" width="30" height="30">
12. VSCode <img src="img/vscode.png" width="30" height="30">
13. [Render.com](https://render.com/)

## Main Features

1.  User can create an account (**signup**) with email, name and password.
2.  Secure **login** with email and password.
3.  Expenses page displaying **total income**, **total expenses**, **net balance**, and **all transactions** (add/edit/delete).
4.  **Insert, update or delete expenses** (date, payee, category, description, amount)
5.  Dashboard with graphs: **Income/Expenses**, **Expenses Over Time**, **Category Expenses.**
6.  Expenses by Category graph clickable to view detailed expenses for each category
7.  Logout

## User Stories

<img src="img/user-stories.png" width="800" height="400">

## Data Model

The following diagram shows which tables will be created and their relationship (One to Many).

The application has two tables: Users and Expenses.

-   **Users** will store the personal data of our users, such as their name and email
-   **Expenses** will store the information about the type of expenses of each user, a description, the date of purchase/expense and finally, the amount spent.

<img src="img/data-models.png" width="600" height="300">

## Approach Taken

In my Expense Tracker project, I utilized Flask, a lightweight Python web framework that provides essential tools and features for developing web applications using Python.

1. Database Modeling and Setup:

-   I began the project by designing the database schema. I created two tables using PostgreSQL via the terminal: Users and Expenses. To interact with the database in a more Pythonic way, I chose SQLAlchemy, an Object Relational Mapper (ORM). SQLAlchemy allows developers to work with Python objects instead of writing raw SQL queries. This combination of Flask and SQLAlchemy proved highly efficient for database interactions, ensuring a smooth experience.

2. Signup/Login Forms using WTForms:

-   To implement secure and flexible form validation, I adopted WTForms, a library that guards against potential vulnerabilities like CSRF attacks. I structured my forms as classes, creating Signup, Login, AddExpense, EditExpense, and DateRange classes. To store passwords safely in the database, I integrated the bcrypt library.

3. Code example for Editing Expenses:

-   One of the highlights of my project was the seamless expense editing process. To achieve this, I employed SQLAlchemy and WTForms together. Here's the process:
    -   I retrieved the expense to edit using SQLAlchemy with a SQL query based on the expense_id
    -   Once I confirmed the existence of the expense, I populated the EditExpense form with the expense's data using the `obj` parameter. Matching form field names to database columns facilitated automatic form population.
    -   By validating the form on submission with `form.validate_on_submit()`, I ensured proper data validation and processing when the form was submitted via the "POST" method.
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
    -   I used `payee=form.payee.data` to retrieve the corresponding data for adding expenses.

5. Dashboard and Visualization:

-   The application's dashboard presented an appealing visualization of expenses. Using Chart.js, a JavaScript library, I created interactive graphs that allowed users to explore their expenses in detail. Clickable charts provide more in-depth insights into a user's financial data.

6. Sorting and Financial Summary:

-   To facilitate better analysis, I implemented a sorting feature in the table to view expenses by date. Additionally, I displayed essential financial metrics like "total income," "total expenses," and "net balance" for a quick overview of one's finances.

7. Styling:

-   I followed a functional-first approach and prioritized implementing core functionalities before focusing on styling. Once the core elements were working, I styled the application using CSS. I applied styling to various components, including the navigation bar, home banner, footer, tables, forms, and graphs, enhancing the user experience.
-   Colours used from [Coolors](https://coolors.co/306b34-222e50-573112-bfd7ea-ff5a5f) :

    -   ![#454545](https://placehold.co/15x15/454545/454545.png) `#454545`
    -   ![#50A060](https://placehold.co/15x15/50A060/50A060.png) `#50A060`
    -   ![#F5E6E8](https://placehold.co/15x15/F5E6E8/F5E6E8.png) `#F5E6E8`
    -   ![#5DB7DE](https://placehold.co/15x15/5DB7DE/5DB7DE.png) `#5DB7DE`
    -   ![#FE5E41](https://placehold.co/15x15/FE5E41/FE5E41.png) `#FE5E41`

-   Font Family from [Google Fonts](https://fonts.google.com/):
    -   [Krona One](https://fonts.google.com/specimen/Krona+One?query=Krona+on)

## Unsolved Problems

-   Make CSS Responsive
-   Implement access control

## Future Improvements

1. Improve CSS responsiveness - The button and banner on the home page are not responsive for smaller screens.
2. Signup/Login button on the home page appears on the burger icon for the smaller screen.
3. Create a guest user on the login form.
4. Implement forgot password on the login form
5. Implement API for signing in with different methods
6. Implement Admin functionalities for managing users and expenses.
