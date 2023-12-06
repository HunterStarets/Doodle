from flask import Flask, render_template, request, abort, redirect, session, url_for
from flask_bcrypt import Bcrypt
from datetime import datetime

from src.repositories.post_repository import post_repository_singleton
from src.repositories.comment_repository import comment_repository_singleton
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

app.secret_key = os.getenv('APP_SECRET_KEY', 'super-secure')

db.init_app(app)
bcrypt = Bcrypt(app)

#Mock Test Data
posts = [
    Post("Post Title 1", "user1", "d/community1", [Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem"), Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem")], ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
    Post("Post Title 2", "user1", "d/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 1, "Malesuada proin libero nunc consequat interdum. Ac turpis egestas sed tempus urna et. Iaculis eu non diam phasellus vestibulum lorem sed. Egestas sed tempus urna et pharetra pharetra massa massa ultricies. Porttitor massa id neque aliquam vestibulum morbi blandit cursus risus. Lorem donec massa sapien faucibus et molestie."),
    Post("Post Title 3", "user1", "d/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 2, "Vitae purus faucibus ornare suspendisse sed. Eu feugiat pretium nibh ipsum consequat nisl vel. Interdum consectetur libero id faucibus nisl. Condimentum vitae sapien pellentesque habitant. Non nisi est sit amet facilisis magna etiam tempor orci."),
]

# @app.route('/')
# def index():
#     #mock test data
#     user = None 
#     user = {'username': 'johndoe', 'profile_picture': 'https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg', 'summary': 'Short bio'}
    
#     #final render
#     return render_template('index.html', home_active=True, user=user, posts=posts)
 
@app.get('/view_profile')
def view_profile():
    #get current user
    #get list of posts posted by that user
    # posts=users posts
    # user = current user
    #if not logged in return render_template(log_in.html)
    # user = {'username': 'johndoe', 'profile_picture': 'https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg', 'summary': 'Short bio'}
    
    #mock test data
    # posts = [
    #     Post("USER POST 1", "johndoe", "d/community132", [Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem"), Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem")], ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
    #     Post("USER POST 2", "johndoe", "d/community13", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 1, "Malesuada proin libero nunc consequat interdum. Ac turpis egestas sed tempus urna et. Iaculis eu non diam phasellus vestibulum lorem sed. Egestas sed tempus urna et pharetra pharetra massa massa ultricies. Porttitor massa id neque aliquam vestibulum morbi blandit cursus risus. Lorem donec massa sapien faucibus et molestie."),
    #     Post("USER POST 3", "johndoe", "d/community1222", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 2, "Vitae purus faucibus ornare suspendisse sed. Eu feugiat pretium nibh ipsum consequat nisl vel. Interdum consectetur libero id faucibus nisl. Condimentum vitae sapien pellentesque habitant. Non nisi est sit amet facilisis magna etiam tempor orci."),
    # ]
    
    return render_template('view_profile.html', view_profile_active=True, user=user, posts=posts)

#TEMPORARY TESTING FUNCTION
def find_post_by_id(post_id):
    post_id = int(post_id)
    try:
        post = posts[post_id]
    except:
        post = Post("Imaginary Post", "user1", "d/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], -1, "Nisl condimentum id venenatis a condimentum. Enim neque volutpat ac tincidunt. At tempor commodo ullamcorper a lacus vestibulum sed. Commodo viverra maecenas accumsan lacus."),
    
    return post

# @app.get('/user_saved_posts')
# def user_saved_posts():
#     #get current user
#     #get list of posts saved by that user
#     # saved_posts=users saved posts
#     # user = current user
#     #if not logged in return render_template(log_in.html)
#     user = {'username': 'johndoe', 'profile_picture': 'https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg', 'summary': 'Short bio'}
    
#     #mock test data
#     saved_posts = [
#         Post("saved post 1", "randuser2", "d/community132", [Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem"), Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem")], ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
#         Post("saved post 2", "randuser4", "d/community13", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 1, "Malesuada proin libero nunc consequat interdum. Ac turpis egestas sed tempus urna et. Iaculis eu non diam phasellus vestibulum lorem sed. Egestas sed tempus urna et pharetra pharetra massa massa ultricies. Porttitor massa id neque aliquam vestibulum morbi blandit cursus risus. Lorem donec massa sapien faucibus et molestie."),
#         Post("saved post 3", "randuser5", "d/community1222", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 2, "Vitae purus faucibus ornare suspendisse sed. Eu feugiat pretium nibh ipsum consequat nisl vel. Interdum consectetur libero id faucibus nisl. Condimentum vitae sapien pellentesque habitant. Non nisi est sit amet facilisis magna etiam tempor orci."),
#     ]
    
#     return render_template('user_saved_posts.html', view_profile_active=True, user=user, saved_posts=saved_posts)

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

# User sign up 
@app.get('/signup')
def get_signup_form():
    if 'user_id' in session:
        return redirect('/secret')
    return render_template('signup.html')

@app.post('/signup')
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    raw_password = request.form.get('password')
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')

    if not (email and username and raw_password and first_name and last_name): 
        abort(400)

    existing_email = user_repository_singleton.get_user_by_email(email)
    if existing_email:
        abort(400)

    existing_username = user_repository_singleton.get_user_by_username(username)
    if existing_username:
        abort(400)

    hashed_password = bcrypt.generate_password_hash(raw_password, 12).decode()

    new_user = user_repository_singleton.create_user(email, username, hashed_password, first_name, last_name)
    session['user_id'] = new_user.user_id
    session['username'] = username
    return redirect('/secret')

# User login
@app.get('/login')
def get_login_page():
    if 'user_id' in session and 'username' in session:
        return redirect('/secret')
    return render_template('login.html')

@app.post('/login')
def login():
    username = request.form.get('username')
    raw_password = request.form.get('password')
    if not username or not raw_password:   
        abort(401)

    existing_user = user_repository_singleton.get_user_by_username(username)
    if not existing_user: 
        abort(401)

    if not bcrypt.check_password_hash(existing_user.password, raw_password):
        abort(401)

    session['user_id'] = existing_user.user_id
    session['username'] = username
    return redirect('/secret')

# Logout user
@app.post('/logout')
def logout():
    del session['user_id']
    del session['username']
    return redirect('/login')

@app.get('/secret')
def get_secret_page():
    if 'user_id' not in session or 'username' not in session:
        abort(401)
    return render_template('secret.html', username=session['username'])

#=========================================
# Creating posts
@app.get('/posts/new')
def create_post_form():
    if 'user_id' not in session or 'username' not in session:
        abort(401)
    return render_template('create_post_form.html')

@app.post('/posts')
def create_post():
    title = request.form.get('title')
    content = request.form.get('content')
    community_name = request.form.get('community-name')
    timestamp = datetime.utcnow()
    points = 0
    if not (title and content and community_name):
        abort(400)

    user_id = session.get('user_id')
    user = user_repository_singleton.get_user_by_id(user_id)

    if not (user_id and user):    
        abort(401)

    author_id = user.user_id
    post_repository_singleton.create_post(title, content, community_name, timestamp, points, author_id)
    return redirect('/secret')

# Edit user
@app.get('/users/<int:user_id>/edit')
def edit_user_form(user_id: int):
    if 'user_id' not in session or 'username' not in session:
        abort(401)
    if session['user_id'] != user_id:
        abort(403)
    existing_user = user_repository_singleton.get_user_by_id(user_id)
    return render_template('edit_user_form.html', existing_user=existing_user)

@app.post('/users/<int:user_id>')
def edit_user(user_id: int):
    email = request.form.get('email')
    username = request.form.get('username')
    current_password = request.form.get('current-password')
    new_password = request.form.get('new-password')
    verify_password = request.form.get('verify-password')
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')

    if not(email and username and current_password and new_password and verify_password and first_name and last_name): 
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

    if new_password != verify_password:
        abort(400)

    hashed_password = bcrypt.generate_password_hash(new_password, 12).decode()
    user_repository_singleton.edit_user(existing_user, email, username, hashed_password, first_name, last_name)
    return redirect('/secret')

# Delete user 
@app.get('/users/<int:user_id>/delete')
def delete_user_form(user_id: int):
    if 'user_id' not in session and 'username' not in session:
        abort(401)
    if session['user_id'] != user_id:
        abort(403)
    existing_user = user_repository_singleton.get_user_by_id(user_id)
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
    return redirect('/login')

# Edit posts
@app.get('/posts/<int:post_id>/edit')
def edit_post_form(post_id: int):
    if 'user_id' not in session or 'username' not in session:
        abort(401)
    existing_post = post_repository_singleton.get_post_by_id(post_id)
    if not existing_post:
        abort(404)
    if existing_post.post_id != post_id:
        abort(403)        
    if existing_post.author_id != session.get('user_id'):
        abort(403)
    return render_template('edit_post_form.html', existing_post=existing_post)

@app.post('/posts/<int:post_id>')
def edit_post(post_id: int):
    title = request.form.get('title')
    content = request.form.get('content')
    community_name = request.form.get('community-name')

    existing_post = post_repository_singleton.get_post_by_id(post_id)
    if not existing_post:
        abort(404)
    post_repository_singleton.edit_post(existing_post, title, content, community_name)
    return redirect('/secret')

# Deleting posts
@app.get('/posts/<int:post_id>/delete')
def delete_post_form(post_id: int):
    if 'user_id' not in session or 'username' not in session:
        abort(401)
    existing_post = post_repository_singleton.get_post_by_id(post_id)
    if not existing_post:
        abort(404)
    if existing_post.post_id != post_id:
        abort(403)        
    if existing_post.author_id != session.get('user_id'):
        abort(403)
    return render_template('delete_post_form.html', existing_post=existing_post)

@app.post('/posts/<int:post_id>/delete')
def delete_post(post_id: int):
    existing_post = post_repository_singleton.get_post_by_id(post_id)
    if not existing_post:
        abort(404)
    
    post_repository_singleton.delete_post(post_id)
    return redirect('/secret')

# Search users
#Reference: module-15-assignment
@app.get('/users/search')
def search_users():
    found_user = None
    q = request.args.get('q', '')
    if q != '':
        found_user = user_repository_singleton.search_users(q)
    return render_template('search_users.html', user=found_user)

# Home page
@app.route('/')
def index():
    user = None 
    user = user_repository_singleton.get_user_by_id(session.get('user_id'))    
    return render_template('index.html', home_active=True, user=user, posts=posts)

# View single post
@app.get('/posts/<int:post_id>')
def get_single_post(post_id:int):
    existing_post = post_repository_singleton.get_post_by_id(post_id)
    if not existing_post:
        abort(404)
    author = user_repository_singleton.get_user_by_id(existing_post.author_id)
    if not author:
        abort(404)
    return render_template('get_single_post.html', existing_post=existing_post, author=author)

#Create comment
@app.post('/comments')
def create_comment():
    comment_content = request.form.get('comment')
    post_id = request.form.get('post-id')
    timestamp = datetime.utcnow()
    points = 0

    if not (comment_content):
        abort(400)

    user_id = session.get('user_id')
    user = user_repository_singleton.get_user_by_id(user_id)

    if not (user_id and user and post_id):    
        abort(401)

    author_id = user.user_id
    comment_repository_singleton.create_comment(timestamp, comment_content, points, author_id, post_id)
    return redirect(url_for('get_single_post', post_id=post_id))