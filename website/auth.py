from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully!", category="success")
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password!", category="error")
        else:
            flash("E-Mail does not exist!", category="error")

    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form['firstName']
        password1 = request.form['password1']
        password2 = request.form['password2']
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email Already exist!", category="error")
        elif len(email) < 4:
            flash("Email should be atleast 4 characters long ", category="error")
            pass
        elif len(firstName) < 2:
            flash("First Name should be atleast 2 characters long ", category="error")
            pass
        elif password1 != password2:
            flash("Password did'nt match ", category="error")

        elif len(password1) < 8:
            flash("Password Should be atleast 8 characters long ", category="error")
        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created ! ", category="success")
            return redirect(url_for('views.home'))

    return render_template("signup.html")
