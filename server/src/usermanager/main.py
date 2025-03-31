from flask import Flask, request
from datetime import datetime



app = Flask(__name__)


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



allowed_groups = ["user", "premium", "admin"]


users = [Person(1, "John", "Doe", 1995, "admin"), Person(2, "Jane", "Doe", 1976, "user")]


@app.route("/")
def main_menu():
    return "<h1>Hello world!</h1>", 200

@app.route("/users", methods=['GET'])
def get_all_users():
    return [u.to_json() for u in users], 200



@app.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    filtered_users = []
    for u in users:
        if u.id == id:
            filtered_users.append(u)
    if len(filtered_users) == 0:
        return "User not found", 404
    if len(filtered_users) > 1:
        return "Multiple users found", 500
    return filtered_users[0].to_json(), 200



@app.route("/users", methods=["POST"])
def create_user():
    first_name = request.json.get("firstname")
    last_name = request.json.get("lastname")
    birth_year = request.json.get("birthyear")
    group = request.json.get("group")

    if any(group in x for x in allowed_groups):

        max_id = 0
        for u in users:
            if u.id > max_id:
                max_id = u.id

        new_id = max_id + 1
        person = Person(new_id, first_name, last_name, birth_year, group)
        users.append(person)
        return {"id": new_id}, 200
    
    else:
        return "Non-existant group passed", 400


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user_by_id(id):
    to_delete = -1
    for i, u in enumerate(users):
        if u.id == id:
            to_delete = i

    if to_delete > -1:
        users.pop(to_delete)
        return "Succesfully deleted person", 200
    
    return "User not found", 404



def start():
    app.run(debug=True)
