from flask.testing import FlaskClient
from src.repositories.user_repository import user_repository_singleton
from tests.utils import clear_db
from app import app  

def test_search_user(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.get('/users/search')
        response_data = response.data.decode('utf-8')

    assert '<h1 class="mt-3 mb-4">Search Users</h1>' in response_data

def test_search_user_no_results(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.get('/users/search?q=blank')
        response_data = response.data.decode('utf-8')

    assert '<p>No users found</p>' in response_data    

def test_search_movie_success(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        user_repository_singleton.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        response = test_app.get('/users/search?q=joe_smith')
        response_data = response.data.decode('utf-8')

    assert '<td>joe</td>' in response_data
    assert '<td>smith</td>' in response_data