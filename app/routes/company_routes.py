from app import db
from flask import Blueprint, redirect, url_for, flash
from app.models.Company import Company
from app.models.Black_list import Black_list
from app.caprendizaje.app import Iniciar
from flask_login import current_user
import uuid

bp = Blueprint("company", __name__)



@bp.route("/company/<company_id>", methods=["GET"])
def get_company(company_id):
    company = Company.get_company_blacklist_by_id(company_id)
    if company:
        return company



@bp.route("/company/remove/<string:company_id>")
def remove_company_blacklist(company_id):
    Company.remove_company_blacklist(company_id)
    print(company_id)
    Black_list.query.filter_by(company_id=company_id).delete()
    db.session.commit()
    return redirect(url_for("user.view_user_settings", tag="blacklist"))

@bp.route("/company/add/<string:company_id>")
def add_company_blacklist(company_id):
    
    company = Company.get_company_by_id(company_id)
        
    company_id = company["company_id"]
    company_name = company["company_name"]
    company_email_address = company["company_email_address"]
    company_departament = company["company_departament"]
    company_city = company["company_city"]
    
    
    
    new_black_list = Black_list(black_list_id=uuid.uuid4(), company_id=company_id, black_list_user_id=current_user.user_id)    
    db.session.add(new_black_list)
    db.session.commit()
    
    
    
    company = {
            "black_list_id": new_black_list.black_list_id,
            "company_id": company_id,
            "company_name": company_name,
            "company_email_address": company_email_address,
            "company_departament": company_departament,
            "company_city": company_city,
        }
    
    
    
    
    
    
    
    
    Company.add_company_blacklist(company)
    
    
    flash(["information", "Company added to blacklist"], "flash")
    return redirect(url_for("user.view_user_search_emails"))




@bp.route('/Company/Search-Emails', methods=["POST"])
def search_emails():
    Company.init_companies()
    Iniciar()
    return Company.get_companies()



@bp.route("/company-search/remove/<string:company_id>")
def remove_company_blacklist_search(company_id):
    Company.remove_company_blacklist(company_id)
    Black_list.query.filter_by(company_id=company_id).delete()
    db.session.commit()
    return redirect(url_for("user.view_user_search_emails"))