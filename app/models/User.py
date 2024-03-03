from app import db


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    user_password = db.Column(db.VARBINARY(256), nullable=False)
    user_rol_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"), nullable=False, default=1)


    def get_id(self):
        return self.idUsuario