import pytest
from usermanager.repositories import Person, PersonNotFound, PersonRepository

def test_get_non_existing_user():
    repository = PersonRepository()
    person = repository.get_by_id(99999999)

    assert person is None

def test_get_all_no_data():
    repository = PersonRepository()

    persons = repository.get_all()
    assert persons is not None
    assert len(persons) == 0

def test_get_all_with_data():
    repository = PersonRepository()
    person = Person(0, "John", "Doe", 1995, "admin")
    repository.add(person)
    person = Person(0, "John", "Doe", 1995, "admin")
    repository.add(person)

    persons = repository.get_all()
    assert len(persons) == 2

def test_create_person():
    repository = PersonRepository()
    person = Person(0, "John", "Doe", 1995, "admin")

    repository.add(person)

    person = repository.get_by_id(person.id)
    assert person is not None
    assert person.id > 0


def test_delete_existing_person():
    repository = PersonRepository()
    person = Person(0, "John", "Doe", 1995, "admin")
    repository.add(person)

    repository.delete_by_id(person.id)

    person = repository.get_by_id(person.id)

    assert person is None


def test_delete_non_existing_person():
    repository = PersonRepository()

    with pytest.raises(PersonNotFound):
        repository.delete_by_id(99999)
