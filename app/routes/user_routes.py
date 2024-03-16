from app import db, socketio
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, login_user, current_user
from flask import Blueprint, render_template
from flask_socketio import emit



bp = Blueprint("user", __name__)

@bp.route('/User/Dashboard')
@login_required
def view_dashboard():
    return render_template('user/dashboard.html')

@bp.route('/User/Caprendizaje/Settings')
@login_required
def view_user_settings():
    return render_template('user/settings.html')




@socketio.on('msj')
def msj(msj): # <-- Recibir
    emit('msj', msj) # <-- Enviar