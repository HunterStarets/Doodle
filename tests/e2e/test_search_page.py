from flask.testing import FlaskClient
from app import app  

def test_delete(test_app: FlaskClient):
    with app.app_context():
        response = test_app.get('/users/search')
        response_data = response.data.decode('utf-8')

    assert '<h1 class="mt-3 mb-4">Search Users</h1>' in response_data
    