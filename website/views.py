from flask import Blueprint, render_template, request, flash, jsonify,redirect
from flask_login import login_user, login_required, logout_user, current_user
from .models import Activity, Cardio
from . import db
import json

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
   
    if request.method =='POST':
        cardio_name = request.form.get('cardio_name')
        place = request.form.get('place')
        distance = request.form.get('distance')
        duration = request.form.get('duration')

        if len(cardio_name) < 1:
            flash('Name of activity is too short', category='error')
        else:
            new_cardio = Cardio(cardio_name=cardio_name, place=place, distance=distance, duration=duration, user_id=current_user.id)
            
            db.session.add(new_cardio)
            db.session.commit()
            flash('Cardio added', category='Success')

    return render_template("cardio.html", user=current_user)

@views.route('/activity', methods=['GET','POST'])
@login_required
def activity():
   
    if request.method =='POST':
        activity_name = request.form.get('activity_name')
        duration = request.form.get('duration')
        description = request.form.get('description')

        if len(activity_name) < 1:
            flash('Name of activity is too short', category='error')
        else:
            new_activity = Activity(activity_name=activity_name,duration=duration, description=description, user_id=current_user.id)
            
            db.session.add(new_activity)
            db.session.commit()
            flash('Activity added', category='Success')
            
    return render_template("activity.html", user=current_user)


@views.route('/delete-activity/<int:id>', methods=['POST'])
def delete_activity(id):
    activity_delete = Activity.query.get_or_404(id)
    db.session.delete(activity_delete)
    db.session.commit()
    return redirect('/')

@views.route('/delete-cardio/<int:id>', methods=['POST'])
def delete_cardio(id):
    cardio_delete = Cardio.query.get_or_404(id)
    db.session.delete(cardio_delete)
    db.session.commit()
    return redirect('/')