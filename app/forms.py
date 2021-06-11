from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, IntegerField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError, NumberRange, EqualTo
from app.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    fullname = StringField("Full Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phonenumber = StringField("Phone Number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    creditcardnum = StringField("Credit Card Number", validators=[DataRequired()])
    securitycode = StringField("Security Code", validators=[DataRequired()])
    expirationdate = StringField("Credit Card Expiration Date", validators=[DataRequired()])
    
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username already exists. Please choose a different one.")
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email already exists. Please choose a different one.")
    def validate_creditcardnum(self, creditcardnum):
        ccnum = list(creditcardnum.data.strip())
        check_digit = ccnum.pop()
        ccnum.reverse()
        processed_digits = []
        for index, digit in enumerate(ccnum):
            if index % 2 == 0:
                doubled_digit = int(digit) * 2
                if doubled_digit > 9:
                    doubled_digit = doubled_digit - 9
                processed_digits.append(doubled_digit)
            else:
                processed_digits.append(int(digit))
        total = int(check_digit) + sum(processed_digits)
        if total % 10 != 0:
            raise ValidationError("That is an invalid Credit Card number. Please check your input.")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    
    submit = SubmitField("Login")

class UpdateAccountForm(FlaskForm):
    fullname = StringField("Full Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phonenumber = StringField("Phone Number", validators=[DataRequired()])
    picture = FileField("Upload Profile Picture", validators=[FileAllowed(['jpg', 'png'])])
    creditcardnum = StringField("Credit Card Number", validators=[DataRequired()])
    securitycode = StringField("Security Code", validators=[DataRequired()])
    expirationdate = StringField("Credit Card Expiration Date", validators=[DataRequired()])
    
    submit = SubmitField("Update Account")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username already exists. Please choose a different one.")
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email already exists. Please choose a different one.")
    def validate_creditcardnum(self, creditcardnum):
        ccnum = list(creditcardnum.data.strip())
        check_digit = ccnum.pop()
        ccnum.reverse()
        processed_digits = []
        for index, digit in enumerate(ccnum):
            if index % 2 == 0:
                doubled_digit = int(digit) * 2
                if doubled_digit > 9:
                    doubled_digit = doubled_digit - 9
                processed_digits.append(doubled_digit)
            else:
                processed_digits.append(int(digit))
        total = int(check_digit) + sum(processed_digits)
        if total % 10 != 0:
            raise ValidationError("That is an invalid Credit Card number. Please check your input.")

class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Request Password Reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email. You must register first.")

class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Reset Password")

class AddToCartSpecialsForm(FlaskForm):
    quantity = SelectField("Quantity", validators=[DataRequired()], choices=["1", "2", "3", "4", "5"])
    addspecial = SubmitField("Add To Cart")

class AddToCartSweetsForm(FlaskForm):
    quantity = SelectField("Quantity", validators=[DataRequired()], choices=["1", "2", "3", "4", "5"])
    addsweet = SubmitField("Add To Cart")

class AddToCartKhakharasForm(FlaskForm):
    quantity = SelectField("Quantity", validators=[DataRequired()], choices=["1", "2", "3", "4", "5"])
    addkhakhara = SubmitField("Add To Cart")

class AddToCartDrySnacksForm(FlaskForm):
    quantity = SelectField("Quantity", validators=[DataRequired()], choices=["1", "2", "3", "4", "5"])
    adddrysnack = SubmitField("Add To Cart")

class RemoveItemFromCartForm(FlaskForm):
    remove = SubmitField("Remove")

class PurchaseItemForm(FlaskForm):
    submit = SubmitField("Purchase")
    