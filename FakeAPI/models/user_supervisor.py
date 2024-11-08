from database import db

class UserSupervisor(db.Model):
    __tablename__ = 'user_supervisor'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    supervisor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)

    # Define relationships (optional if you need to access them directly)
    user = db.relationship('User', foreign_keys=[user_id])
    supervisor = db.relationship('User', foreign_keys=[supervisor_id])

    def __init__(self, user_id, supervisor_id):
        self.user_id = user_id
        self.supervisor_id = supervisor_id
