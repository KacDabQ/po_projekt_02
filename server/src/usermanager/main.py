from flask import Flask, request
from usermanager.repositories import User, UserNotFound, UserRepository

app = Flask(__name__)
user_repository = UserRepository()

allowed_groups = ["user", "premium", "admin"]

@app.route("/")
def main_menu():
    return "<h1>Hello world!</h1>", 200

@app.route("/users", methods=['GET'])
def get_all_users():
    return [p.to_json() for p in user_repository.get_all()], 200


@app.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    user = user_repository.get_by_id(id)
    if user is None:
        return "User not found", 404

    return user.to_json(), 200



@app.route("/users", methods=["POST"])
def create_user():
    first_name = request.json.get("firstname")
    last_name = request.json.get("lastname")
    birth_year = request.json.get("birthyear")
    group = request.json.get("group")

    if any(group in x for x in allowed_groups):
        user = User(0, first_name, last_name, birth_year, group)
        user_repository.add(user)
        return {"id": user.id}, 200
    
    else:
        return "Non-existant group passed", 400


@app.route("/users", methods=["PATCH"])
def update_user(id):
    pass


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user_by_id(id):
    try:
        user_repository.delete_by_id(id)
        return "Succesfully deleted person", 200
    except UserNotFound:
        return "User not found", 404


def start():
    app.run(debug=True)
