from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import (
    logout_user,
    login_user,
    current_user,
)
from app.models.User import User
from flask_bcrypt import Bcrypt


bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()


@bp.route("/")
def home():
    if current_user.is_authenticated:
        if current_user.user_role_id == 2:
            return redirect(url_for("administrator.view_dashboard"))
        return redirect(url_for("user.view_dashboard"))
    return redirect(url_for("auth.view_login"))


@bp.route("/Login")
def view_login():
    return render_template("auth/login.html")


@bp.route("/Forgot-password")
def view_forgot_password():
    return render_template("auth/forgot-password.html")


@bp.route("/logging-in", methods=["POST"])
def login():

    user_email = request.form["user_email"]
    user_password = request.form["user_password"]
    user = User.query.filter_by(user_email=user_email).first()

    if not user:
        flash(["mistake", "Invalid credentials"], "flash")
        return redirect(url_for("auth.view_login"))

    if not bcrypt.check_password_hash(
        password=user_password, pw_hash=user.user_password
    ):
        flash(["mistake", "Invalid credentials"], "flash")
        return redirect(url_for("auth.view_login"))
    login_user(user)


    flash(["information", "You are logged in"], "flash")
    if user.user_role_id == 2:
        return redirect(url_for("administrator.view_dashboard"))

    return redirect(url_for("user.view_dashboard"))


@bp.route("/User/Logout")
def logout():
    logout_user()
    flash(["information", "you have logged out"], "flash")
    return redirect(url_for("auth.home"))
