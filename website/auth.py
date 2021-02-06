from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
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
        if len(email) < 4:
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
            flash("Account Created ! ", category="success")

    return render_template("signup.html")
