from flask import Blueprint, render_template
from flask_login import login_user, logout_user, current_user, login_required

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html")
