from database import db
from datetime import datetime

class Division(db.Model):
    __tablename__ = 'division'
    
    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    laboratory_id = db.Column(db.Integer, nullable=False)
    create_user_id = db.Column(db.Integer, nullable=False)
    update_user_id = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(100), nullable=False, unique=True)  # Make slug unique and required
    title = db.Column(db.String(255), nullable=False)  # Title is required
    description = db.Column(db.Text, nullable=True)
    keywords = db.Column(db.String(255), nullable=True)
    sort = db.Column(db.Integer, nullable=True, default=0)
    revision = db.Column(db.Integer, nullable=True, default=0)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_valid = db.Column(db.Boolean, nullable=False, default=True)
    conditional = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Division {self.title}>'

