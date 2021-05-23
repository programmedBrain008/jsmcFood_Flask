from app import db, login_manager, app
from flask_login import UserMixin
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    products = db.relationship("Cart", backref="buyer", lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    priceForEach = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Cart('{self.name}', '{self.date_added}')"

class SpecialsProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.String(200), nullable=False)
    priceForEach = db.Column(db.String(200), nullable=False)
    

    def __repr__(self):
        return f"{self.name}"

class DrySnacksProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.String(200), nullable=False)
    priceForEach = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.name}"

class SweetsProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.String(200), nullable=False)
    priceForEach = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.name}"

class KhakharasProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.String(200), nullable=False)
    priceForEach = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.name}"

