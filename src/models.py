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
    profile_picture = content = db.Column(db.Text, nullable=False)

    def __init__(self, email: str, username: str, password: str, first_name: str, last_name: str, profile_picture: str) -> None:
        self.email = email
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.profile_picture_url = profile_picture

    def __repr__(self) -> str:
        return f'User({self.user_id}, {self.email}, {self.username}, {self.password}, {self.first_name}, {self.last_name})'

    @classmethod
    def get_user_by_id(cls, user_id: int):
        return cls.query.get(user_id)
    

class Post2(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('app_user.user_id'), nullable=False)

    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    community_name = db.Column(db.String(255), nullable=False) 
    
    

    def __init__(self, author_id: int, title: str, content: str, timestamp: datetime, community_name: str):
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.utcnow()
        self.author_id = author_id
        self.community_name = community_name

    def __repr__(self) -> str:
        return f'Post2({self.post_id}, "{self.title}", "{self.content}", "{self.community_name}", "{self.timestamp}", {self.author_id})'

    def net_upvotes(self):
        return db.session.query(db.func.count(Vote.vote_id)).filter(Vote.post_id == self.post_id, Vote.is_upvote == True).scalar() - \
               db.session.query(db.func.count(Vote.vote_id)).filter(Vote.post_id == self.post_id, Vote.is_upvote == False).scalar()

    @classmethod
    def get_all_posts(cls):
        return cls.query.all()
    
# Comment Model
class Comment(db.Model):
    __tablename__ = 'comment'
    
    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('app_user.user_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Comment {self.comment_id}>'

# Vote Model
class Vote(db.Model):
    __tablename__ = 'vote'
    
    vote_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('app_user.user_id'), nullable=False)
    is_upvote = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Vote {self.vote_id}: {"Upvote" if self.is_upvote else "Downvote"}>'
