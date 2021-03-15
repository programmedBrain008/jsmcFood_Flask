from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import environ
from flask_session import Session
import redis

app = Flask(__name__)
app.config["SECRET_KEY"] = "77ffb88e52a3460be3304a3c752c8ecf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes