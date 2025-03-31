from flask.testing import FlaskClient
import pytest
from usermanager.main import app
from pytest import fixture

@fixture
def client() -> FlaskClient:
    return app.test_client()


def test_get_users_returs_list_of_users(client: FlaskClient) -> None:
    response = client.get('/users')
    assert response.status_code == 200


def test_create_user(client: FlaskClient) -> None:
    pre_test_users_count = len(client.get('/users').json)

    response = client.post('/users', json={
        "firstname": "John",
        "lastname": "Doe",
        "birthyear": 1995,
        "group": "admin"
    })
    assert response.status_code == 200
    assert response.json['id'] > 0
    new_id = int(response.json['id'])

    response = client.get('/users')
    assert len(response.json) == pre_test_users_count + 1

    response = client.get(f'/users/{new_id}')
    assert response.status_code == 200
    assert response.json['firstname'] == 'John'
    assert response.json['lastname'] == 'Doe'
    assert response.json['age'] == 30
    assert response.json['group'] == 'admin'


def test_delete_user(client: FlaskClient) -> None:
    response = client.post('/users', json={
        "firstname": "John",
        "lastname": "Doe",
        "birthyear": 1995,
        "group": "admin"
    })
    assert response.status_code == 200
    assert response.json['id'] > 0
    new_id = int(response.json['id'])

    response = client.delete(f'/users/{new_id}')

    response = client.get(f'/users{new_id}')
    assert response.status_code == 404

@pytest.mark.parametrize("tested_group,expected_status_code", [
    ("admin", 200),
    ("premium", 200),
    ("user", 200),
    ("root", 400)])
def test_create_user_with_non_existant_group(tested_group: str, expected_status_code: int, client: FlaskClient) -> None:
    response = client.post('/users', json={
        "firstname": "John",
        "lastname": "Doe",
        "birthyear": 1995,
        "group": tested_group
    })
    assert response.status_code == expected_status_code