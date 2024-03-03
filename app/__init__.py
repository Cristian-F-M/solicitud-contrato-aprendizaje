from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
import os


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(24)
    app.config.from_object("Config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.view_login"

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.User import User
        user = User.query.get(int(user_id))
        return user

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    from app.routes import auth_routes, administrator_routes, user_routes
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(administrator_routes.bp)
    app.register_blueprint(user_routes.bp)

    return app
