import matplotlib.pyplot as plt
import numpy as np
import json
import tkinter 
from tkinter import * 
from tkinter import messagebox


window = tkinter.Tk()

label = tkinter.Label(window, text="list a students").pack()
entry = tkinter.Entry(window)
def sub():
    text = entry.get()
    user_data = data[text]
    
btn = tkinter.Button(window, text="submit", command=sub()).pack()

entry.pack()






data = dict()
with open('students.json') as file:
    data = json.dumps(file.read())


print(data)





window.mainloop()


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()