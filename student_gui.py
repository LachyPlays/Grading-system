from ctypes import alignment
from tkinter import *
import json
from database import student

class student_gui:
    def __init__(self):
        self.ui = Tk()
        self.students = dict
        with open ("students.json") as file:
            self.students = json.loads(file.read())

    def update_list(self, evt):
        grade_map = {"F":0, "F+":1, "D-":2, "D":3, "D+":4, "C-":5, "C":6, "C+":7, "B-":8, "B":9, "B+":10, "A-":11, "A":12, "A+":13}
        math_grade = grade_map.get(self.students[self.studentlist.get(self.studentlist.curselection())]["grades"]["math"])

        if math_grade <= 8:
            new_text = " is not elegible for math methods"
        if math_grade > 8 and math_grade < 12:
            new_text = " is elegible for methods, but may struggle"
        if math_grade >= 12:
            new_text = " is recommended for math methods"
            
        self.sortLabel.config(text=self.studentlist.get(self.studentlist.curselection()) + new_text)

    def open_window(self):
        self.studentlist = Listbox(self.ui)
        self.studentData = Label(self.ui, text="No student selected", anchor='s')
        self.sortLabel = Label(self.ui, text="Sort by:", anchor='sw')

        index = int(0)
        for student in list(self.students.keys()):
            self.studentlist.insert(index,student)
            index = index + 1

        students = self.students
        self.studentlist.bind("<<ListboxSelect>>", self.update_list)
        self.studentlist.pack()
        self.studentData.pack()
        self.sortLabel.pack()
        self.ui.geometry("400x400")
        self.ui.mainloop()