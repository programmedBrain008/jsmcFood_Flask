from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, ValidationError, NumberRange
from app.models import User
import email_validator

class orderForm(FlaskForm):
    firstname = StringField("First Name", validators=[DataRequired(), Length(min=2, max=25)])
    lastname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phonenumber = StringField("Phone Number", validators=[DataRequired()])
    
    street = StringField("Street", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    state = StringField("State / Province", validators=[DataRequired()])
    postalzip = StringField("Postal / Zip Code", validators=[DataRequired()])
    
    ccnum = StringField("Credit Card Number", validators=[DataRequired()])
    seccode = StringField("Security Code", validators=[DataRequired()])
    ccexpidate = StringField("Credit Card Expiration Date", validators=[DataRequired()])
       
    submit = SubmitField("Place Order Now!")