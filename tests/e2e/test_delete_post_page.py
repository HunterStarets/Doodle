# from flask.testing import FlaskClient
# from src.repositories.user_repository import user_repository_singleton
# from src.repositories.post_repository import post_repository_singleton
# from tests.utils import clear_db
# from datetime import datetime
# from app import app  

# def test_delete_post_success(test_app: FlaskClient):
#     with app.app_context():
#         clear_db()
#         response = test_app.post('/signup', data={
#             'email': 'joe@gmail.com',
#             'username': 'joe_smith',
#             'password': 'abc',
#             'first-name': 'joe',
#             'last-name': 'smith',
#             'bio': 'bio'
#         }, follow_redirects=True)

#         user = user_repository_singleton.get_user_by_username('joe_smith')
#         user_id = user_repository_singleton.get_users_id(user)
#         timestamp = timestamp = datetime.utcnow()

#         response = test_app.post('/posts', data={
#             'title': 'todays news',
#             'content': 'blah',
#             'community-name': 'world news',
#         }, follow_redirects=True)

#         post = post_repository_singleton.get_all_posts_by_author_id(user_id)
#         post_id = post_repository_singleton.get_post_id(post)
#         # response = test_app.post(f'/posts/{post_id}/delete', follow_redirects=True)
#         # post = post_repository_singleton.create_post('test_title', 'test_body', 'test_name', timestamp, user_id)
#         # post_id = post_repository_singleton.get_post_id(post)
#         response = test_app.get(f'/posts/{post_id}')

#         assert response.status_code == 200