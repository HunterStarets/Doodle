from flask.testing import FlaskClient
from tests.utils import clear_db
from src.repositories.user_repository import user_repository_singleton

from app import app  

def test_home_page(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.get('/')
        response_data = response.data.decode('utf-8')

    assert '<div class="col-md-9">' in response_data
    assert response.status_code == 200
    
def test_post_lists(test_app: FlaskClient):
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

        response = test_app.get('/')
        response_data = response.data.decode('utf-8')

    assert '<a class="px-2" id="delete-post-link" href="#">Delete</a>' in response_data

