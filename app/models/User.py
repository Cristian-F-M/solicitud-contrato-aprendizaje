from app import db
from flask_login import UserMixin
import uuid


class User(db.Model, UserMixin):
    __tablename__ = "users"

    user_id = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()), unique=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    user_password = db.Column(db.VARBINARY(256), nullable=False)
    user_role_id = db.Column(
        db.Integer, db.ForeignKey("roles.role_id"), nullable=False, default=1
    )
    user_user_caprendizaje = db.Column(db.String(25), nullable=True)
    user_password_caprendizaje = db.Column(db.String(150), nullable=True)
    user_acept_tyc = db.Column(db.Boolean, nullable=True, default=False)
    user_black_list = db.relationship("Black_list", backref="black_list_user", lazy=True)
    
    
    def get_id(self):
        return self.user_id
