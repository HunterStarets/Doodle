def test_index_page(test_app):
    response = test_app.get('/')

    data = response.data.decode('utf-8')

    assert response.status_code == 200
    #assert '<h1>hello world</h1>' in data


def test_create_user(test_app):
    test_app.post('')