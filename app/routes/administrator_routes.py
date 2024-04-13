from flask import Blueprint, render_template
from flask_login import login_required
from app.decorators.admin_required import admin_required
from app.models.User import User
from app.models.Company import Company



bp = Blueprint("administrator", __name__)

@bp.route('/Administrator/Dashboard')
@login_required
@admin_required
def view_dashboard():
    return render_template('administrator/dashboard.html')

@bp.route('/Administrator/Users')
@login_required
@admin_required
def view_users():
    get_companies2 = Company.get_companies()
    users = User.query.all()
    return render_template('administrator/users.html', users=users, get_companies2=get_companies2)

