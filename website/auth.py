from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(name=name).first()
    if user:
        if check_password_hash(user.password, password):
            flash('Logged in', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            flash('Incorrect password', category='error')
    else:
        flash('Name doesnt exist', category='error')
        
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(name = name).first() 
        
        if user:
            flash('Name already extists', category='error')
        elif len(name) < 3:
            flash('Name is too short', category='error')
        elif password1 != password2:
            flash('Passwords doesnt match', category='error')
        elif len(password1) < 3:
            flash('Password is too short', category='error')
        else:
            #add user to database
            new_user = User(name=name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)