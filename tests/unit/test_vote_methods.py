from flask.testing import FlaskClient
from src.repositories.post_repository import post_repository_singleton
from src.repositories.user_repository import user_repository_singleton
from src.repositories.comment_repository import comment_repository_singleton
from src.repositories.vote_repostory import vote_repository_singleton
from tests.utils import clear_db
from app import app  
import datetime

def test_create_post_vote_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        created_vote = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)

        assert created_vote is not None
        assert created_vote.post_id == test_post.post_id
        assert created_vote.voter_id == test_user.user_id
        assert created_vote.is_upvote == True

def test_create_comment_vote_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        created_vote = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)

        assert created_vote is not None
        assert created_vote.comment_id == test_comment.comment_id
        assert created_vote.voter_id == test_user.user_id
        assert created_vote.is_upvote == True


def test_get_net_comment_votes_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        vote1 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)
        vote2 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,False)
        vote3 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)
        vote4 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)
        vote5 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)

        karma = vote_repo.get_net_comment_votes(test_comment.comment_id)
        assert karma == 3


def test_get_net_post_votes_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        vote1 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote2 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,False)
        vote3 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote4 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote5 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)

        karma = vote_repo.get_net_post_votes(test_post.post_id)
        assert karma == 3

def test_get_all_post_votes_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post2","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        vote1 = vote_repo.create_post_vote(test_post2.post_id,test_user.user_id,True)
        vote2 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,False)
        vote3 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote4 = vote_repo.create_post_vote(test_post2.post_id,test_user.user_id,True)
        vote5 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)

        votes = vote_repo.get_all_post_votes()

        assert len(votes) == 5
        assert vote1 in votes
        assert vote2 in votes
        assert vote3 in votes
        assert vote4 in votes
        assert vote5 in votes



def test_get_post_votes_by_post_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post2","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        vote1 = vote_repo.create_post_vote(test_post2.post_id,test_user.user_id,True)
        vote2 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,False)
        vote3 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote4 = vote_repo.create_post_vote(test_post2.post_id,test_user.user_id,True)
        vote5 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)

        votes = vote_repo.get_post_votes_by_post_id(test_post.post_id)

        assert len(votes) == 3
        assert vote1 not in votes
        assert vote2 in votes
        assert vote3 in votes
        assert vote4 not in votes
        assert vote5 in votes

def test_get_comment_votes_by_comment_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)


        vote1 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)
        vote2 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,False)
        vote3 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)
        vote4 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)
        vote5 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)

        votes = vote_repo.get_comment_votes_by_comment_id(test_comment.comment_id)

        assert len(votes) == 5
        assert vote1 in votes
        assert vote2 in votes
        assert vote3 in votes
        assert vote4 in votes
        assert vote5 in votes
        

def test_get_post_vote_by_id_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post2","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        vote1 = vote_repo.create_post_vote(test_post2.post_id,test_user.user_id,True)
        vote2 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,False)
        vote3 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote4 = vote_repo.create_post_vote(test_post2.post_id,test_user.user_id,True)
        vote5 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)

        selected_vote = vote_repo.get_post_vote_by_id(vote3.vote_id)

        assert selected_vote.post_id == vote3.post_id
        assert selected_vote.voter_id == vote3.voter_id
        assert selected_vote.is_upvote == vote3.is_upvote

def test_get_post_upvotes_by_user_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post2","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        vote1 = vote_repo.create_post_vote(test_post2.post_id,test_user2.user_id,True)
        vote2 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote3 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,False)
        vote4 = vote_repo.create_post_vote(test_post2.post_id,test_user.user_id,True)
        vote5 = vote_repo.create_post_vote(test_post.post_id,test_user2.user_id,True)

        votes = vote_repo.get_post_upvotes_by_user_id(test_user.user_id)

        assert len(votes) == 2
        assert vote2 in votes
        assert vote4 in votes



def test_get_post_downvotes_by_user_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post2","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        vote1 = vote_repo.create_post_vote(test_post2.post_id,test_user2.user_id,True)
        vote2 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,False)
        vote3 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote4 = vote_repo.create_post_vote(test_post2.post_id,test_user.user_id,False)
        vote5 = vote_repo.create_post_vote(test_post.post_id,test_user2.user_id,True)

        votes = vote_repo.get_post_downvotes_by_user_id(test_user.user_id)

        assert len(votes) == 2
        assert vote2 in votes
        assert vote4 in votes

def test_get_post_vote_by_post_user_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post2","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        vote1 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote2 = vote_repo.create_post_vote(test_post.post_id,test_user2.user_id,False)
        

        selected_vote = vote_repo.get_post_vote_by_post_and_user_ids(test_post.post_id,test_user.user_id)

        assert selected_vote == vote1

def test_get_comment_vote_by_comment_user_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)


        vote1 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)
        vote2 = vote_repo.create_comment_vote(test_comment.comment_id,test_user2.user_id,False)
        

        selected_vote = vote_repo.get_comment_vote_by_comment_and_user_ids(test_comment.comment_id,test_user.user_id)

        assert selected_vote == vote1
    
def test_get_all_post_user_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post2","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        vote1 = vote_repo.create_post_vote(test_post2.post_id,test_user2.user_id,True)
        vote2 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,False)
        vote3 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote4 = vote_repo.create_post_vote(test_post2.post_id,test_user.user_id,False)
        vote5 = vote_repo.create_post_vote(test_post.post_id,test_user2.user_id,True)

        votes = vote_repo.get_all_post_votes_by_user_id(test_user.user_id)

        assert len(votes) == 3
        assert vote2 in votes
        assert vote3 in votes
        assert vote4 in votes

def test_get_all_comment_user_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)


        vote1 = vote_repo.create_comment_vote(test_comment.comment_id,test_user2.user_id,True)
        vote2 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,False)
        vote3 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)
        vote4 = vote_repo.create_comment_vote(test_comment.comment_id,test_user2.user_id,True)
        vote5 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)

        votes = vote_repo.get_all_comment_votes_by_user_id(test_user.user_id)

        assert len(votes) == 3
        assert vote2 in votes
        assert vote3 in votes
        assert vote5 in votes
        

def test_delete_post_vote_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post2","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)

        vote1 = vote_repo.create_post_vote(test_post2.post_id,test_user2.user_id,True)
        vote2 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,False)
        vote3 = vote_repo.create_post_vote(test_post.post_id,test_user.user_id,True)
        vote4 = vote_repo.create_post_vote(test_post2.post_id,test_user.user_id,False)
        vote5 = vote_repo.create_post_vote(test_post.post_id,test_user2.user_id,True)

        vote_repo.delete_post_vote_by_id(vote2.vote_id)

        votes = vote_repo.get_all_post_votes_by_user_id(test_user.user_id)

        assert len(votes) == 2
        assert vote3 in votes
        assert vote4 in votes


def test_delete_comment_vote_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton
        comment_repo = comment_repository_singleton
        vote_repo = vote_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_comment = comment_repo.create_comment("test content",'2023-12-14 10:01:00',test_post.post_id,test_user.user_id)


        vote1 = vote_repo.create_comment_vote(test_comment.comment_id,test_user2.user_id,True)
        vote2 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,False)
        vote3 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)
        vote4 = vote_repo.create_comment_vote(test_comment.comment_id,test_user2.user_id,True)
        vote5 = vote_repo.create_comment_vote(test_comment.comment_id,test_user.user_id,True)

        vote_repo.delete_comment_vote_by_id(vote2.vote_id)

        votes = vote_repo.get_all_comment_votes_by_user_id(test_user.user_id)

        assert len(votes) == 2
        assert vote3 in votes
        assert vote5 in votes


