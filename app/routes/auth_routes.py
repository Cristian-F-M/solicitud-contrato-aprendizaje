from app import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import (
    login_required,
    logout_user,
    login_user,
    current_user,
    login_remembered,
)
from flask import Blueprint, render_template
from sqlalchemy.exc import IntegrityError
import os
from app.models.User import User
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv


bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()


@bp.route("/")
def home():
    if current_user.is_authenticated:
        if current_user.user_role_id == 2:
            return redirect(url_for('administrator.view_dashboard'))
        return redirect(url_for('user.view_dashboard'))
    return redirect(url_for('auth.view_login'))


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
    user_remember = True if request.form.get("user_remember") else False
    user = User.query.filter_by(user_email=user_email).first()

    if not bcrypt.check_password_hash(
        password=user_password, pw_hash=user.user_password
    ):
        flash(["mistake", "Invalid credentials", "flash"])
        return redirect(url_for("auth.view_login"))

    login_user(user, remember=user_remember)

    if user.user_role_id > 1:
        return redirect(url_for("administrator.view_dashboard"))

    return redirect(url_for("user.view_dashboard"))
