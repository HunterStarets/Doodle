from src.models import db, Comment

class CommentRepository:
    
    def create_comment(self, content, timestamp, post_id, author_id) -> None:
        new_comment = Comment(content, timestamp, post_id, author_id)
        db.session.add(new_comment)
        db.session.commit()

# Singleton to be used in other modules
comment_repository_singleton = CommentRepository()