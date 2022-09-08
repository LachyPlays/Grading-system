from decimal import DivisionByZero
from tkinter import *
import json
from tkinter import simpledialog
import tkinter
from typing import *
from test_view import test_gui
from database import student

class student_gui:
    def __init__(self):
        self.ui = Tk()
        self.students = dict
        with open ("students.json") as file:
            self.students = json.loads(file.read())

    def updateJson(self):
        with open("students.json", 'wt') as file:
            file.write(json.dumps(self.students))

    def update_listbox(self):
        self.studentlist.delete(0, END)
        index = int(0)
        for student in list(self.students.keys()):
            self.studentlist.insert(index,student)
            index = index + 1

    def updateInfo(self, student_name, avg_grade, last_result):
        avg_grade = str(int(avg_grade * 100)) + "%"
        last_result = str(int(last_result * 100)) + "%"
        self.nameBox.delete(0, END)
        self.avgGradeBox.delete(0, END)
        self.lastTestResBox.delete(0, END)
        self.nameBox.insert(0, student_name)
        self.avgGradeBox.insert(0, avg_grade)
        self.lastTestResBox.insert(0, last_result)

    def update_list(self, evt):
        results = self.students[self.studentlist.get(self.studentlist.curselection())]["results"]
        
        avg_grade = float()
        for (test, grade) in results.items():
            avg_grade += float(grade)
        try:
            avg_grade = float(avg_grade / len(results))
            math_grade = avg_grade
        except:
            math_grade = 0

        if math_grade <= 0.7:
            new_text = " is not elegible for methods"
        if math_grade > 0.7 and math_grade < 0.8:
            new_text = " is elegible for methods"
        if math_grade >= 0.8:
            new_text = " is recommended for methods"
            
        self.studentData.config(text=self.studentlist.get(self.studentlist.curselection()) + new_text)
        try:
            self.updateInfo(self.studentlist.get(self.studentlist.curselection()), avg_grade, results[str(len(results) - 1)])
        except:
            self.updateInfo(self.studentlist.get(self.studentlist.curselection()), 0.0, 0.0)

    def addStudent(self):
        newStudentName = simpledialog.askstring(title="Add new student",
                                  prompt="What is their name?:")
        self.students[newStudentName] = {"age":0, "results":{}}
        self.studentlist.insert(self.studentlist.size(), newStudentName)
        self.updateJson()

    def delStudent(self):
        try:
            del self.students[self.studentlist.get(self.studentlist.curselection())]
        except:
            pass
        self.update_listbox()
        self.updateInfo("", 0.0, 0.0)
        self.studentData.config(text='No student selected')
        self.updateJson()

    def viewTests(self):
        try:
            currentStudent = student(self.studentlist.get(self.studentlist.curselection()))
        except:
            pass
        tGui = test_gui(currentStudent)
        tGui.open_window()
        self.students[self.studentlist.get(self.studentlist.curselection())]["results"] = tGui.updatedStudent.to_json()["results"]
        self.update_list(None)
        self.updateJson()

    def open_window(self):
        self.studentlist = Listbox(self.ui)
        self.studentData = Label(self.ui, text="No student selected")
        self.addStudentBtn = Button(self.ui, text='Add student', command=self.addStudent)
        self.delStudentBtn = Button(self.ui, text='Remove students', command=self.delStudent)

        self.update_listbox()
        self.nameVar = StringVar()
        self.avgVar = StringVar()
        self.lastVar = StringVar()
        self.nameBox = Entry(self.ui, width=8)
        self.nameBoxLabel = Label(self.ui, text="Name")
        self.avgGradeBox = Entry(self.ui, width=8)
        self.avgGradeBoxLabel = Label(self.ui, text="Average grade")
        self.lastTestResBox = Entry(self.ui, width=8)
        self.lastTestResLabel = Label(self.ui, text="Previous test results")
        self.viewTestBtn = Button(self.ui, text="View tests", command=self.viewTests)

        self.studentlist.bind("<<ListboxSelect>>", self.update_list)
        self.nameBox.bind("<Key>", lambda e: "break")
        self.avgGradeBox.bind("<Key>", lambda e: "break")
        self.lastTestResBox.bind("<Key>", lambda e: "break")

        # Placing all widgets
        self.studentlist.grid(row=0, column=0, columnspan=2, rowspan=6)
        self.studentData.grid(row=6, column=0, columnspan=2)
        self.addStudentBtn.grid(row=7, column=0, columnspan=2)
        self.delStudentBtn.grid(row=8, column=0, columnspan=2)
        self.viewTestBtn.grid(row=3, column=5, columnspan=6, rowspan=1)

        self.nameBox.grid(row=0, column=5, columnspan=6, rowspan=1)
        self.avgGradeBox.grid(row=1, column=5, columnspan=6, rowspan=1)
        self.lastTestResBox.grid(row=2, column=5, columnspan=6, rowspan=1)
        self.nameBoxLabel.grid(row=0, column=3, rowspan=1, columnspan=1)
        self.avgGradeBoxLabel.grid(row=1, column=3, rowspan=1, columnspan=1)
        self.lastTestResLabel.grid(row=2, column=3, rowspan=1, columnspan=1)

        self.ui.geometry("500x300")
        self.ui.mainloop()