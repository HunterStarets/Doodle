from src.models import db, Comment

class CommentRepository:
    
    def create_comment(self, timestamp, content, points, author_id, post_id) -> None:
        new_comment = Comment(timestamp, content, points, author_id, post_id)
        db.session.add(new_comment)
        db.session.commit()
    
    def get_all_comments_by_post_id(self, existing_post):
        comments = Comment.query.filter_by(author_id=existing_post.author_id).all()
        return comments

# Singleton to be used in other modules
comment_repository_singleton = CommentRepository()