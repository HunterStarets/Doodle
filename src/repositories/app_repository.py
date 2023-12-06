from src.models import User, Post2, Comment, PostVote, CommentVote, db

class AppRepository:
    #USERS
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)
    
    def create_user(self, email, username, password, first_name, last_name, profile_picture, summary):
        new_user = User(email=email, username=username, password=password, first_name=first_name, last_name=last_name, profile_picture=profile_picture, summary=summary)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    #POSTS
    def get_all_posts(self):
        return Post2.query.all()
    
    def create_post(self, author_id, title, content, community_name):
        new_post = Post2(author_id=author_id, title=title, content=content, community_name=community_name)
        db.session.add(new_post)
        db.session.commit()
        return new_post
    
    def get_post_by_id(self, post_id):
        return Post2.query.get(post_id)
    

    #COMMENTS
    def get_comment_by_id(self, comment_id):     
        return Comment.query.get(comment_id)
    
    def get_comments_for_post(self, post_id):
        comments = Comment.query.filter(Comment.post_id == post_id).all()
        return comments
    
    def get_comments_for_user(self, user_id):
        comments = Comment.query.filter(Comment.author_id == user_id).all()
        return comments
    
    def create_comment(self, post_id, author_id, content):
        new_comment = Comment(post_id=post_id, author_id=author_id, content=content)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment
    
    #VOTES
    def get_net_post_votes(self, post_id):
        votes = PostVote.query.filter(PostVote.post_id == post_id).all()

        upvotes = []
        downvotes = []

        for vote in votes:
            if vote.is_upvote:
                upvotes.append(vote)
            else:
                downvotes.append(vote)
        
        net_votes = len(upvotes) - len(downvotes)
        return net_votes
    
    def get_net_comment_votes(self, comment_id):
        votes = CommentVote.query.filter(CommentVote.comment_id == comment_id).all()

        upvotes = []
        downvotes = []

        for vote in votes:
            if vote.is_upvote:
                upvotes.append(vote)
            else:
                downvotes.append(vote)
        
        net_votes = len(upvotes) - len(downvotes)
        return net_votes

    def create_post_vote(self, post_id, voter_id, is_upvote):
        new_vote = PostVote(post_id=post_id, voter_id=voter_id, is_upvote=is_upvote)
        db.session.add(new_vote)
        db.session.commit()
        return new_vote
    
    def create_comment_vote(self, comment_id, voter_id, is_upvote):
        new_vote = CommentVote(comment_id=comment_id, voter_id=voter_id, is_upvote=is_upvote)
        db.session.add(new_vote)
        db.session.commit()
        return new_vote
    

app_repository_singleton = AppRepository()
