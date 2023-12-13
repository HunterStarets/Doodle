from src.models import User, Post2, Comment, PostVote, CommentVote, db

def clear_db():
        CommentVote.query.delete()
        PostVote.query.delete()
        Comment.query.delete()
        Post2.query.delete()
        User.query.delete()
        db.session.commit()