from src.models import db

class VoteRepository:

    def get_net_post_votes(self, post_id):
        return 120
        #votes = PostVote.query.filter(PostVote.post_id == post_id).all()
        #
        #upvotes = []
        #downvotes = []
        #
        #for vote in votes:
        #    if vote.is_upvote:
        #        upvotes.append(vote)
        #    else:
        #        downvotes.append(vote)
        
        #net_votes = len(upvotes) - len(downvotes)
        #return net_votes
    
    def get_net_comment_votes(self, comment_id):
        return 100
        #votes = CommentVote.query.filter(CommentVote.comment_id == comment_id).all()
        #
        #upvotes = []
        #downvotes = []
        #
        #for vote in votes:
        #    if vote.is_upvote:
        #        upvotes.append(vote)
        #    else:
        #        downvotes.append(vote)
        #
        #net_votes = len(upvotes) - len(downvotes)
        #return net_votes

    #def create_post_vote(self, post_id, voter_id, is_upvote):
        #new_vote = PostVote(post_id=post_id, voter_id=voter_id, is_upvote=is_upvote)
        #db.session.add(new_vote)
        #db.session.commit()
        #return new_vote
    
    #def create_comment_vote(self, comment_id, voter_id, is_upvote):
        #new_vote = CommentVote(comment_id=comment_id, voter_id=voter_id, is_upvote=is_upvote)
        #db.session.add(new_vote)
        #db.session.commit()
        #return new_vote


vote_repository_singleton = VoteRepository()