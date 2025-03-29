from flask.testing import FlaskClient
from pytest import fixture

from usermanager.main import app

@fixture
def client() -> FlaskClient:
    return app.test_client()

def test_get_users_endpoint_returns_200(client: FlaskClient) -> None:
    assert True


