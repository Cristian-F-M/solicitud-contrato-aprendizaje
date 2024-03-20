from app import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
import re
from app.models.User import User
from app.models.Mail import Mail
from app.models.Company import Company


bp = Blueprint("user", __name__)


@bp.route("/User/Dashboard")
@login_required
def view_dashboard():
    return render_template("user/dashboard.html")


@bp.route("/User/Caprendizaje/Settings")
@login_required
def view_user_settings():        
    companies_sorted = Company.get_companies_sorted()
    return render_template("user/settings.html", companies_sorted=companies_sorted)


@bp.route("/User/Account", methods=["POST"])
def save_account():
    email_address = request.form["email_address"]
    google_password = request.form["google_password"]
    caprendizaje_user = request.form["caprendizaje_user"]
    caprendizaje_password = request.form["caprendizaje_password"]

    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email_address):
        flash(["mistake", "Invalid email address"], "flash")
        return redirect(url_for("user.view_user_settings", tag="account"))

    if not google_password:
        flash(["mistake", "Google password is required"], "flash")
        return redirect(url_for("user.view_user_settings", tag="account"))

    if not caprendizaje_user:
        flash(["mistake", "Caprendizaje user is required"], "flash")
        return redirect(url_for("user.view_user_settings", tag="account"))

    if not caprendizaje_password:
        flash(["mistake", "Caprendizaje password is required"], "flash")
        return redirect(url_for("user.view_user_settings", tag="account"))

    user = User.query.get_or_404(current_user.user_id)

    if not user:
        return redirect(url_for("auth.home"))

    user.email_address = email_address
    user.google_password = google_password
    user.caprendizaje_user = caprendizaje_user
    user.caprendizaje_password = caprendizaje_password

    db.session.commit()

    flash(["information", "Account updated successfully"], "flash")
    return redirect(url_for("user.view_user_settings", tag="account"))


@bp.route("/User/Mail", methods=["POST"])
@login_required
def save_mail():
    mail_subject = request.form["subject"]
    mail_content = request.form["content"]

    if not mail_subject:
        flash(["mistake", "Subject is required"], "flash", methods=["POST"])
        return redirect(url_for("user.view_user_settings", tag="email"))

    if not mail_content:
        flash(["mistake", "Content is required"], "flash")
        return redirect(url_for("user.view_user_settings", tag="email"))

    user = User.query.get_or_404(current_user.user_id)

    
    if user.mail_id is None:
        new_mail = Mail(mail_subject=mail_subject, mail_content=mail_content)
        db.session.add(new_mail)
    else:
        mail = Mail.query.get_or_404(user.mail_id)
        mail.mail_subject = mail_subject
        mail.mail_content = mail_content

    db.session.commit()
    if user.mail_id is None:
        user.mail_id = new_mail.mail_id
        db.session.commit()
    
    
    flash(["information", "Mail updated successfully"], "flash")
    return redirect(url_for("user.view_user_settings", tag="email"))


@bp.route("/User/File", methods=["POST"])
@login_required
def save_file():
    file = request.files["mail_file"]

    if not file:
        flash(["mistake", "File is required"], "flash")
        return redirect(url_for("user.view_user_settings", tag="file"))

    
    file.save("app/static/files/" + file.filename)

    user = User.query.get_or_404(current_user.user_id)



    if not user.mail_id:
        new_mail = Mail(mail_file=file.filename)
        db.session.add(new_mail)
    else:
        mail = Mail.query.get_or_404(user.mail_id)
        mail.mail_file = file.filename

    db.session.commit()
    
    if user.mail_id is None:
        user.mail_id = new_mail.mail_id
        db.session.commit()
    

    flash(["information", "File uploaded successfully"], "flash")
    return redirect(url_for("user.view_user_settings", tag="file"))
