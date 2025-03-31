from usermanager.repositories import Person, PersonRepository


def test_create_person():
    repository = PersonRepository()
    person = Person(0, "John", "Doe", 1995, "admin")

    repository.add(person)

    person = repository.get_by_id(person.id)
    assert person is not None
    assert person.id > 0



