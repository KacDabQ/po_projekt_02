from usermanager.repositories import User, UserRepository


allowed_groups = ["user", "premium", "admin"]

class NonExistingGroup(Exception):
    pass

class UserController():
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create(self, dict) -> User:
        first_name = dict["firstname"]
        last_name = dict["lastname"]
        birth_year = dict["birthyear"]
        group = dict["group"]

        if any(group in x for x in allowed_groups):
            user = User(0, first_name, last_name, birth_year, group)
            self.user_repository.add(user)
            return user

        raise NonExistingGroup