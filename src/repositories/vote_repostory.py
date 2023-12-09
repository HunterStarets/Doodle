from src.models import db, PostVote, CommentVote

class VoteRepository:

    def get_post_vote_by_id(self, vote_id):
        vote = PostVote.query.filter_by(vote_id=vote_id).first()
        return vote
    
    def get_post_upvotes_by_user_id(self, user_id):
        votes = PostVote.query.filter_by(user_id=user_id, is_upvote = True)
        return votes
    
    def get_post_downvotes_by_user_id(self, user_id):
        votes = PostVote.query.filter_by(user_id=user_id, is_upvote = False)
        return votes
    
    def get_post_vote_by_post_and_user_ids(self, post_id, voter_id):
        vote = PostVote.query.filter_by(post_id=post_id, voter_id=voter_id).first()
        return vote
    
    def delete_post_vote_by_id(self, vote_id):
        vote = PostVote.query.filter_by(vote_id=vote_id).first()
        db.session.delete(vote)
        db.session.commit()
        return vote.vote_id
    
    def get_all_post_votes(self):
        votes = PostVote.query.all()
        return votes
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
        new_vote = PostVote(post_id, voter_id, is_upvote)
        db.session.add(new_vote)
        db.session.commit()
        return new_vote
    
    def create_comment_vote(self, comment_id, voter_id, is_upvote):
        new_vote = CommentVote(comment_id, voter_id, is_upvote)
        db.session.add(new_vote)
        db.session.commit()
        return new_vote

    

vote_repository_singleton = VoteRepository()