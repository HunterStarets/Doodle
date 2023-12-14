from flask.testing import FlaskClient
from src.repositories.user_repository import user_repository_singleton
from tests.utils import clear_db
from app import app  

# def test_delete_user_logged_out(test_app: FlaskClient):
#     with app.app_context():
#         clear_db()
#         user_repository_singleton.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
#         user = user_repository_singleton.get_user_by_username("joe_smith")
#         print(user)
#         response = test_app.get(f'/users/{user.user_id}')
#         response_data = response.data.decode('utf-8')

#     assert 5 > 1