from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import time
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    activities = db.relationship('Activity')
    cardios = db.relationship('Cardio')

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    activity_name = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 


class Cardio(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cardio_name =  db.Column(db.String(150))
    place = db.Column(db.String(100))
    distance = db.Column(db.Integer)
    # duration = db.Column(db.DateTime()[11:19], default=func.now())
    duration = dict(
        clock_start=lambda v, c, m, p:m.clock_start.strftime('%M:%S'),
        clock_end=lambda v, c, m, p:m.clock_end.strftime('%M:%S')
    )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 