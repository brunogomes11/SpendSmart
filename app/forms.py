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
from wtforms.fields import EmailField, DateField
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
