from src.models import db, Post2

class PostRepository:

    def get_post_by_id(self, post_id):
        post = Post2.query.filter_by(post_id=post_id.first())
        return post
    
# Singleton to be used in other modules
post_repository_singleton = PostRepository()