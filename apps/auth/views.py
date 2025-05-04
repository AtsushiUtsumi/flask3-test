from apps.app import User
from apps.auth.forms import LoginForm, SignUpForm
# from apps.crud.models import User
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user, login_required

auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")

@auth.route("/")
def index():
    return 'INDEX'# render_template("auth/index.html")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    return 'SIGNUP'# render_template("auth/signup.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    login_user(User(1))
    return render_template("auth/login.html")

@auth.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect("/")

@auth.route("/authorized")
@login_required
def authorized():
    return render_template("auth/authorized.html")
