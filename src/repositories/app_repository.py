from src.models import User, Post2, db

class AppRepository:
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)
    
    def get_all_posts(self):
        return Post2.query.all()
    
    def get_net_upvotes(self, post_id):
        return 120
    
    def create_user(self, email, username, password, first_name, last_name, profile_picture, summary):
        new_user = User(email=email, username=username, password=password, first_name=first_name, last_name=last_name, profile_picture=profile_picture, summary=summary)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    def create_post(self, author_id, title, content, community_name):
        #db.session.query(db.func.count(Vote.vote_id)).filter(Vote.post_id == self.post_id, Vote.is_upvote == True).scalar() - \ db.session.query(db.func.count(Vote.vote_id)).filter(Vote.post_id == self.post_id, Vote.is_upvote == False).scalar()
        new_post = Post2(author_id=author_id, title=title, content=content, community_name=community_name)
        db.session.add(new_post)
        db.session.commit()
        return new_post
    
    def get_post_by_id(self, post_id):
        return Post2.query.get(post_id)
    
    
app_repository_singleton = AppRepository()
