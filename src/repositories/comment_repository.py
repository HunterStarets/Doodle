from src.models import db, Comment
from src.repositories.post_repository import post_repository_singleton

class CommentRepository:
    
    def create_comment(self, content, timestamp, post_id, author_id) -> None:
        new_comment = Comment(content, timestamp, post_id, author_id)
        db.session.add(new_comment)
        db.session.commit()
    
    def get_all_comments_by_post_id(self, post_id):
        existing_post = post_repository_singleton.get_post_by_id(post_id)     
        if not existing_post:
            return None
        comments = Comment.query.filter_by(post_id=existing_post.post_id).all()
        return comments        

# Singleton to be used in other modules
comment_repository_singleton = CommentRepository()