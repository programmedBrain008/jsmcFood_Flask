from flask import url_for, render_template, request, redirect, flash, session
from app import app, db, bcrypt, mail
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm, AddToCartSpecialsForm, AddToCartSweetsForm, AddToCartKhakharasForm, AddToCartDrySnacksForm, RemoveItemFromCartForm, PurchaseItemForm
from app.models import db, User, Cart, SpecialsProduct, DrySnacksProduct, SweetsProduct, KhakharasProduct
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
from flask_mail import Message


@app.route("/", methods=["GET", "POST"])
def snackPage():
    specialsform = AddToCartSpecialsForm()
    sweetsform = AddToCartSweetsForm()
    khakharasform = AddToCartKhakharasForm()
    drysnacksform = AddToCartDrySnacksForm()
    user_cart = Cart.query.all()
    if request.method == "POST":
        if request.form.get('itemaddedtospecialscart'):
            added_specials_product = request.form.get('itemaddedtospecialscart')
            already_exists_in_cart = Cart.query.filter_by(name=added_specials_product).first()
            if already_exists_in_cart:
                flash("The item you tried to add already exists in your cart. To continue this action, remove the item from your cart, and try again.", "danger")
                return redirect(url_for('cart'))
            else:
                added_specials_product_object = SpecialsProduct.query.filter_by(name=added_specials_product).first()
                specialsform = AddToCartSpecialsForm()
                product_name = str(added_specials_product_object.name)
                product_amount = str(added_specials_product_object.amount)
                product_price = float(added_specials_product_object.priceForEach)
                quantity_of_product = specialsform.quantity.data
                total_price = product_price * int(quantity_of_product)
                buyer = current_user.id
                cart_product = Cart(name=product_name, amount=product_amount, priceForEach=product_price, quantity=quantity_of_product, total_price=total_price, user_id=buyer)
                db.session.add(cart_product)
                db.session.commit()
                flash(f"You have successfully added {product_name} to your cart!", "success")
        if request.form.get('itemaddedtosweetscart'):
            added_sweets_product = request.form.get('itemaddedtosweetscart')
            already_exists_in_cart = Cart.query.filter_by(name=added_sweets_product).first()
            if already_exists_in_cart:
                flash("The item you tried to add already exists in your cart. To continue this action, remove the item from your cart, and try again.", "danger")
                return redirect(url_for('cart'))
            else:
                added_sweets_product_object = SweetsProduct.query.filter_by(name=added_sweets_product).first()
                sweetsform = AddToCartSweetsForm()
                product_name = str(added_sweets_product_object.name)
                product_amount = str(added_sweets_product_object.amount)
                product_price = float(added_sweets_product_object.priceForEach)
                quantity_of_product = sweetsform.quantity.data
                total_price = product_price * int(quantity_of_product)
                buyer = current_user.id
                cart_product = Cart(name=product_name, amount=product_amount, priceForEach=product_price, quantity=quantity_of_product, total_price=total_price, user_id=buyer)
                db.session.add(cart_product)
                db.session.commit()
                flash(f"You have successfully added {product_name} to your cart!", "success")
        if request.form.get('itemaddedtokhakharascart'):
            added_khakharas_product = request.form.get('itemaddedtokhakharascart')
            already_exists_in_cart = Cart.query.filter_by(name=added_khakharas_product).first()
            if already_exists_in_cart:
                flash("The item you tried to add already exists in your cart. To continue this action, remove the item from your cart, and try again.", "danger")
                return redirect(url_for('cart'))
            else:
                added_khakharas_product_object = KhakharasProduct.query.filter_by(name=added_khakharas_product).first()
                product_name = str(added_khakharas_product_object.name)
                product_amount = str(added_khakharas_product_object.amount)
                product_price = float(added_khakharas_product_object.priceForEach)
                quantity_of_product = khakharasform.quantity.data
                total_price = product_price * int(quantity_of_product)
                buyer = current_user.id
                cart_product = Cart(name=product_name, amount=product_amount, priceForEach=product_price, quantity=quantity_of_product, total_price=total_price, user_id=buyer)
                db.session.add(cart_product)
                db.session.commit()
                flash(f"You have successfully added {product_name} to your cart!", "success")  
        if request.form.get('itemaddedtodrysnackscart'):
            added_drysnacks_product = request.form.get('itemaddedtodrysnackscart')
            already_exists_in_cart = Cart.query.filter_by(name=added_drysnacks_product).first()
            if already_exists_in_cart:
                flash("The item you tried to add already exists in your cart. To continue this action, remove the item from your cart, and try again.", "danger")
                return redirect(url_for('cart'))
            else:
                added_drysnacks_product_object = DrySnacksProduct.query.filter_by(name=added_drysnacks_product).first()
                product_name = str(added_drysnacks_product_object.name)
                product_amount = str(added_drysnacks_product_object.amount)
                product_price = float(added_drysnacks_product_object.priceForEach)
                quantity_of_product = drysnacksform.quantity.data
                total_price = product_price * int(quantity_of_product)
                buyer = current_user.id
                cart_product = Cart(name=product_name, amount=product_amount, priceForEach=product_price, quantity=quantity_of_product, total_price=total_price, user_id=buyer)
                db.session.add(cart_product)
                db.session.commit()
                flash(f"You have successfully added {product_name} to your cart!", "success")
        return redirect(url_for('snackPage'))
    
    elif request.method == "GET":
        specials = SpecialsProduct.query.all()
        sweets = SweetsProduct.query.all()
        khakharas = KhakharasProduct.query.all()
        drysnacks = DrySnacksProduct.query.all()
        user_cart = Cart.query.all()
        num_of_items = len(user_cart)

        return render_template("index.html", specials=specials, sweets=sweets, khakharas=khakharas, drysnacks=drysnacks, specialsform=specialsform, sweetsform=sweetsform, khakharasform=khakharasform, drysnacksform=drysnacksform, user_cart=user_cart, item_counter=num_of_items)

@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    removeitemform = RemoveItemFromCartForm()
    user_cart = Cart.query.all()

    if request.method == "POST":
        if request.form.get('deleteitemincartbutton'):
            removal_item = request.form.get('deleteitemincartbutton')
            db_removal_item = Cart.query.filter_by(name=removal_item).first()
            db.session.delete(db_removal_item)
            db.session.commit()
            return redirect(url_for('cart'))
        if request.form.get('updatequantitybutton'):
            return redirect(url_for('cart'))

    elif request.method == "GET":
        removeitemform = RemoveItemFromCartForm()
        user_cart = Cart.query.all()
        total_price = 0.0
        for item in user_cart:
            total_price = item.total_price + total_price
        
        return render_template("cart.html", user_cart=user_cart, removeitemform=removeitemform, total_price=total_price)

@app.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
    user_cart = Cart.query.all()
    users = User.query.all()
    purchase_form = PurchaseItemForm()
    total_price = 0.0
    for item in user_cart:
        total_price = item.total_price + total_price

    return render_template("checkout.html", user_cart=user_cart, total_price=total_price, current_user=current_user, purchase_form=purchase_form)

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('snackPage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(fullname=form.fullname.data, username=form.username.data, email=form.email.data, phonenumber=form.phonenumber.data,password=hashed_password, creditcardnum=form.creditcardnum.data, securitycode=form.securitycode.data, expirationdate=form.expirationdate.data)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created successfully! Login with your newly created account.", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('snackPage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("snackPage"))
        else:
            flash("Login unsucessful. Please check email and password.", "danger")
            
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("snackPage"))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + str(f_ext)
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.fullname = form.fullname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.phonenumber = form.phonenumber.data
        current_user.creditcardnum = form.creditcardnum.data
        current_user.securitycode = form.securitycode.data
        current_user.expirationdate = form.expirationdate.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("account"))
    elif request.method == "GET":
        form.fullname.data = current_user.fullname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.phonenumber.data = current_user.phonenumber
        form.creditcardnum.data = current_user.creditcardnum
        form.securitycode.data = current_user.securitycode
        form.expirationdate.data = current_user.expirationdate
    image_file = url_for('static', filename='profile_pics/' + str(current_user.image_file))
    return render_template("account.html", title="Account", image_file=image_file, form=form)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender="aaravshah.300@gmail.com", recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for("reset_token", token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

@app.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("snackPage"))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("An email has been sent with instructions to reset your password.", "info")
        return redirect(url_for("login"))
    return render_template("reset_request.html", title="Reset Password", form=form)

@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("snackPage"))
    user = User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid or expired token.", "warning")
        return redirect(url_for("reset_request"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user.password = hashed_password
        db.session.commit()
        flash("Your password has been reset! You are now able to login.", "success")
        return redirect(url_for('login'))

    return render_template("reset_token.html", title="Reset Password", form=form)

