from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    HiddenField,
    SelectField,
    HiddenField,
    EmailField,
    PasswordField,
)
from wtforms.fields import EmailField, DateField, DecimalField
from wtforms.validators import (
    DataRequired,
    Length,
    ValidationError,
    EqualTo,
    InputRequired,
)


class Signup(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    name = StringField("First Name", validators=[DataRequired(), Length(min=4, max=15)])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            InputRequired(),
            EqualTo("confirm", message="Passwords must match."),
            Length(message="Password must be at least 6 characters long.", min=6),
        ],
    )
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("Sign up")


class Login(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
        ],
    )
    submit = SubmitField("Log In")


category_types = [
    ("expenses", "Expenses"),
    ("income", "Income"),
    ("eating_out", "Eating out"),
    ("transport", "Transport"),
    ("fun", "Fun"),
    ("pet", "Pet"),
    ("photo", "Photo"),
    ("gift", "Gift"),
    ("miscellaneous", "Miscellaneous"),
]


class AddExpense(FlaskForm):
    expense_id = HiddenField("id")
    date = DateField(
        "Date",
        format="%Y-%m-%d",
        validators=[DataRequired()],
        render_kw={"placeholder": "DD/MM/YYYY"},
    )
    payee = StringField(
        "Payee",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter payee name"},
    )
    category = SelectField("Category", choices=category_types)
    description = StringField(
        "Description",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter expense description"},
    )
    amount = DecimalField(
        "Amount (A$)",
        validators=[
            DataRequired(message="Invalid amount. Please, introduce a positive number")
        ],
        render_kw={"placeholder": "Enter expense amount"},
    )
    add = SubmitField("Add new expense")

    def validate_amount(self, amount):
        if amount.data <= 0:
            raise ValidationError("Invalid amount. Please, introduce a positive number")


class EditExpense(FlaskForm):
    expense_id = HiddenField("id")
    date = DateField(
        "Date",
        format="%Y-%m-%d",
        validators=[DataRequired()],
    )
    payee = StringField(
        "Payee",
        validators=[DataRequired()],
    )
    category = SelectField("Category", choices=category_types)
    description = StringField(
        "Description",
        validators=[DataRequired()],
    )
    amount = DecimalField(
        "Amount (A$)",
        validators=[
            DataRequired(message="Invalid amount. Please, introduce a positive number")
        ],
    )
    save = SubmitField("Save Changes")
    delete = SubmitField("Delete Expense")

    def validate_amount(self, amount):
        if amount.data <= 0:
            raise ValidationError("Invalid amount. Please, introduce a positive number")


class DateRange(FlaskForm):
    start_date = DateField("Start Date", format="%Y-%m-%d")
    end_date = DateField("End Date", format="%Y-%m-%d")
    submit = SubmitField("Search")

    def validate_end_date(form, field):
        if field.data < form.start_date.data:
            raise ValidationError("End date must not be earlier than start date.")
