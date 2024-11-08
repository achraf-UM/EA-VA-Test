from datetime import datetime
from database import db

class Civility(db.Model):
    __tablename__ = 'civility'
    
    id = db.Column(db.Integer, primary_key=True)
    create_user_id = db.Column(db.Integer, nullable=False)
    update_user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    keywords = db.Column(db.String(255), nullable=True)
    sort = db.Column(db.Integer, nullable=False)
    revision = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_valid = db.Column(db.Boolean, nullable=False, default=True)
    conditional = db.Column(db.String(255), nullable=True)

    def __init__(self, create_user_id, update_user_id, title, description, keywords, sort, revision, conditional=None):
        self.create_user_id = create_user_id
        self.update_user_id = update_user_id
        self.title = title
        self.description = description
        self.keywords = keywords
        self.sort = sort
        self.revision = revision
        self.conditional = conditional
