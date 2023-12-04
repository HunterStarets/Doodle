from src.models import db, Post2

class PostRepository:

    def get_post_by_id(self, post_id):
        post = Post2.query.filter_by(post_id=post_id).first()
        return post
    
    def create_post(self, title, content, community_name, timestamp, points, author_id) -> None:
        new_post = Post2(title, content, community_name, timestamp, points, author_id)
        db.session.add(new_post)
        db.session.commit()

    def edit_post(self, existing_post, title, content, community_name) -> None:
        existing_post.title = title
        existing_post.content = content
        existing_post.community_name = community_name
        db.session.commit()
    
    def delete_post(self, existing_post):
        db.session.delete(existing_post)
        db.session.commit()

    def get_all_posts_by_author_id(self, existing_user):
        posts = Post2.query.filter_by(author_id=existing_user.user_id).all()
        return posts

# Singleton to be used in other modules
post_repository_singleton = PostRepository()