from app import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, login_user, current_user
from flask import Blueprint, render_template
from app.decorators.admin_required import admin_required



bp = Blueprint("administrator", __name__)

@bp.route('/Administrator/Dashboard')
@login_required
@admin_required
def view_dashboard():
    return render_template('administrator/dashboard.html')