from src.models import db, Post2, Comment, CommentVote, PostVote

class PostRepository:

    def get_post_by_id(self, post_id):
        post = Post2.query.filter_by(post_id=post_id).first()
        return post
    
    def get_posts_by_ids(self, post_ids):
        posts = Post2.query.filter(Post2.post_id.in_(post_ids)).all()
        return posts
    
    def create_post(self, title, content, community_name, timestamp, author_id):
        new_post = Post2(title, content, community_name, timestamp, author_id)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    def edit_post(self, existing_post, title, content, community_name) -> None:
        existing_post.title = title
        existing_post.content = content
        existing_post.community_name = community_name
        db.session.commit()

    def delete_post(self, post_to_delete):
        comments_to_delete = Comment.query.filter_by(post_id=post_to_delete.post_id).all()
        for comment in comments_to_delete:
            votes = CommentVote.query.filter_by(comment_id=comment.comment_id)
            for vote in votes:
                db.session.delete(vote)
                db.session.commit()
            db.session.delete(comment)
            db.session.commit()  
        votes = PostVote.query.filter_by(post_id=post_to_delete.post_id)
        for vote in votes:
            db.session.delete(vote)
            db.session.commit()        
        db.session.delete(post_to_delete)
        db.session.commit()        

    def get_all_posts_by_author_id(self, user_id):
        posts = Post2.query.filter_by(author_id=user_id).all()
        return posts
    
    def get_all_posts_by_post_votes(self, post_votes):
        return None

    def get_all_posts(self):
        return Post2.query.all()
    
    def get_all_posts_newest_first(self):
        return Post2.query.order_by(Post2.timestamp.desc()).all()

    def get_single_post(self, author_id):
        post = Post2.query.filter_by(author_id=author_id).first()
        return post
    
# Singleton to be used in other modules
post_repository_singleton = PostRepository()