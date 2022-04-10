# import the db object from the flask app
from collections import UserString
from app import db

# create user table with required field
class User(db.Model):
    __tablename__= "user"
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100), nullable = False)
    # user_email = db.Column(db.String(100), nullable= False)
    user_password = db.Column(db.String(150), nullable = False)
    