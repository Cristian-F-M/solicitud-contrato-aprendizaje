from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
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



    from app.routes import auth_routes
    app.register_blueprint(auth_routes.bp)

    return app
