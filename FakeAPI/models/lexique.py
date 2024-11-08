from datetime import datetime
import uuid
from database import db

class Lexique(db.Model):
    __tablename__ = 'lexique'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    revision = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_valid = db.Column(db.Boolean, nullable=False)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=str(uuid.uuid4()))
