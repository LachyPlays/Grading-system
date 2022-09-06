from tkinter import *
import json


window = Tk()

def get_content():
    with open('students.json') as file:
        students_dict = json.loads(file.read())
        if entry.get() == students_dict['Name']:
            print(students_dict['grades'])
            students_grades = students_dict['grades']
            student_grade_letter = students_grades['math']
            if student_grade_letter == 'C':
                student_grade_num = f"{90}%"
                print(student_grade_num)
            
        

    


entry = Entry(window, width= 40)
entry.pack(pady= 20)


button= Button(window, text= "Get Content", command= get_content)
button.pack(pady=10)

window.mainloop()