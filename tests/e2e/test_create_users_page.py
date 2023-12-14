from flask.testing import FlaskClient
from src.repositories.user_repository import user_repository_singleton
from tests.utils import clear_db
from app import app  

def test_create_user_success(test_app: FlaskClient):
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
        response_data = response.data.decode('utf-8')

    assert '<h5 class="card-title">joe_smith</h5>' in response_data
    assert '<a class="nav-link active" href="#" onclick="logout()">Logout</a>' in response_data

def test_create_user_failure(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.post('/signup', data={}, follow_redirects=True)

    assert response.status_code == 400
    
def test_existing_email(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        user_repository_singleton.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        response = test_app.post('/signup', data={
            'email': 'joe@gmail.com',
            'username': 'joe_smith2',
            'password': 'abc',
            'first-name': 'joe',
            'last-name': 'smith',
            'bio': 'bio'
        }, follow_redirects=True)

    assert response.status_code == 400

def test_existing_username(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        user_repository_singleton.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        response = test_app.post('/signup', data={
            'email': 'joe2@gmail.com',
            'username': 'joe_smith',
            'password': 'abc',
            'first-name': 'joe',
            'last-name': 'smith',
            'bio': 'bio'
        }, follow_redirects=True)

    assert response.status_code == 400 