from ast import Delete
import json
from queue import Empty
import tkinter
from tkinter import *

class login_gui:
    def __init__(self):
        self.window = Tk()
        self.login = False
        with open ("Teacher.json") as file:
            self.tdata = json.loads(file.read())

    def open_window(self):
        self.Label = Label(self.window, text="what is your username")
        self.Label.pack()
        self.Entry = Entry(self.window)
        self.Entry.pack()
        self.btn = Button(self.window, text='Submit', command=self.Get_username)
        self.btn.pack()
        self.window.mainloop()

    def Get_username(self):
            self.username = self.Entry.get()
            print(self.username)
            self.Entry.delete(0, END)
            self.Label.config(text="what is your passsowrd")
            self.btn.config(command=self.Get_password)
    
    def Get_password(self):
            password = self.Entry.get()
            if self.tdata[self.username]["Password"] == password:
                self.window.destroy()
                self.login = True
            delattr(self, "username")

