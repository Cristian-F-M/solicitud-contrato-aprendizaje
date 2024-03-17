from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "users"

    user_id = db.Column(db.VARBINARY(256), primary_key=True, default=db.func.uuid_to_bin(db.func.uuid()))
    user_name = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    user_password = db.Column(db.VARBINARY(256), nullable=False)
    user_role_id = db.Column(
        db.Integer, db.ForeignKey("roles.role_id"), nullable=False, default=1
    )
    user_user_caprendizaje = db.Column(db.String(25), nullable=True)
    user_password_caprendizaje = db.Column(db.String(150), nullable=True)
    user_acept_tyc = db.Column(db.Boolean, nullable=True, default=False)

    def get_id(self):
        return self.user_id
