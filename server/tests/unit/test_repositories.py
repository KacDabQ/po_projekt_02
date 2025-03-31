import pytest
from usermanager.repositories import User, UserNotFound, UserRepository

@pytest.fixture
def repository():
    return UserRepository()

def test_get_non_existing_user(repository):
    user = repository.get_by_id(99999999)

    assert user is None

def test_get_all_no_data(repository):
    users = repository.get_all()
    assert users is not None
    assert len(users) == 0

def test_get_all_with_data(repository):
    user = User(0, "John", "Doe", 1995, "admin")
    repository.add(user)
    user = User(0, "John", "Doe", 1995, "admin")
    repository.add(user)

    users = repository.get_all()
    assert len(users) == 2

def test_create_user(repository):
    user = User(0, "John", "Doe", 1995, "admin")

    repository.add(user)

    user = repository.get_by_id(user.id)
    assert user is not None
    assert user.id > 0


def test_delete_existing_user(repository):
    user = User(0, "John", "Doe", 1995, "admin")
    repository.add(user)

    repository.delete_by_id(user.id)

    user = repository.get_by_id(user.id)

    assert user is None


def test_delete_non_existing_user(repository):
    with pytest.raises(UserNotFound):
        repository.delete_by_id(99999)
