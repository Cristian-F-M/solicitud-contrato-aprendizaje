from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from flask_socketio import SocketIO
import uuid


db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(24)
    app.config.from_object("Config.Config")

    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    login_manager.login_view = "auth.view_login"


    @login_manager.user_loader
    def load_user(user_id):
        from app.models.User import User
        user = User.query.get(uuid.UUID(user_id))
        return user

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    from app.routes import auth_routes, administrator_routes, user_routes, company_routes
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(administrator_routes.bp)
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(company_routes.bp)

    return app
