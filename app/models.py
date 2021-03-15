from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(25), unique=False, nullable=False)
    lastname = db.Column(db.String(25), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    phonenumber = db.Column(db.Integer, unique=False, nullable=False)

    street = db.Column(db.String(65), unique=False, nullable=False)
    city = db.Column(db.String(65), unique=False, nullable=False)
    state = db.Column(db.String(65), unique=False, nullable=False)
    postalzip = db.Column(db.Integer, unique=False, nullable=False)

    ccnum = db.Column(db.Integer, unique=False, nullable=False)
    seccode = db.Column(db.Integer, unique=False, nullable=False)
    ccexpidate = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.firstname}', '{self.lastname}', '{self.email}', '{self.phonenumber}', '{self.street}', '{self.city}', '{self.state}', '{self.postalzip}', '{self.ccnum}', '{self.seccode}', '{self.ccexpidate}')"