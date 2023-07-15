from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    HiddenField,
    SelectField,
    FloatField,
    HiddenField,
)
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Length, ValidationError
