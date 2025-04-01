from unittest.mock import call, Mock
from pytest import fixture, raises

from usermanager.controllers import NonExistingGroup, UserController
from usermanager.repositories import UserRepository


@fixture
def repository() -> Mock:
    return Mock(UserRepository)

@fixture
def controller(repository: Mock) -> UserController:
    return UserController(repository)

def test_user_controller_create_calls_add_in_repository(
        controller: UserController,
        repository: Mock):
    dict = {
        "firstname": "John",
        "lastname": "Doe",
        "birthyear": 1995,
        "group": "admin"
    }

    created_user = controller.create(dict)
    assert created_user.firstname == "John"
    assert created_user.lastname == "Doe"
    assert created_user.birthyear == 1995
    assert created_user.group == "admin"

    expected = call(created_user)
    assert expected in repository.add.mock_calls

def test_user_controller_create_with_wrong_group_not_call_add_in_repository(
        controller: UserController,
        repository: Mock):
    dict = {
        "firstname": "John",
        "lastname": "Doe",
        "birthyear": 1995,
        "group": "non existing"
    }

    with raises(NonExistingGroup):
        controller.create(dict)

    repository.add.assert_not_called()

def test_user_controller_delete_calls_delete_by_id_in_repository(
        controller: UserController,
        repository: Mock):
    controller.delete(999)

    expected = call(999)

    assert expected in repository.delete_by_id.mock_calls

def test_user_controller_get_all_calls_get_all_in_repository(
        controller: UserController,
        repository: Mock):
    controller.get_all()

    expected = call()

    assert expected in repository.get_all.mock_calls

def test_user_controller_get_calls_get_by_id_in_repository(
        controller: UserController,
        repository: Mock):
    controller.get(999)

    expected = call(999)

    assert expected in repository.get_by_id.mock_calls  