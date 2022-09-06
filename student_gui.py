from curses import window
from tkinter import *
import json
from tkinter import simpledialog
#from database import student

class student_gui:
    def __init__(self):
        self.ui = Tk()
        self.students = dict
        with open ("students.json") as file:
            self.students = json.loads(file.read())

    def __del__(self):
        with open("students.json", 'wt') as file:
            file.write(json.dumps(self.students))

    def update_listbox(self):
        index = int(0)
        for student in list(self.students.keys()):
            self.studentlist.insert(index,student)
            index = index + 1

    def update_list(self, evt):
        grade_map = {"F":0, "F+":0.5, "D-":1, "D":1.3, "D+":1.3, "C-":1.7, "C":2, "C+":2.3, "B-":2.7, "B":3.0, "B+":3.3, "A-":3.7, "A":4.0, "A+":4.3}
        math_grade = grade_map.get(self.students[self.studentlist.get(self.studentlist.curselection())]["grades"]["math"])

        if math_grade <= 8:
            new_text = " is not elegible for math methods"
        if math_grade > 8 and math_grade < 12:
            new_text = " is elegible for methods, but may struggle"
        if math_grade >= 12:
            new_text = " is recommended for math methods"
            
        self.studentData.config(text=self.studentlist.get(self.studentlist.curselection()) + new_text)

    def addStudent(self):
        newStudentName = simpledialog.askstring(title="Add new student",
                                  prompt="What is their name?:")
        # self.students[newStudentName] = {"age":0, "grades":{"math":"C"}}
        self.students = {"Name": newStudentName, "age": 0,"grades":{"math":"C"}}
        self.studentlist.insert(self.studentlist.size(), newStudentName)

    def delStudent(self):
        if self.studentlist.curselection != "":
            del self.students[self.studentlist.get(self.studentlist.curselection())]
            self.studentlist.delete(self.studentlist.curselection())
            self.update_listbox()

            #self.studentData.config(text="No students selected")
    def add_grade():
        pass
    def open_window(self):
        self.studentlist = Listbox(self.ui)
        self.studentData = Label(self.ui, text="No student selected")
        self.addStudentBtn = Button(self.ui, text='Add student', command=self.addStudent)
        self.nameBox = Entry(self.ui)
        self.button_del = Button(self.ui, text='Remove students', command=self.delStudent)

        self.update_listbox()

        students = self.students
        self.studentlist.bind("<<ListboxSelect>>", self.update_list)
        self.studentlist.pack(side=LEFT, anchor=NW)
        self.studentData.place(x=10, y=180)
        self.addStudentBtn.place(x=10, y=200)
        self.nameBox.pack(side=RIGHT, anchor=NE)
        self.button_del.place(x=10, y=250)
        self.ui.geometry("400x400")
        self.ui.mainloop()