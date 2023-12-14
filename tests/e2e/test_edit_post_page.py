from flask.testing import FlaskClient
from src.repositories.post_repository import post_repository_singleton
from src.repositories.user_repository import user_repository_singleton
from tests.utils import clear_db
from datetime import datetime
from app import app  

def test_edit_post_logged_out(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.get('/posts/1/edit')
        response_data = response.data.decode('utf-8')

    assert response.status_code == 401

def test_edit_post_success(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.post('/signup', data={
            'email': 'joe@gmail.com',
            'username': 'joe_smith',
            'password': 'abc',
            'first-name': 'joe',
            'last-name': 'smith',
            'bio': 'bio'
        }, follow_redirects=True)

        response = test_app.post('/posts', data={
            'title': 'test-title',
            'content': 'test-content',
            'community-name': 'test-name'
        }, follow_redirects=True)
        
        user = user_repository_singleton.get_user_by_username('joe_smith')
        user_id = user_repository_singleton.get_users_id(user)
        post = post_repository_singleton.get_single_post(user_id)
        
        response = test_app.post(f'/posts/{post.post_id}', data={
            'title': 'new-title',
            'content': 'new-content',
            'community-name': 'new-name'
        }, follow_redirects=True)
        response_data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert 'new-content</textarea>' in response_data

def test_edit_post_empty(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.post('/signup', data={
            'email': 'joe@gmail.com',
            'username': 'joe_smith',
            'password': 'abc',
            'first-name': 'joe',
            'last-name': 'smith',
            'bio': 'bio'
        }, follow_redirects=True)
        user = user_repository_singleton.get_user_by_username('joe_smith')
        user_id = user_repository_singleton.get_users_id(user)

        response = test_app.post('/posts', data={
            'title': 'test-title',
            'content': 'test-content',
            'community-name': 'test-name'
        }, follow_redirects=True)
        
        post = post_repository_singleton.get_single_post(user_id)
        response = test_app.post(f'/posts/{post.post_id}', data={}, follow_redirects=True)
        response_data = response.data.decode('utf-8')

    assert response.status_code == 400


def test_edit_post_unauthorized(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        user_repository_singleton.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")

        response = test_app.post('/signup', data={
            'email': 'serg@gmail.com',
            'username': 'serg_joya',
            'password': 'abc',
            'first-name': 'serg',
            'last-name': 'joya',
            'bio': 'bio'
        }, follow_redirects=True)

        timestamp = datetime.utcnow()
        user = user_repository_singleton.get_user_by_username('joe_smith')
        user_id = user_repository_singleton.get_users_id(user)

        new_post = post_repository_singleton.create_post('title', 'content', 'name', timestamp, user_id)
        response = test_app.get(f'/posts/{new_post.post_id}/edit')

    assert response.status_code == 403