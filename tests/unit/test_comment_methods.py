from flask.testing import FlaskClient
from src.repositories.comment_repository import comment_repository_singleton
from src.repositories.post_repository import post_repository_singleton
from src.repositories.user_repository import user_repository_singleton
from tests.utils import clear_db
from app import app  


def test_create_comment_unit():
    with app.app_context():
        clear_db()
        comment_repo = comment_repository_singleton
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)


        created_comment = comment_repo.create_comment("This is a test","2023-12-15 10:00:00",test_post.post_id,test_user.user_id)
        found_comment = comment_repo.get_comment_by_id(created_comment.comment_id)

        assert found_comment is not None
        assert found_comment.content == "This is a test"
        assert found_comment.author_id == test_user.user_id
        assert found_comment.post_id == test_post.post_id

def test_get_comment_by_id_unit():
    with app.app_context():
        clear_db()
        comment_repo = comment_repository_singleton
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)


        created_comment = comment_repo.create_comment("This is a test","2023-12-15 10:00:00",test_post.post_id,test_user.user_id)

        found_comment = comment_repo.get_comment_by_id(created_comment.comment_id)

        assert found_comment is not None
        assert found_comment.post_id == test_post.post_id
        assert found_comment.content == "This is a test"
        assert found_comment.author_id == test_user.user_id

def test_get_comments_for_post_unit():
    with app.app_context():
        clear_db()
        comment_repo = comment_repository_singleton
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        test_comment1 = comment_repo.create_comment("this is a test","2023-12-14 10:01:00",test_post.post_id,test_user.user_id)
        test_comment2 = comment_repo.create_comment("this is also a test","2023-12-14 10:02:00",test_post.post_id,test_user.user_id)

        comments_on_post = comment_repo.get_comments_for_post(test_post.post_id)

        assert len(comments_on_post) == 2
        assert test_comment1 in comments_on_post
        assert test_comment2 in comments_on_post

def test_get_comments_for_user_unit():
    with app.app_context():
        clear_db()
        comment_repo = comment_repository_singleton
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post 2","This is also a test","Test_Community2",'2023-12-14 10:01:00',test_user.user_id)


        test_comment1 = comment_repo.create_comment("this is a test","2023-12-14 10:01:00",test_post.post_id,test_user.user_id)
        test_comment2 = comment_repo.create_comment("this is also a test","2023-12-14 10:02:00",test_post2.post_id,test_user.user_id)

        comments_for_user = comment_repo.get_comments_for_user(test_user.user_id)

        assert len(comments_for_user) == 2
        assert test_comment1 in comments_for_user
        assert test_comment2 in comments_for_user

def test_delete_comments():
    with app.app_context():
        clear_db()
        comment_repo = comment_repository_singleton
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post 2","This is also a test","Test_Community2",'2023-12-14 10:01:00',test_user.user_id)


        test_comment1 = comment_repo.create_comment("this is a test","2023-12-14 10:01:00",test_post.post_id,test_user.user_id)
        test_comment2 = comment_repo.create_comment("this is also a test","2023-12-14 10:02:00",test_post2.post_id,test_user.user_id)

        comment_repo.delete_comment(test_comment2)

        comments_for_user = comment_repo.get_comments_for_user(test_user.user_id)
        assert len(comments_for_user) == 1
        assert test_comment1 in comments_for_user
        assert test_comment2 not in comments_for_user

def test_edit_comment_unit():
    with app.app_context():
        clear_db()
        comment_repo = comment_repository_singleton
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        test_comment1 = comment_repo.create_comment("this is a test","2023-12-14 10:01:00",test_post.post_id,test_user.user_id)

        comment_repo.edit_comment(test_comment1,"new test content")

        found_comment = comment_repo.get_comment_by_id(test_comment1.comment_id)
        assert found_comment is not None
        assert found_comment.content == "new test content"