import tkinter
from tkinter import *

class login_gui:
    def __init__(self):
        self.window = Tk()

    def open_window(self):
        self.Label = Label(self.window, text="what is your username")
        self.Label.pack()
        self.Entry = Entry(self.window)
        self.Entry.pack()
        self.btn = Button(self.window, text='Submit', command=self.Get_username)
        self.btn.pack()
        self.window.mainloop()

    def Get_username(self):
            username = self.Entry.get()
            print(username)
            self.Label.config(text="what is your passsowrd")
            self.btn.config(command=self.Get_password)
    
    def Get_password(self):
            password = self.Entry.get()
            self.window.destroy()
            login = True

