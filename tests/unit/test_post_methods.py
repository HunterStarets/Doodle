from flask.testing import FlaskClient
from src.repositories.post_repository import post_repository_singleton
from src.repositories.user_repository import user_repository_singleton
from tests.utils import clear_db
from app import app  
import datetime

def test_create_post_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")

        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        found_post = post_repo.get_post_by_id(test_post.post_id)

        assert found_post is not None
        assert found_post.title =="Test Post"
        assert found_post.content == "This is a test"
        assert found_post.community_name == "Test_Community"
        assert found_post.timestamp == datetime.datetime(2023,12,14,10,0,0)
        assert found_post.author_id == test_user.user_id



def test_get_posts_by_id_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")

        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)

        found_post = post_repo.get_post_by_id(test_post.post_id)
        assert found_post is not None
        assert found_post.title =="Test Post"
        assert found_post.content == "This is a test"
        assert found_post.community_name == "Test_Community"
        assert found_post.timestamp == datetime.datetime(2023,12,14,10,0,0)
        assert found_post.author_id == test_user.user_id

def test_get_posts_by_ids_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")

        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post 2","This is also a test","Test_Community2",'2023-12-14 11:00:00',test_user.user_id)

        test_ids = [test_post.post_id,test_post2.post_id]

        posts = post_repo.get_posts_by_ids(test_ids)

        assert len(posts) == 2
        assert test_post in posts
        assert test_post2 in posts

def test_get_posts_by_author():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")

        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post 2","This is also a test","Test_Community2",'2023-12-14 11:00:00',test_user.user_id)

        posts = post_repo.get_all_posts_by_author_id(test_user.user_id)
        assert len(posts) == 2
        assert test_post in posts
        assert test_post2 in posts

def test_get_all_posts_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")


        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-14 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post 2","This is also a test","Test_Community2",'2023-12-14 11:00:00',test_user2.user_id)
        test_post3 = post_repo.create_post("Test Post 3","This is also also a test","Test_Community3",'2023-12-14 12:00:00',test_user.user_id)

        posts = post_repo.get_all_posts()
        assert len(posts) == 3
        assert test_post in posts
        assert test_post2 in posts
        assert test_post3 in posts
#not sure this is working correctly...
def test_get_all_posts__ordered_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")


        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-12 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post 2","This is also a test","Test_Community2",'2023-12-13 11:00:00',test_user2.user_id)
        test_post3 = post_repo.create_post("Test Post 3","This is also also a test","Test_Community3",'2023-12-14 12:00:00',test_user.user_id)

        posts = post_repo.get_all_posts()
        assert len(posts) == 3
        assert test_post in posts
        assert test_post2 in posts
        assert test_post3 in posts
        assert posts[-1] == test_post3
        assert posts[-2] == test_post2
        assert posts[-3] == test_post

def test_edit_posts_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")


        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-12 10:00:00',test_user.user_id)

        post_repo.edit_post(test_post,"New Title","new content","new_community")

        found_post = post_repo.get_post_by_id(test_post.post_id)
        assert found_post.title == "New Title"
        assert found_post.content == "new content"
        assert found_post.community_name == "new_community"

def test_delete_post_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton
        post_repo = post_repository_singleton

        test_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        test_user2 = user_repo.create_user("joe2@gmail.com", "joe2_smith", "abc", "joe", "smith", "bio")


        test_post = post_repo.create_post("Test Post","This is a test","Test_Community",'2023-12-12 10:00:00',test_user.user_id)
        test_post2 = post_repo.create_post("Test Post 2","This is also a test","Test_Community2",'2023-12-13 11:00:00',test_user2.user_id)
        test_post3 = post_repo.create_post("Test Post 3","This is also also a test","Test_Community3",'2023-12-14 12:00:00',test_user.user_id)

        post_repo.delete_post(test_post2)

        posts = post_repo.get_all_posts()
        assert len(posts) == 2
        assert test_post in posts
        assert test_post3 in posts
        assert test_post2 not in posts
