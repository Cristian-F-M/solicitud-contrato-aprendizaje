from app import db
import uuid

class Black_list(db.Model):
    __tablename__ = "black_list"
    
    black_list_id = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()), unique=True)
    black_list_user_id = db.Column(db.String(50), db.ForeignKey("users.user_id"), nullable=False)
    company_id = db.Column(db.String(50), nullable=False)
    black_list_user = db.relationship("User", backref="user_black_list", lazy=True)