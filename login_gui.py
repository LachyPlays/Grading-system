from cProfile import label
from curses import window
import tkinter
from tkinter import *

class login_gui:
    def __init__(self):
        self.window = Tk()
        self.Label = Label(self.window, text="what is your username")
        self.Label.pack()
        self.Entry = Entry(self.window)
        self.Entry.pack()
        def Get_username():
            username = self.Entry.get()
            print(username)
            self.Label.config(text="what is your passsowrd")
            self.btn.config(command=Get_password)
        self.btn = Button(self.window, text='Submit', command=Get_username)
        self.btn.pack()
        def Get_password():
            pass
        self.window.mainloop()

p1 = login_gui()
