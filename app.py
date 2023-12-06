from flask import Flask, render_template, request, abort, redirect, session
from flask_bcrypt import Bcrypt
from datetime import datetime
from src.repositories.post_repository import post_repository_singleton
#TODO move comment and post objects into appropriate folder and update imports
from post import Post
from comment import Comment
from src.models import db, User, Post2
from dotenv import load_dotenv
from src.repositories.app_repository import app_repository_singleton
import os

load_dotenv()

app = Flask(__name__)

# DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
app.config['SQLALCHEMY_ECHO'] = True

app.secret_key = os.getenv('APP_SECRET_KEY', 'super-secure')

db.init_app(app)
bcrypt = Bcrypt(app)

#Mock Test Data
posts = [
    Post("Post Title 1", "user1", "d/community1", [Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem"), Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem")], ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
    Post("Post Title 2", "user1", "d/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 1, "Malesuada proin libero nunc consequat interdum. Ac turpis egestas sed tempus urna et. Iaculis eu non diam phasellus vestibulum lorem sed. Egestas sed tempus urna et pharetra pharetra massa massa ultricies. Porttitor massa id neque aliquam vestibulum morbi blandit cursus risus. Lorem donec massa sapien faucibus et molestie."),
    Post("Post Title 3", "user1", "d/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 2, "Vitae purus faucibus ornare suspendisse sed. Eu feugiat pretium nibh ipsum consequat nisl vel. Interdum consectetur libero id faucibus nisl. Condimentum vitae sapien pellentesque habitant. Non nisi est sit amet facilisis magna etiam tempor orci."),
]


@app.route('/')
def index():
    #mock test data
    app_repository_singleton.get_all_posts()
    user = None
    if 'user_id' in session:
        user = app_repository_singleton.get_user_by_id(session['user_id'])

    posts = app_repository_singleton.get_all_posts()
    
    return render_template('index.html', home_active=True, user=user, posts=posts, app_repository_singleton=app_repository_singleton)

@app.get('/posts/<int:post_id>')
def view_post(post_id):
    #temporary
    post = app_repository_singleton.get_post_by_id(post_id)

    #final render
    return render_template('view_post.html', post=post, app_repository_singleton=app_repository_singleton)
 
@app.get('/view_profile')
def view_profile():
    #get current user
    #get list of posts posted by that user
    # posts=users posts
    # user = current user
    #if not logged in return render_template(log_in.html)
    user = {'username': 'johndoe', 'profile_picture': 'https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg', 'summary': 'Short bio'}
    
    #mock test data
    posts = [
        Post("USER POST 1", "johndoe", "d/community132", [Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem"), Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem")], ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
        Post("USER POST 2", "johndoe", "d/community13", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 1, "Malesuada proin libero nunc consequat interdum. Ac turpis egestas sed tempus urna et. Iaculis eu non diam phasellus vestibulum lorem sed. Egestas sed tempus urna et pharetra pharetra massa massa ultricies. Porttitor massa id neque aliquam vestibulum morbi blandit cursus risus. Lorem donec massa sapien faucibus et molestie."),
        Post("USER POST 3", "johndoe", "d/community1222", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 2, "Vitae purus faucibus ornare suspendisse sed. Eu feugiat pretium nibh ipsum consequat nisl vel. Interdum consectetur libero id faucibus nisl. Condimentum vitae sapien pellentesque habitant. Non nisi est sit amet facilisis magna etiam tempor orci."),
    ]
    
    return render_template('view_profile.html', view_profile_active=True, user=user, posts=posts)


@app.get('/user_saved_posts')
def user_saved_posts():
    #get current user
    #get list of posts saved by that user
    # saved_posts=users saved posts
    # user = current user
    #if not logged in return render_template(log_in.html)
    user = {'username': 'johndoe', 'profile_picture': 'https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg', 'summary': 'Short bio'}
    
    #mock test data
    saved_posts = [
        Post("saved post 1", "randuser2", "d/community132", [Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem"), Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem")], ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
        Post("saved post 2", "randuser4", "d/community13", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 1, "Malesuada proin libero nunc consequat interdum. Ac turpis egestas sed tempus urna et. Iaculis eu non diam phasellus vestibulum lorem sed. Egestas sed tempus urna et pharetra pharetra massa massa ultricies. Porttitor massa id neque aliquam vestibulum morbi blandit cursus risus. Lorem donec massa sapien faucibus et molestie."),
        Post("saved post 3", "randuser5", "d/community1222", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 2, "Vitae purus faucibus ornare suspendisse sed. Eu feugiat pretium nibh ipsum consequat nisl vel. Interdum consectetur libero id faucibus nisl. Condimentum vitae sapien pellentesque habitant. Non nisi est sit amet facilisis magna etiam tempor orci."),
    ]
    
    return render_template('user_saved_posts.html', view_profile_active=True, user=user, saved_posts=saved_posts)

@app.get('/user_comments_only')
def user_comments_only():
    user = {'username': 'johndoe','profile_picture': 'https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg', 'summary': 'Short Bio'}

    user_comments = [
        Comment('johndoe',["upvote1","upvote2"],["downvote1"],0,"random"),
        Comment('johndoe',["upvote1"],["downvote1","downvote2","downvote3"],1,"mean thing"),
        Comment('johndoe',["upvote1","upvote2","upvote3"],["downvote1"],2,"nice thing"),
    ]
    return render_template('user_comments_only.html',view_profile_active=True,user=user,user_comments=user_comments)

# all code from sprint03 
# Adding bcrypt and user sessions
@app.get('/login')
def get_login_page():
    if 'username' in session:
        return redirect('/secret')
    return render_template('login.html')

@app.get('/signup')
def get_signup_page():
    if 'username' in session:
        return redirect('/secret')
    return render_template('signup.html')

@app.post('/signup')
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    raw_password = request.form.get('password')
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    
    if not email or not username or not raw_password or not first_name or not last_name: 
        abort(400)
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        abort(400)
    existing_username = User.query.filter_by(username=username).first()
    if existing_username:
        abort(400)
    hashed_password = bcrypt.generate_password_hash(raw_password, 12).decode()

    ##mock data
    profile_picture='https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg'
    summary='testing description'
    ##end mock data
    
    new_user = app_repository_singleton.create_user(email, username, hashed_password, first_name, last_name, profile_picture, summary)
    
    session['username'] = username
    session['user_id'] = new_user.user_id
    return redirect('/secret')

@app.post('/login')
def login():
    username = request.form.get('username')
    raw_password = request.form.get('password')
    if not username or not raw_password:   
        abort(401)
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user: 
        abort(401)
    if not bcrypt.check_password_hash(existing_user.password, raw_password):
        abort(401)
    session['username'] = username
    session['user_id'] = existing_user.user_id
    return redirect('/')

@app.post('/logout')
def logout():
    del session['username']
    del session['user_id']
    return redirect('/login')

@app.get('/secret')
def get_secret_page():
    if 'username' not in session:
        abort(401)
    return render_template('secret.html', username=session['username'])

# Creating posts
@app.get('/posts/new')
def create_post_form():
    if 'username' not in session:
        abort(401)
    return render_template('create_post_form.html')

@app.post('/posts')
def create_post():
    title = request.form.get('title')
    content = request.form.get('content')
    community_name = request.form.get('community-name')
    author_id = session['user_id']

    user = app_repository_singleton.get_user_by_id(author_id)
    #user = User.query.filter_by(user_id=author_id).first()
    
    if not (title and content and author_id and user):
        abort(400)
    new_post = app_repository_singleton.create_post(author_id, title, content, community_name)

    return redirect('/')

# View single post
# OLD DEPRECATED METHOD, NEW METHOD DOES NOT WORK YET, HTML STILL NEEDS TO BE FIXED
# Leaving just for testing purposes
# @app.get('/view_post/<post_id>')
# def view_post(post_id):
#     #temporary
#     post = find_post_by_id(post_id)

#     #final render
#     return render_template('view_post.html', post=post)

@app.get('/posts/<post_id>')
def get_single_post(post_id: int):
    single_post = post_repository_singleton.get_post_by_id(post_id)
    return render_template('view_post', post=single_post)

