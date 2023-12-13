from src.models import User, Post2, Comment, PostVote, CommentVote, db

def insert_db():
        new_user = User("drako789@gmail.com", "drako789", "abc", "drako", "joya", "bio")
        db.session.add(new_user)
        db.session.commit()