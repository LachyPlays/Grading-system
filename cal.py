from cryptography.fernet import Fernet
import base64
import json
import tkinter 
from tkinter import * 
import os


class find():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x500")
        
        self.button = Button(self.window, text="Submit")
        self.entry_ask = Entry(self.window, text="what is the student name")
        self.label = Label(self.window, text="make a new password")
        

    def open_window(self):
        self.label.pack()
        self.entry.pack()
        self.button.pack()
        self.window.mainloop()

Cal = find()
Cal.open_window()