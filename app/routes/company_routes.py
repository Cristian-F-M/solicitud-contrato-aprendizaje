from app import db
from flask import Blueprint, render_template, request, redirect, url_for
from app.models.Company import Company
from app.models.Black_list import Black_list


bp = Blueprint("company", __name__)



@bp.route("/company/<company_id>", methods=["GET"])
def get_company(company_id):
    company = Company.get_company_by_id(company_id)
    if company:
        return company



@bp.route("/company/remove/<string:company_id>")
def remove_company(company_id):
    Company.remove_company(company_id)
    print(company_id)
    Black_list.query.filter_by(company_id=company_id).delete()
    db.session.commit()
    return redirect(url_for("user.view_user_settings", tag="blacklist"))