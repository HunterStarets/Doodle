from flask.testing import FlaskClient
from src.repositories.post_repository import post_repository_singleton
from tests.utils import clear_db
from app import app  

def test_create_post_logged_out(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.post('/posts', data={
            'title': 'test-title',
            'content': 'test-content',
            'community-name': 'test-name'
        }, follow_redirects=True)

    assert response.status_code == 401

def test_create_post_success(test_app: FlaskClient):
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
        response_data = response.data.decode('utf-8')

    assert 'test-content</textarea>' in response_data
    assert '<strong class="pe-2">test-title'

def test_create_post_failure(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.post('/posts', data={}, follow_redirects=True)

    assert response.status_code == 400
