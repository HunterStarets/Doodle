from src.models import db, User

class UserRepository:

    def get_user_by_id(self, user_id):
        user = User.query.filter_by(user_id=user_id).first()
        return user
    
    def edit_user(self, existing_user, email, username, password, first_name, last_name) -> None:
        existing_user.email = email
        existing_user.username = username
        existing_user.password = password
        existing_user.first_name = first_name
        existing_user.last_name = last_name
        db.session.commit()

    def delete_user(self, existing_user) -> None:
        db.session.delete(existing_user)
        db.session.commit()

# Singleton to be used in other modules
user_repository_singleton = UserRepository()