from flask import Blueprint, render_template, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Activity, Cardio
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods = ['GET'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/activities', methods=['GET','POST'])
@login_required
def activities():

    return render_template("activities.html", user=current_user)

@views.route('/cardio', methods=['GET','POST'])
@login_required
def cardio():
   
    if request.method =="POST":
        cardio_name = request.form.get('cardio_name')
        place = request.form.get('place')
        duration = request.form.get('duration')

        if len(cardio_name) < 1:
            flash('Name of activity is too short', category='error')
        else:
            new_cardio = Cardio(cardio_name = cardio_name, place=place,duration=duration, user_id=current_user.id)
            flash('Cardio added', category='Success')
            db.session.add(new_cardio)
            db.session.commit()

    return render_template("cardio.html", user=current_user)