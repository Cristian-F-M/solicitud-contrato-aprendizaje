from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app.decorators.admin_required import admin_required
from app.models.User import User
from app.models.Company import Company
from app import db



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


@bp.route('/Administrator/Users/Delete/<string:user_id>')
@login_required
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        flash(['information', 'User deleted'], 'flash')
    
    return redirect(url_for('administrator.view_users'))