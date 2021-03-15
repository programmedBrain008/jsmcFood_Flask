from flask import url_for, render_template, request, redirect, flash, session
from app import app, db, bcrypt
from app.forms import orderForm
from app.models import db, User
from sqlalchemy.exc import IntegrityError
from datetime import datetime

makh = False
jmkh = False
jtkh = False
plkh = False
amkh = False
mekh = False
plpa = False
mapa = False
plse = False
homi = False
kmmi = False
sumi = False
pach = False
mepa = False
stga = False
bhga = False
ph = False
bsbh = False
rase = False
total_price = 0.00

@app.route("/", methods=["GET", "POST"])
def snackPage():
    if request.method == "POST":
        global total_price
        if request.form.get("masalakhakhara") == "makh":
            global makh
            makh = True
            total_price = total_price + 4.00

        if request.form.get("jeeramarikhakhara") == "jmkh":
            global jmkh
            jmkh = True
            total_price = total_price + 4.00

        if request.form.get("jeeratilkhakhara") == "jtkh":
            global jtkh
            jtkh = True
            total_price = total_price + 4.00

        if request.form.get("plainkhakhara") == "plkh":
            global plkh
            plkh = True
            total_price = total_price + 1.40

        if request.form.get("acharmasalakhakhara") == "amkh":
            global amkh
            amkh = True
            total_price = total_price + 1.40

        if request.form.get("methikhakhara") == "mekh":
            global mekh
            mekh = True
            total_price = total_price + 1.40

        if request.form.get("plainpapadi") == "plpa":
            global plpa
            plpa = True
            total_price = total_price + 3.00

        if request.form.get("masalapapadi") == "mapa":
            global mapa
            mapa = True
            total_price = total_price + 3.00

        if request.form.get("plainsev") == "plse":
            global plse
            plse = True
            total_price = total_price + 3.00

        if request.form.get("hotmix") == "homi":
            global homi
            homi = True
            total_price = total_price + 3.00

        if request.form.get("khattamithamix") == "kmmi":
            global kmmi
            kmmi = True
            total_price = total_price + 3.00

        if request.form.get("surtimix") == "sumi":
            global sumi
            sumi = True
            total_price = total_price + 3.00

        if request.form.get("papadchavanu") == "pach":
            global pach
            pach = True
            total_price = total_price + 3.00

        if request.form.get("methipara") == "mepa":
            global mepa
            mepa = True
            total_price = total_price + 3.00

        if request.form.get("starganthia") == "stga":
            global stga
            stga = True
            total_price = total_price + 3.00

        if request.form.get("bhavnagriganthia") == "bhga":
            global bhga
            bhga = True
            total_price = total_price + 3.00

        if request.form.get("phulvadi") == "ph":
            global ph
            ph = True
            total_price = total_price + 3.00

        if request.form.get("bikanerisevbhujia") == "bsbh":
            global bsbh
            bsbh = True
            total_price = total_price + 3.00

        if request.form.get("ratlamisev") == "rase":
            global rase
            rase = True
            total_price = total_price + 3.00

    return render_template("index.html")

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

    return render_template("order_form.html", form=form, makh=makh, jmkh=jmkh, jtkh=jtkh, plkh=plkh, amkh=amkh, mekh=mekh, plpa=plpa, mapa=mapa, plse=plse, homi=homi, kmmi=kmmi, sumi=sumi, pach=pach, mepa=mepa, stga=stga, bhga=bhga, ph=ph, bsbh=bsbh, rase=rase, total_price=total_price)
