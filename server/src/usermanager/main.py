from flask import Flask, request
from usermanager.controllers import NonExistingGroup, UserController
from usermanager.repositories import User, UserNotFound, UserRepository

app = Flask(__name__)
user_repository = UserRepository()


@app.route("/")
def main_menu():
    return "<h1>Hello world!</h1>", 200

@app.route("/users", methods=['GET'])
def get_all_users():
    controller = UserController(user_repository)
    return [p.to_json() for p in controller.get_all()], 200


@app.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    controller = UserController(user_repository)
    user = controller.get(id)
    if user is None:
        return "User not found", 404

    return user.to_json(), 200


@app.route("/users", methods=["POST"])
def create_user():
    controller = UserController(user_repository)
    try:
        created_user = controller.create(request.json)
        return {"id": created_user.id}, 200
    except NonExistingGroup:
        return "Non-existant group passed", 400


@app.route("/users/<int:id>", methods=["PATCH"])
def update_user(id):
    controller = UserController(user_repository)
    try:
        controller.update(id, request.json)
        return "User updated", 200
    except UserNotFound:
        return "There is no such user", 404
    except NonExistingGroup:
        return "Non-existant group passed", 400



@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user_by_id(id):
    controller = UserController(user_repository)
    try:
        controller.delete(id)
        return "Succesfully deleted person", 200
    except UserNotFound:
        return "User not found", 404


def start():
    app.run(debug=True)
