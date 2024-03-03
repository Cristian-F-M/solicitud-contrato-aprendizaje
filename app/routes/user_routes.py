from app import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, login_user, current_user
from flask import Blueprint, render_template


bp = Blueprint("user", __name__)

@bp.route('/User/Dashboard')
@login_required
def view_dashboard():
    return render_template('user/dashboard.html')