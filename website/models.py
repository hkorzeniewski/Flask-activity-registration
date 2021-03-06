from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    activities = db.relationship('Activity')
    cardios = db.relationship('Cardio')
   

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    activity_name = db.Column(db.String(150))
    duration = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 


class Cardio(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cardio_name =  db.Column(db.String(150))
    place = db.Column(db.String(100))
    distance = db.Column(db.Integer)
    duration = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

