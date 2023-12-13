from flask.testing import FlaskClient
from tests.utils import clear_db
from app import app  

def test_delete(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.get('/users/search')
        response_data = response.data.decode('utf-8')


    assert response.status_code == 200
