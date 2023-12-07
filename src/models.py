from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# User model
class User(db.Model):
    __tablename__ = 'app_user'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.TEXT, nullable=False)

    def __init__(self, email: str, username: str, password: str, first_name: str, last_name: str, bio:str) -> None:
        self.email = email
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.bio = bio

    def __repr__(self) -> str:
        return f'User({self.user_id}, {self.email}, {self.username}, {self.password}, {self.first_name}, {self.last_name})'

# Post Model
class Post2(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    community_name = db.Column(db.String(255), nullable=False) 
    timestamp = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    author_id = db.Column(db.Integer, db.ForeignKey('app_user.user_id'), nullable=False)

    def __init__(self, title: str, content: str, community_name: str, timestamp: datetime, author_id: int) -> None:
        self.title = title
        self.content = content
        self.community_name = community_name
        self.timestamp = timestamp
        self.author_id = author_id

    def __repr__(self) -> str:
        return f'Post({self.post_id}, {self.title}, {self.content}, {self.community_name}, {self.timestamp}, {self.author_id})'
    
# Comment Model
class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=False)
    post = db.relationship('Post2', backref='comments', lazy=True)
    author_id = db.Column(db.Integer, db.ForeignKey('app_user.user_id'), nullable=False)
    author = db.relationship('User', backref='comments', lazy=True)


    def __init__(self, content: str, timestamp: datetime, post_id: int, author_id: int) -> None:
        self.content = content
        self.timestamp = timestamp
        self.post_id = post_id
        self.author_id = author_id

    def __repr__(self) -> str:
            return f'Comment({self.comment_id}, {self.content}, {self.timestamp}, {self.post_id}, {self.author_id})'

# class Comment(db.Model):
#     __tablename__ = 'comment'
    
#     comment_id = db.Column(db.Integer, primary_key=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('app_user.user_id'), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
#     def __repr__(self):
#         return f'<Comment {self.comment_id}>'

# # Vote Model
# class Vote(db.Model):
#     __tablename__ = 'vote'
    
#     vote_id = db.Column(db.Integer, primary_key=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('app_user.user_id'), nullable=False)
#     is_upvote = db.Column(db.Boolean, nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __repr__(self):
#         return f'<Vote {self.vote_id}: {"Upvote" if self.is_upvote else "Downvote"}>'
