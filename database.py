import json
import string
# Load a person from a json file
def load_person(name, dbase):
    # Ensure that the database is a json
    if dbase.split('.')[1] == "json":
        with open(dbase) as file:
            return json.loads(file.read())[name]

class student:
    def __init__(self, name: str):
        jsondata = load_person(name, "students.json")
        self.name = name
        self.age = jsondata["age"]
        self.results = jsondata['results']

    def __call__(self, *,data: dict, name: str):
        self.name = name
        self.age = data["age"]
        self.results = data["results"]

    def to_json(self):
        data = dict()
        data["age"] = int(self.age)
        data["results"] = dict(self.results)
        return data
    