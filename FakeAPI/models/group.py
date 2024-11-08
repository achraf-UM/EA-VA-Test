from database import db
from sqlalchemy import Column, Integer, String, Boolean, Text, JSON

class Group(db.Model):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    roles = Column(JSON, nullable=False)  # Use JSON type for storing array
    description = Column(Text, nullable=True)
    is_valid = Column(Boolean, default=True)

    def __init__(self, name, roles, description=None, is_valid=True):
        self.name = name
        self.roles = roles
        self.description = description
        self.is_valid = is_valid

    def __repr__(self):
        return f"<Group {self.name}>"