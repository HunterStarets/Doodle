from flask.testing import FlaskClient
from src.repositories.user_repository import user_repository_singleton
from src.repositories.post_repository import post_repository_singleton
from tests.utils import clear_db
from datetime import datetime
from app import app  

def test_delete_post_success(test_app: FlaskClient):
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
            'community-name': 'test-name',
        }, follow_redirects=True)

        user = user_repository_singleton.get_user_by_username('joe_smith')
        user_id = user_repository_singleton.get_users_id(user)
        post = post_repository_singleton.get_single_post(user_id)

        response = test_app.post(f'/posts/{post.post_id}/delete', follow_redirects=True)
        response_data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<a class="px-2" id="delete-post-link" href="#">Delete</a>' not in response_data


def test_delete_post_failure(test_app: FlaskClient):
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


        response = test_app.post(f'/posts/000/delete', follow_redirects=True)
        response_data = response.data.decode('utf-8')

    assert response.status_code == 404
