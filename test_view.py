from curses.ascii import isdigit
from operator import contains
from tkinter import *
from tkinter import ttk
from turtle import right
from database import student
from tkinter import simpledialog

class test_gui():
    def __init__(self, student: student):
        self.ui = Tk()
        self.student = student
        self.updatedStudent = student
    
    def update_table(self):
        for row in self.gradeTable.get_children():
            self.gradeTable.delete(row)

        for (test_no, grade) in self.student.results.items():
            self.gradeTable.insert(parent='',index='end',iid=int(test_no),text='',
                values=(test_no,(str(float(grade * 100)) + "%")))

    
    def __isPercentage(self, val:str):
        if(len(val) == 3):
            if(val[0].isdigit() and val[1].isdigit() and (val[2] == "%")):
                return True
            else: 
                return False
        else:
            return False

    def __isFraction(self, val:str):
        try:
            (a, b) = val.split('/')
            res = float(int(a) / int(b))
            if(res >= 0.0 and res <= 1.0):
                return True
        except:
            return False

    def addTest(self):
        testGrade = simpledialog.askstring("New test", "Enter new test result(%, 0.0-1.0, 0-100, c/t")
        newResult = float()
        chars = list()

        for char in testGrade:
            chars.append(char)
        
        if len(chars) <= 5:
            if(self.__isFraction(testGrade)):
                newResult = float(int(testGrade.split('/')[0]) / int(testGrade.split('/')[1]))
            elif(self.__isPercentage(testGrade)):
                newResult = float(chars[0] + chars[1]) / 100
            elif(float(testGrade) <= 1.0 and float(testGrade) >= 0.0 and len(chars) >= 3):
                newResult = float(testGrade)
            elif(int(testGrade) >= 0 and int(testGrade) <= 100 and len(chars) == 2):
                newResult = float(testGrade) / 100
        else:
            self.addTest()
            pass

        self.student.results[str(len(self.student.results))] = newResult
        self.update_table()

    def applyChanges(self):
        self.updatedStudent = self.student
        self.ui.destroy()
        self.ui.quit()

    def open_window(self):
        self.ui.geometry("400x300")

        self.gradeTable = ttk.Treeview(self.ui)
        self.gradeTable['columns'] = ('test_number', "grade")
        self.gradeTable.column("#0", width=0,  stretch=NO)
        self.gradeTable.column("test_number",anchor=CENTER, width=80)
        self.gradeTable.column("grade",anchor=CENTER, width=80)
        self.gradeTable.heading("#0",text="",anchor=CENTER)
        self.gradeTable.heading("test_number",text="Test Number",anchor=CENTER)
        self.gradeTable.heading("grade",text="Grade(%)",anchor=CENTER)

        self.addTestBtn = Button(self.ui, text="Add a test", command=self.addTest)
        self.applyBtn = Button(self.ui, text="Apply changes", command=self.applyChanges)

        self.update_table()

        self.gradeTable.pack(side=LEFT, anchor=NW)
        self.addTestBtn.pack(side=RIGHT, anchor=NE)
        self.applyBtn.pack(side=BOTTOM, anchor=SE)
        self.ui.mainloop()