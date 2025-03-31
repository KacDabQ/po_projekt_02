from usermanager.repositories import User, UserNotFound, UserRepository


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

    def update(self, id, dict) -> None:
        user = self.user_repository.get_by_id(id)
        if user is None:
            raise UserNotFound

        if "group" in dict and any(dict["group"] in x for x in allowed_groups) == False:
            raise NonExistingGroup

        if "firstname" in dict:
            user.firstname = dict["firstname"]

        if "lastname" in dict:
            user.lastname = dict["lastname"]

        if "birthyear" in dict:
            user.birthyear = dict["birthyear"]

        if "group" in dict:
            user.group = dict["group"]