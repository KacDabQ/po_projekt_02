from datetime import datetime


year = datetime.now().year

class Person():
    def __init__(self, id:int, firstname:str, lastname:str, birthyear:int, group:str):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.group = group


    def to_json(self):
        return {    
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "age": year - self.birthyear,
            "group": self.group
        }


class PersonRepository():
    def __init__(self):
        self.storage = []

    def get_all(self):
        pass

    def get_by_id(self, id: int):
        for u in self.storage:
            if u.id == id:
                return u

        return None

    def add(self, person: Person):
        max_id = 0
        for u in self.storage:
            if u.id > max_id:
                max_id = u.id
        person.id = max_id + 1
        self.storage.append(person);

    def delete_by_id(self, id: int):
        pass
