from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    HiddenField,
    SelectField,
    FloatField,
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


category_type = [
    "Expenses",
    "Eating out",
    "Transport",
    "Fun",
    "Pet",
    "Photo",
    "Gift",
    "Miscellaneous",
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
    category = SelectField("Category", choices=[(typ, typ) for typ in category_type])
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
    category = SelectField("Category", choices=[(typ, typ) for typ in category_type])
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
