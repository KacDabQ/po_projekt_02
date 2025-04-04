from datetime import datetime


year = datetime.now().year

class User():
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

class UserNotFound(Exception):
    pass

class UserRepository():
    def __init__(self):
        self.storage = []

    def get_all(self):
        return self.storage

    def get_by_id(self, id: int):
        for u in self.storage:
            if u.id == id:
                return u

        return None

    def add(self, user: User):
        max_id = 0
        for u in self.storage:
            if u.id > max_id:
                max_id = u.id
        user.id = max_id + 1
        self.storage.append(user);

    def delete_by_id(self, id: int):
        to_delete = -1
        for i, u in enumerate(self.storage):
            if u.id == id:
                to_delete = i

        if to_delete > -1:
            self.storage.pop(to_delete)
            return
        
        raise UserNotFound
