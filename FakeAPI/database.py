from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    
    with app.app_context():
        # Import models to ensure they are registered
        from models.lexique import Lexique
        from models.user import User  # Import User model as well
        from models.civility import Civility 
        from models.laboratory import Laboratory 
        from models.user_supervisor import UserSupervisor
        from models.division import Division
        from models.group import Group
        
        
        
        db.create_all()  # Create all tables
    


   # Register the user blueprint

    return app
