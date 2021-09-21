from flask_login import UserMixin
from flaskr.db_setup import database as db

class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # Relationships
    bucket = db.relationship("Bucket", back_populates="user")

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

class Bucket(db.Model):
    __tablename__='buckets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(1000))
    
    # Relationships
    user = db.relationship("User", back_populates="bucket", foreign_keys=user_id)

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name