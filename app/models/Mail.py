from app import db
import uuid

class Mail:
    __tablename__ = "mails"
    mail_id = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()), unique=True)
    mail_subject = db.Column(db.String(100), nullable=False)
    mail_content = db.Column(db.String(500), nullable=False)
    mail_file = db.Column(db.String(100), nullable=True)