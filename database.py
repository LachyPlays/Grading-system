import json
import string

# Load a person from a json file
def load_person(name, dbase):
    # Ensure that the database is a json
    if dbase.split('.')[1] == "json":
        with open(dbase) as file:
            return json.loads(file.read())[name]

class student:
    def __init__(self, name: string):
        jsondata = load_person(name, "students.json")
        self.name = name
        self.age = jsondata["age"]
        self.grades = jsondata["grades"]

    def __init__(self, data: dict):
        self.name = data["name"]
        self.age = data["age"]
        self.grades = data["grades"]

    def to_json(self):
        data = dict
        data["name"] = self.name
        data["age"] = self.age
        data["grades"] = self.grades
        return data