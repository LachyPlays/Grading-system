import json

# Load a person from a json file
def load_person(name, dbase):
    # Ensure that the database is a json
    if dbase.split('.')[1] == "json":
        with open(dbase) as file:
            return json.loads(file.read())[name]

class student:
    def __init__(self, name):
        jsondata = load_person(name, "students.json")
        self.name = name
        self.age = jsondata["age"]
        self.grades = jsondata["grades"]

    def print_data(self):
        print(f"{self.name} is {self.age} years old")
