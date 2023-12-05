from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'app_user'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    def __init__(self, email: str, username: str, password: str, first_name: str, last_name: str) -> None:
        self.email = email
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return f'User({self.user_id}, {self.email}, {self.username}, {self.password}, {self.first_name}, {self.last_name})'
    
class Post2(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    community_name = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    points = db.Column(db.Integer, nullable=True, default=0)
    author_id = db.Column(db.Integer, db.ForeignKey('app_user.user_id'), nullable=False)
    author = db.relationship('User', backref='posts', lazy=True, primaryjoin="Post2.author_id == User.user_id")

    def __init__(self, title: str, content: str, community_name: str, timestamp: datetime, points: int, author_id: int) -> None:
        self.title = title
        self.content = content
        self.community_name = community_name
        self.timestamp = timestamp
        self.points = points
        self.author_id = author_id

    def __repr__(self) -> str:
        return f'Post({self.post_id}, {self.title}, {self.content}, {self.community_name}, {self.timestamp}, {self.points}, {self.author_id})'
    
class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    content = db.Column(db.Text, nullable=False)
    points = db.Column(db.Integer, nullable=True, default=0)
    author_id = db.Column(db.Integer, db.ForeignKey('app_user.user_id'), nullable=False)
    author = db.relationship('User', backref='posts', lazy=True, primaryjoin="Comment.author_id == User.user_id")
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=False)
    post = db.relationship('Post2', backref='comments', lazy=True, primaryjoin="Comment.post_id == Post2.post_id")

    def __init__(self, timestamp: datetime, content: str, points: int, author_id: int, post_id: int) -> None:
        self.timestamp = timestamp
        self.content = content
        self.points = points
        self.author_id = author_id
        self.post_id = post_id

    def __repr__(self) -> str:
            return f'Comment({self.comment_id}, {self.timestamp}, {self.content}, {self.points}, {self.author_id}, {self.post_id})'