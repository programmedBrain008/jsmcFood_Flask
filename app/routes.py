from flask import url_for, render_template, request, redirect, flash, session
from app import app, db, bcrypt
from app.forms import orderForm
from app.models import db, User, ProductRecord
from app.productInfo import jekh, kmkh, makh, jmkh, plkh, amkh, mekh, plpa, mapa, plse, homi, kmmi, sumi, pach, mepa, stga, bhga, ph, bsbh, rase, rach, sspa, drka, bh, vaga, sh, guja, ragu, gcla, ma, lunchSpecial, basundi, bhajinabhajiya


@app.route("/", methods=["GET", "POST"])
def snackPage():

    def addToCart(getMethodName, amount, priceForEach):
        if request.form.get(str(getMethodName)):
            print(getMethodName + " has been added to cart database.")
            product = ProductRecord(name=getMethodName, amount=amount, priceForEach=priceForEach)
            
            db.session.add(product)
            db.session.commit()
            flash(f"{getMethodName} has been added to your cart!", "success")
            return redirect(url_for("snackPage"))

    if request.method == "POST":
        addToCart("lunchSpecial", "Includes: Basundi, Bhaji na Bhajiya, Bhinda-Capsicum-Tomato-Shaak, Kala Chana, Puri, Jeera Rice, Dal Fry", 10)
        addToCart("basundi", "1 LB", 6.00)
        addToCart("bhajinabhajiya", "8pcs", 4.00)
        addToCart("sh", "1 LB", 6.00)
        addToCart("guja", "1 LB", 6.00)
        addToCart("ragu", "8pcs", 4.00)
        addToCart("gcla", "1 LB", 6.00)
        addToCart("ma", "14 OZ", 6.00)
        addToCart("jekh", "500g", 4.00)
        addToCart("kmkh", "500g", 4.00)
        addToCart("makh", "200g", 1.50)
        addToCart("jmkh", "200g", 1.50)
        addToCart("plkh", "200g", 1.50)
        addToCart("amkh", "200g", 1.50)
        addToCart("mekh", "200g", 1.50)
        addToCart("plpa", "9 OZ", 3)
        addToCart("mapa", "9 OZ", 3)
        addToCart("plse", "12 OZ", 3)
        addToCart("homi", "12 OZ", 3)
        addToCart("kmmi", "12 OZ", 3)
        addToCart("sumi", "12 OZ", 3)
        addToCart("pach", "12 OZ", 3)
        addToCart("mepa", "12 OZ", 3)
        addToCart("stga", "11 OZ", 3)
        addToCart("bhga", "12 OZ", 3)
        addToCart("ph", "11 OZ", 3)
        addToCart("bshb", "12 OZ", 3)
        addToCart("rase", "12 OZ", 3)
        addToCart("rach", "12 OZ", 3)
        addToCart("sspa", "11 OZ", 3)
        addToCart("drka", "11 OZ", 3)
        addToCart("bh", "11 OZ", 3)
        addToCart("vaga", "12 OZ", 3)

    return render_template("index.html", jekh=jekh, kmkh=kmkh, makh=makh, jmkh=jmkh, plkh=plkh, amkh=amkh, mekh=mekh, 
    plpa=plpa, mapa=mapa, plse=plse, homi=homi, kmmi=kmmi, sumi=sumi, pach=pach, mepa=mepa, stga=stga, bhga=bhga,
    ph=ph, bsbh=bsbh, rase=rase, rach=rach, sspa=sspa, drka=drka, bh=bh, vaga=vaga, sh=sh, guja=guja, ragu=ragu,
    gcla=gcla, ma=ma, lunchSpecial=lunchSpecial, basundi=basundi, bhajinabhajiya=bhajinabhajiya)

@app.route("/order", methods=["GET", "POST"])
def order():
    form = orderForm()
    if form.validate_on_submit():
        REF_firstname = form.firstname.data
        REF_lastname = form.lastname.data
        REF_email = form.email.data
        REF_phonenumber = form.phonenumber.data
        REF_street = form.street.data
        REF_city = form.city.data
        REF_state = form.state.data
        REF_postalzip = form.postalzip.data
        REF_ccnum = form.ccnum.data
        REF_seccode = form.seccode.data
        REF_ccexpidate = form.ccexpidate.data

        user = User(firstname=REF_firstname, lastname=REF_lastname, email=REF_email, 
                    phonenumber=REF_phonenumber, street=REF_street, city=REF_city, 
                    state=REF_state, postalzip=REF_postalzip, ccnum=REF_ccnum, 
                    seccode=REF_seccode, ccexpidate=REF_ccexpidate)
        db.session.add(user)
        db.session.commit()
        flash(f"Order placed successfully for: {REF_firstname} {REF_lastname}", "success")
        return redirect(url_for("snackPage"))

    return render_template("order_form.html", form=form)
