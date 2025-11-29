from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#from carapp import db

class User(db.Model):
    user_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_fullname = db.Column(db.String(100), nullable=False)
    user_number = db.Column(db.String(100), nullable=False, unique=True)
    user_email = db.Column(db.String(100), nullable=False, unique=True)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    last_login = db.Column(db.DateTime(), default=datetime.utcnow)


   
class Admin(db.Model):
    admin_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    admin_name = db.Column(db.String(100), nullable=False)
    admin_password = db.Column(db.String(255), nullable=False)
    admin_email = db.Column(db.String(100), nullable=False)
    admin_login = db.Column(db.DateTime(), default=datetime.utcnow)
    vcf_status = db.Column(db.Enum("Active","Inactive"), nullable=False, server_default=("Inactive"))



    





