from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db = SQLAlchemy()

class User(db.Model):
    # user_id SERIAL,
    user_id = db.Columnn(db.Integer, primary_key=True)
    # email VARCHAR(255) UNIQUE NOT NULL,
    email = db.Column(db.String(255), unqiue=True, nullable=False)
    # user_name VARCHAR(20) UNIQUE NOT NULL,
    user_name = db.Column(db.String(20), unqiue=True, nullable=False)
    # password VARCHAR(20) NOT NULL,
    password = db.Column(db.String(20), nullable=False)
    # first_name VARCHAR(255) NOT NULL,
    first_name = db.Column(db.String(255), nullable=False)
    # last_name VARCHAR(255) NOT NULL,
    last_name = db.Column(db.String(255), nullable=False)
    # PRIMARY KEY (user_id)

    def __init__(self, email: str, user_name: str, password: str, first_name: str, last_name, str) -> None:
        self.email = email
        self.user_name = user_name
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self) -> str:
        return f'User({self.user_id}, {self.email}, {self.user_name}, {self.password}, {self.first_name}, {self.last_name})'
    
# Double check timestamp and content columns!
class Post(db.Model):
    # post_id SERIAL,
    post_id = db.Columnn(db.Integer, primary_key=True)
    #timestamp TIMESTAMP NOT NULL,
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now())
    # title VARCHAR(100) NOT NULL,
    title = db.Column(db.String(100), nullable=False)
    # content TEXT NOT NULL,
    content = db.Column(db.Text, nullable=False)
    # points INT NOT NULL,
    points = db.Column(db.Integer, nullable=False, default=0)
    # community_name VARCHAR(100),
    community_name = db.Column(db.String(100), nullable=True)
    # user_id INT,
    author_id = db.Column(db.Integer, \
        db.ForeginKey('user.user_id'), nullable=False)
    author = db.relationship('User', backref='posts')
    # PRIMARY KEY (post_id),
    # FOREIGN KEY (user_id) REFERENCES "user"(user_id)

    def __init__(self, timestamp: datetime, title: str, content: str, points: int, community_name, str, author_id: int) -> None:
        self.timestamp = timestamp
        self.title = title
        self.content = content
        self.points = points
        self.community_name = community_name
        self.author_id = author_id
    
    def __repr__(self) -> str:
        return f'Post({self.post_id}, {self.timestamp}, {self.title}, {self.content}, {self.points}, {self.community_name}, {self.author_id})'
    
# Double check timestamp, content, user_id, post_id, and parent_comment_id columns!      
class Comment(db.Model):
    #comment_id SERIAL,
    comment_id = db.Columnn(db.Integer, primary_key=True)
    #timestamp TIMESTAMP NOT NULL,
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now())
    #content TEXT NOT NULL,
    content = db.Column(db.Text, nullable=False)
    #points INT NOT NULL,
    points = db.Column(db.Integer, nullable=False, default=0)
    #user_id INT,
    user_id = db.Column(db.Integer, \
        db.ForeginKey('user.user_id'), nullable=False)
    user = db.relationship('User', backref='comments')
    #post_id INT,
    post_id = db.Column(db.Integer, \
        db.ForeginKey('post.post_id'), nullable=False)
    post = db.relationship('Post', backref='comments')
    #parent_comment_id INT,
    parent_comment_id = db.Column(db.Integer, \
        db.ForeginKey('comment.comment_id'), nullable=True)
    parent_comment = db.relationship('Comment', backref='comments')
    #PRIMARY KEY (post_id),
    #FOREIGN KEY (user_id) REFERENCES "user"(user_id),
    #FOREIGN KEY (post_id) REFERENCES post(post_id)
    #FOREIGN KEY (parent_comment_id) REFERENCES comment(comment_id),

    def __init__(self, timestamp: datetime, content: str, points: int, user_id: int, post_id: int, parent_comment_id: int) -> None:
        self.timestamp = timestamp
        self.content = content
        self.points = points
        self.user_id = user_id
        self.post_id = post_id
        self.parent_comment_id = parent_comment_id
    
    def __repr__(self) -> str:
        return f'Comment({self.comment_id}, {self.timestamp}, {self.content}, {self.points}, {self.user_id}, {self.post_id}, {self.parent_comment_id})'
    
# Double check user_id, post_id, and comment_id columns!    
class Vote(db.Model):
    #vote_id SERIAL,
    vote_id = db.Columnn(db.Integer, primary_key=True)
    #vote_type BOOLEAN NOT NULL, # upvote or downvote
    vote_type = db.Column(db.Boolean, nullable=False)
    #user_id INT,
    user_id = db.Column(db.Integer, \
        db.ForeginKey('user.user_id'), nullable=False)
    user = db.relationship('User', backref='votes')
    #post_id INT,
    post_id = db.Column(db.Integer, \
        db.ForeginKey('post.post_id'), nullable=False)
    post = db.relationship('Post', backref='votes')
    #comment_id INT,
    comment_id = db.Column(db.Integer, \
        db.ForeginKey('comment.comment_id'), nullable=True)
    comment = db.relationship('Comment', backref='votes')
    #PRIMARY KEY (vote_id),
    #FOREIGN KEY (user_id) REFERENCES "user"(user_id),
    #FOREIGN KEY (post_id) REFERENCES post(post_id),
    #FOREIGN KEY (comment_id) REFERENCES comment(comment_id)

    def __init__(self, vote_type: bool, user_id: int, post_id: int, comment_id: int) -> None:
        self.vote_type = vote_type
        self.user_id = user_id
        self.post_id = post_id
        self.comment_id = comment_id

    def __repr__(self) -> str:
        return f'Vote({self.vote_id}, {self.vote_type}, {self.user_id}, {self.post_id}, {self.comment_id})'

# Double check user_id, post_id, and comment_id columns!    
class SavedItems(db.Model):
    #saved_item_id SERIAL,
    saved_item_id = db.Columnn(db.Integer, primary_key=True)
    #user_id INT,
    user_id = db.Column(db.Integer, \
        db.ForeginKey('user.user_id'), nullable=False)
    user = db.relationship('User', backref='saved_items')
    #post_id INT,
    post_id = db.Column(db.Integer, \
        db.ForeginKey('post.post_id'), nullable=False)
    post = db.relationship('Post', backref='saved_items')
    #comment_id INT,
    comment_id = db.Column(db.Integer, \
        db.ForeginKey('comment.comment_id'), nullable=True)
    comment = db.relationship('Comment', backref='saved_items')
    #PRIMARY KEY (saved_item_id),
    #FOREIGN KEY (user_id) REFERENCES "user"(user_id),
    #FOREIGN KEY (post_id) REFERENCES post(post_id),
    #FOREIGN KEY (comment_id) REFERENCES comment(comment_id)

    def __init__(self, user_id: int, post_id: int, comment_id: int) -> None:
        self.user_id = user_id
        self.post_id = post_id
        self.comment_id = comment_id
        
    def __repr__(self) -> str:
        return f'SavedItems({self.saved_item_id}, {self.user_id}, {self.post_id}, {self.comment_id})'