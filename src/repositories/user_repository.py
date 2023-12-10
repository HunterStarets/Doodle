from src.models import User, db, Post2, Comment, PostVote, CommentVote
from sqlalchemy import func

class UserRepository:

    def get_user_by_username(self, username):
        user = User.query.filter_by(username=username).first()
        return user
    
    def get_user_by_email(self, email):
        user = User.query.filter_by(email=email).first()
        return user
    
    def get_user_by_id(self, user_id):
        user = User.query.filter_by(user_id=user_id).first()
        return user
    
    def create_user(self, email, username, password, first_name, last_name, bio):
        new_user = User(email, username, password, first_name, last_name, bio)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    def edit_user(self, existing_user, email, username, password, first_name, last_name, bio) -> None:
        existing_user.email = email
        existing_user.username = username
        existing_user.password = password
        existing_user.first_name = first_name
        existing_user.last_name = last_name
        existing_user.bio = bio
        db.session.commit()

    # OLD FLOW
    # (1) Delete users comments (2) delete comments associated with the users posts (3) delete users posts (4) delete user
    
    # UPDATED FLOW
    #(1) Delete all votes associated with users comments (2) delete users comments (3) delete all votes associated with comments
    # associated with users posts (4) delete comments associated with users posts (5) delete votes associate with users posts (6) delete users posts (7) delete user
    def delete_user(self, user_to_delete) -> None:
        
        #TODO: move db.session.commit() to once at the end of the loops

        user_comments = Comment.query.filter_by(author_id=user_to_delete.user_id).all()
        for comment in user_comments: 
            votes = CommentVote.query.filter_by(comment_id=comment.comment_id)
            for vote in votes:
                db.session.delete(vote)
                db.session.commit()
            db.session.delete(comment)
            db.session.commit()  

        user_posts = Post2.query.filter_by(author_id=user_to_delete.user_id).all()    

        for post in user_posts:
            other_user_comments = Comment.query.filter_by(post_id=post.post_id).all()
            for comment in other_user_comments:
                votes = CommentVote.query.filter_by(comment_id=comment.comment_id)
                for vote in votes:
                    db.session.delete(vote)
                    db.session.commit()
                db.session.delete(comment)
                db.session.commit()
            votes = PostVote.query.filter_by(post_id=post.post_id)
            for vote in votes:
                db.session.delete(vote)
                db.session.commit()     
            db.session.delete(post)
            db.session.commit()   

        db.session.delete(user_to_delete)
        db.session.commit()       
    
    def search_users(self, username):
        found_user = User.query.filter(func.lower(User.username).like(func.lower(f'%{username}%'))).first()
        return found_user
    
# Singleton to be used in other modules
user_repository_singleton = UserRepository()
