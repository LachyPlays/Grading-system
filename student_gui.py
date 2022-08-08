from tkinter import *
import json
from database import student

class student_gui:
    def __init__(self):
        self.ui = Tk()
        self.students = dict
        with open ("students.json") as file:
            self.students = json.loads(file.read())
    

    def open_window(self):
        studentlist = Listbox(self.ui)
        index = int(0)
        for student in list(self.students.keys()):
            studentlist.insert(index,student)
            index = index + 1

        studentlist.pack()
        self.ui.geometry("400x400")
        self.ui.mainloop()