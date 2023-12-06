from src.models import User, Post2, db
from src.repositories.post_repository import post_repository_singleton
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

    def delete_user(self, existing_user) -> None:
        # user_posts = post_repository_singleton.get_all_posts_by_author_id(existing_user.user_id)
        # for post in user_posts:
        #     post_repository_singleton.delete_post(post)

        db.session.delete(existing_user)
        db.session.commit()       
    
    # Reference: module-15-assignment
    def search_users(self, username):
        found_user = User.query.filter(func.lower(User.username).like(func.lower(f'%{username}%'))).first()
        return found_user
    
# Singleton to be used in other modules
user_repository_singleton = UserRepository()
