from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("config")

app.config["SQLALCHEMY_DATABASE_URI"]
db = SQLAlchemy(app)

from app import routes
