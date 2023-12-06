from flask import Flask, render_template, request, abort, redirect, session, url_for
from flask_bcrypt import Bcrypt
from datetime import datetime

from src.repositories.post_repository import post_repository_singleton
from src.repositories.user_repository import user_repository_singleton
from src.models import db, User, Post2
#TODO move comment and post objects into appropriate folder and update imports
from post import Post
from comment import Comment

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

# Bcrypt connection
app.secret_key = os.getenv('APP_SECRET_KEY', 'super-secure')
bcrypt = Bcrypt(app)

# Home page
@app.route('/')
def index():
    user = None
    if 'user_id' in session:
        user = user_repository_singleton.get_user_by_id(session.get('user_id'))    
    posts = post_repository_singleton.get_all_posts()
    return render_template('index.html', home_active=True, user=user, posts=posts, user_repository_singleton=user_repository_singleton)

# User sign up
@app.get('/signup')
def get_signup_form():
    if 'user_id' in session:
        return redirect('/')
    return render_template('signup.html')

@app.post('/signup')
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    raw_password = request.form.get('password')
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    bio = request.form.get('bio')

    if not (email and username and raw_password and first_name and last_name and bio): 
        abort(400)

    existing_email = user_repository_singleton.get_user_by_email(email)
    if existing_email:
        abort(400)

    existing_username = user_repository_singleton.get_user_by_username(username)
    if existing_username:
        abort(400)

    hashed_password = bcrypt.generate_password_hash(raw_password, 12).decode()

    new_user = user_repository_singleton.create_user(email, username, hashed_password, first_name, last_name, bio)
    session['user_id'] = new_user.user_id
    session['username'] = username
    return redirect('/')

# Login user
@app.post('/login')
def login():
    username = request.form.get('username')
    raw_password = request.form.get('password')
    if not username or not raw_password:   
        abort(400)

    existing_user = user_repository_singleton.get_user_by_username(username)
    if not existing_user: 
        abort(401)

    if not bcrypt.check_password_hash(existing_user.password, raw_password):
        abort(401)

    session['user_id'] = existing_user.user_id
    session['username'] = username
    return redirect('/')

# Logout user
@app.post('/logout')
def logout():
    del session['user_id']
    del session['username']
    return redirect('/')

# Edit user
@app.get('/users/<int:user_id>/edit')
def edit_user_form(user_id: int):
    if 'user_id' not in session and 'username' not in session:
        abort(401)
    if session['user_id'] != user_id:
        abort(403)
    existing_user = user_repository_singleton.get_user_by_id(user_id)
    if not existing_user:
        abort(404)
    return render_template('edit_user_form.html', existing_user=existing_user)

@app.post('/users/<int:user_id>')
def edit_user(user_id: int):
    email = request.form.get('email')
    username = request.form.get('username')
    current_password = request.form.get('current-password')
    new_password = request.form.get('new-password')
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    bio = request.form.get('bio')

    if not(email and username and current_password and new_password and first_name and last_name and bio): 
        abort(400)

    existing_user = user_repository_singleton.get_user_by_id(user_id)
    if not existing_user:
        abort(401)

    if email != existing_user.email: 
        existing_email = user_repository_singleton.get_user_by_email(email)
        if existing_email:
            abort(400)

    if username != existing_user.username:
        existing_username = user_repository_singleton.get_user_by_username(username)
        if existing_username:
            abort(400)

    if not bcrypt.check_password_hash(existing_user.password, current_password):
        abort(401)

    hashed_password = bcrypt.generate_password_hash(new_password, 12).decode()
    user_repository_singleton.edit_user(existing_user, email, username, hashed_password, first_name, last_name, bio)
    return redirect('/')

# Delete User
@app.get('/users/<int:user_id>/delete')
def delete_user_form(user_id: int):
    if 'user_id' not in session and 'username' not in session:
        abort(401)
    if session['user_id'] != user_id:
        abort(403)
    existing_user = user_repository_singleton.get_user_by_id(user_id)
    if not existing_user:
        abort(404)
    return render_template('delete_user_form.html', existing_user=existing_user)

@app.post('/users/<int:user_id>/delete')
def delete_user(user_id: int):
    username = request.form.get('username')
    password = request.form.get('password')
    checkbox = request.form.get('checkbox')

    if not(username and password and checkbox):
        abort(400)
    
    existing_user = user_repository_singleton.get_user_by_id(user_id)
    if not existing_user: 
        abort(401)

    if not bcrypt.check_password_hash(existing_user.password, password):
        abort(401)

    user_repository_singleton.delete_user(existing_user)
    del session['username']
    del session['user_id']
    return redirect('/')

# Search users
#Reference: module-15-assignment
@app.get('/users/search')
def search_users():
    found_user = None
    q = request.args.get('q', '')
    if q != '':
        found_user = user_repository_singleton.search_users(q)
    return render_template('search_users.html', user=found_user)