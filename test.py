import pytest
from main import app, db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect


@pytest.fixture(autouse=True, scope='session')
def prepare_db():
    db.create_all()
    yield
    db.drop_all()

@pytest.fixture(autouse=True)
def unlock_db():
    yield
    db.session.commit()

# DEF ------------------------
def test_review_add():
    with app.test_client() as client:
        response = client.post('/add-review', json={
            'book_name': 'ASDF',
            'rating': 3,
            'review': 'QWERTY'
        })
        assert response.status_code == 200

def test_get_book_id():
    with app.test_client() as client:
        response = client.post('/search', json={
            'query': 'ASDF',
        })
        assert response.status_code == 200
        assert int(response.json['book_id']) == 1

# MY ---------------------------------------------------------------------------

def test_review_false_value_add():
    with app.test_client() as client:
        response = client.post('/add-review', json={
            'book_name': 'WSB',
            'review' : '2/10'
        })
        assert response.status_code != 200

def test_input_text_plus_500_char():
    with app.test_client() as client:
        response = client.post('/add-review', json={
            'book_name': 10000 * 'a',
            'rating': 3,
            'review' : 10000 * '2/10'
        })
        assert response.status_code == 200

def test_home_page():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 500


def test_go_try_GET():
    with app.test_client() as client:
        response = client.get('/add-review', json={
            'book_name': 10000 * 'a',
            'rating': 3,
            'review' : 10000 * '2/10'
        })
        assert response.status_code != 200

def test_get_book_false_name():
    with app.test_client() as client:
        response = client.post('/search', json={
            'query': 'WSB32323',
        })
        assert response.status_code == 500
