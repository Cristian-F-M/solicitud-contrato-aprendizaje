from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    user_password = db.Column(db.VARBINARY(256), nullable=False)
    user_role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"), nullable=False, default=1)


    def get_id(self):
        return self.user_id