from flask.testing import FlaskClient
from src.repositories.user_repository import user_repository_singleton
from tests.utils import clear_db
from app import app  

def test_search_user_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton

        user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        found_user = user_repo.search_users("joe_smith")

        assert found_user is not None
        assert found_user.username == "joe_smith"

def test_get_user_by_email_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton

        user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        found_user = user_repo.get_user_by_email("joe@gmail.com")
        
        assert found_user is not None
        assert found_user.email == "joe@gmail.com"
        assert found_user.username == "joe_smith"

def test_get_user_by_id_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton

        created_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")    
        created_user_id = created_user.user_id
        found_user = user_repo.get_user_by_id(created_user_id)

        assert found_user is not None
        assert found_user.username == "joe_smith"

def test_get_user_by_username_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton

        user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        found_user = user_repo.get_user_by_username("joe_smith")

        assert found_user is not None
        assert found_user.username == "joe_smith"

def test_create_user_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton

        user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        found_user = user_repo.get_user_by_username("joe_smith")

        assert found_user is not None
        assert found_user.username == "joe_smith"
        assert found_user.email == "joe@gmail.com"
        assert found_user.password == "abc"
        assert found_user.first_name == "joe"
        assert found_user.last_name == "smith"
        assert found_user.bio == "bio"


def test_edit_user_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton

        created_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        user_repo.edit_user(created_user,"joe2@gmail.com","joe2_smith","abc","joe","smith","bio")

        found_user = user_repo.get_user_by_username("joe2_smith")


        assert found_user is not None
        assert found_user.username == "joe2_smith"
        assert found_user.email == "joe2@gmail.com"
        assert found_user.password == "abc"
        assert found_user.first_name == "joe"
        assert found_user.last_name == "smith"
        assert found_user.bio == "bio"

def test_delete_user_unit():
    with app.app_context():
        clear_db()
        user_repo = user_repository_singleton

        created_user = user_repo.create_user("joe@gmail.com", "joe_smith", "abc", "joe", "smith", "bio")
        user_repo.delete_user(created_user)

        found_user = user_repo.search_users("joe_smith")

        assert found_user is None

