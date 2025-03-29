from flask import Flask

app = Flask(__name__)

class Person():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def to_json(self):
        return {    
            "name": self.name,
            "age": self.age
        }

    '''{ "id": 4, "name": "Wojciech", "lastname": "Oczkowski" },
    { "id": 3, "name": "Jan", "lastname": "Kowalski" },
    { "id": 2, "name": "Adam", "lastname": "Nowak" },
    { "id": 1, "name": "Marta", "lastname": "Nowakowska"}'''





users = [Person("Kacper", 16), Person("Kamil", 14), Person("Kendrick", 20)]





@app.route("/")
def main_menu():
    return "<h1>Hello world!</h1>"

@app.route("/users", methods=['GET'])
def get_all_users():
    return [u.to_json() for u in users]

@app.route("/test/<username>/<int:age>")
def test(username, age):
    users = [Person(username, age)] * 10
    return [u.to_json() for u in users]

def start():
    app.run(debug=True)
