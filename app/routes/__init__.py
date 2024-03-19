from flask import Blueprint

bp = Blueprint('main', __name__)


from app.routes import auth_routes, administrator_routes, user_routes, company_routes
