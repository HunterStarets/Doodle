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
    
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    points = db.Column(db.Integer, nullable=True, default=0)
    community_name = db.Column(db.String(255), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    author = db.relationship('User', backref='posts', lazy=True)

    def __init__(self, timestamp: datetime, title: str, content: str, points: int, community_name, str, author_id: int) -> None:
        self.timestamp = timestamp
        self.title = title
        self.content = content
        self.points = points
        self.community_name = community_name
        self.author_id = author_id

    def __repr__(self) -> str:
        return f'Post({self.post_id}, {self.timestamp}, {self.title}, {self.content}, {self.points}, {self.community_name}, {self.author_id})'