from src.models import db, Comment

class CommentRepository:
    
    def create_comment(self, timestamp, content, points, author_id, post_id) -> None:
        new_comment = Comment(timestamp, content, points, author_id, post_id)
        db.session.add(new_comment)
        db.session.commit()

# Singleton to be used in other modules
comment_repository_singleton = CommentRepository()