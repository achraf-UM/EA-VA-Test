from datetime import datetime
from database import db

class Laboratory(db.Model):
    __tablename__ = 'laboratory'
    
    # Define the columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    create_user_id = db.Column(db.Integer, nullable=True)
    update_user_id = db.Column(db.Integer, nullable=True)
    logo = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=True)
    city = db.Column(db.String(80), nullable=True)
    address = db.Column(db.String(155), nullable=True)
    address_bis = db.Column(db.String(155), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    zip_code = db.Column(db.String(20), nullable=True)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    keywords = db.Column(db.String(255), nullable=True)
    sort = db.Column(db.Integer, nullable=True)
    revision = db.Column(db.Integer, nullable=False, default=0)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_valid = db.Column(db.Boolean, nullable=False, default=True)
    conditional = db.Column(db.String(255), nullable=True)
    ladp_server_id = db.Column(db.Integer, nullable=True)
    dashboard_blocks = db.Column(db.Text, nullable=True)
    mail_formation_ouverture = db.Column(db.Text, nullable=True)
    mail_formation_relance = db.Column(db.Text, nullable=True)
    afficher_module_informations = db.Column(db.Boolean, nullable=False, default=False)
    afficher_formation_informations = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, slug, create_user_id=None, update_user_id=None, logo=None, url=None, city=None, address=None,
                 address_bis=None, phone=None, email=None, zip_code=None, title=None, description=None, keywords=None,
                 sort=None, revision=1, create_date=None, update_date=None, is_valid=True, conditional=None, ladp_server_id=None, dashboard_blocks = None,mail_formation_ouverture = None, mail_formation_relance = None, afficher_module_informations = None, afficher_formation_informations = None):
        self.slug = slug
        self.create_user_id = create_user_id
        self.update_user_id = update_user_id
        self.logo = logo
        self.url = url
        self.city = city
        self.address = address
        self.address_bis = address_bis
        self.phone = phone
        self.email = email
        self.zip_code = zip_code
        self.title = title
        self.description = description
        self.keywords = keywords
        self.sort = sort
        self.revision = revision
        self.create_date = create_date or datetime.utcnow()
        self.update_date = update_date or datetime.utcnow()
        self.is_valid = is_valid
        self.conditional = conditional
        self.ladp_server_id = ladp_server_id
        self.dashboard_blocks = dashboard_blocks
        self.mail_formation_ouverture = mail_formation_ouverture
        self.mail_formation_relance = mail_formation_relance
        self.afficher_module_informations = afficher_module_informations
        self.afficher_formation_informations = afficher_formation_informations

