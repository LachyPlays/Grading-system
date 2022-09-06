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
        self.label = Label(self.window, "what is the student first exam score")
        self.exam1_entry = Entry(self.window, text="Exam 1")
        self.exam2_entry = Entry(self.window, text="Exam 2")
        

    def open_window(self):
        self.exam2_entry.pack()
        self.exam1_entry.pack()
        self.window.mainloop()

Cal = find()
Cal.open_window()