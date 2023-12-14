from flask.testing import FlaskClient
from src.repositories.user_repository import user_repository_singleton
from tests.utils import clear_db
from app import app  

def test_edit_user_logged_out(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        user_repository_singleton.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        user = user_repository_singleton.get_user_by_username("joe_smith")
        user_id = user_repository_singleton.get_users_id(user)
        response = test_app.get(f'/users/{user_id}/edit')

    assert response.status_code == 401

def test_edit_user_unauthorized(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        user_repository_singleton.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        user = user_repository_singleton.get_user_by_username("joe_smith")
        user_id = user_repository_singleton.get_users_id(user)

        response = test_app.post('/signup', data={
            'email': 'serg@gmail.com',
            'username': 'serg_joya',
            'password': 'abc',
            'first-name': 'serg',
            'last-name': 'joya',
            'bio': 'bio'
        }, follow_redirects=True)
        response = test_app.get(f'/users/{user_id}/edit')

    assert response.status_code == 403

def test_edit_user_empty(test_app: FlaskClient):
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
        user = user_repository_singleton.get_user_by_username("joe_smith")
        user_id = user_repository_singleton.get_users_id(user)

        response = test_app.post(f'/users/{user_id}', data={}, follow_redirects=True)

    assert response.status_code == 400

def test_edit_user_existing_email(test_app: FlaskClient):
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
        user = user_repository_singleton.get_user_by_username("serg_joya")
        user_id = user_repository_singleton.get_users_id(user)

        response = test_app.post(f'/users/{user_id}', data={
            'email': 'joe@gmail.com',
            'username': 'serg_joya',
            'current-password': 'abc',
            'new-password': 'abc',
            'first-name': 'serg',
            'last-name': 'joya',
            'bio': 'bio'
        }, follow_redirects=True)

    assert response.status_code == 400

def test_edit_user_existing_username(test_app: FlaskClient):
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
        user = user_repository_singleton.get_user_by_username("serg_joya")
        user_id = user_repository_singleton.get_users_id(user)

        response = test_app.post(f'/users/{user_id}', data={
            'email': 'serg@gmail.com',
            'username': 'joe_smith',
            'current-password': 'abc',
            'new-password': 'abc',
            'first-name': 'serg',
            'last-name': 'joya',
            'bio': 'bio'
        }, follow_redirects=True)

    assert response.status_code == 400


def test_edit_user_wrong_password(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.post('/signup', data={
            'email': 'serg@gmail.com',
            'username': 'serg_joya',
            'password': 'abc',
            'first-name': 'serg',
            'last-name': 'joya',
            'bio': 'bio'
        }, follow_redirects=True)
        user = user_repository_singleton.get_user_by_username("serg_joya")
        user_id = user_repository_singleton.get_users_id(user)

        response = test_app.post(f'/users/{user_id}', data={
            'email': 'serg@gmail.com',
            'username': 'serg_joya',
            'current-password': '123',
            'new-password': 'abc',
            'first-name': 'serg',
            'last-name': 'joya',
            'bio': 'bio'
        }, follow_redirects=True)

    assert response.status_code == 401



def test_edit_user_success(test_app: FlaskClient):
    with app.app_context():
        clear_db()
        response = test_app.post('/signup', data={
            'email': 'serg@gmail.com',
            'username': 'serg_joya',
            'password': 'abc',
            'first-name': 'serg',
            'last-name': 'joya',
            'bio': 'bio'
        }, follow_redirects=True)
        user = user_repository_singleton.get_user_by_username("serg_joya")
        user_id = user_repository_singleton.get_users_id(user)

        response = test_app.post(f'/users/{user_id}', data={
            'email': 'joe@gmail.com',
            'username': 'joe_smith',
            'current-password': 'abc',
            'new-password': 'abc',
            'first-name': 'joe',
            'last-name': 'smith',
            'bio': 'bio'
        }, follow_redirects=True)
        response_data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<h5 class="card-title">joe_smith</h5>' in response_data
