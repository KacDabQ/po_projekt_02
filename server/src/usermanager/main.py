from flask import Flask, jsonify

app = Flask(__name__)

class Person():
    def __init__(self, id:int, firstname:str, lastname:str, age:int, group:str):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.group = group


    def to_json(self):
        return {    
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "age": self.age,
            "group": self.group
        }






users = [Person(1, "John", "Doe", 25, "admin"), Person(2, "Jane", "Doe", 22, "user")]





@app.route("/")
def main_menu():
    return "<h1>Hello world!</h1>", 200

@app.route("/users", methods=['GET'])
def get_all_users():
    return [u.to_json() for u in users], 200

@app.route("/users/<int:id>", methods=['GET'])
def get_all_users_by_id(id):
    filtered_users = []
    for u in users:
        if u.id == id:
            filtered_users.append(u)
    if len(filtered_users) == 0:
        return "User not found", 404
    return [u.to_json() for u in filtered_users], 200

def start():
    app.run(debug=True)
