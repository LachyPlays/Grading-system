from cryptography.fernet import Fernet
import base64
import json
import tkinter 
from tkinter import * 
import os

class hash_gui():
    def __init__(self):
        self.window = Tk()
        self.button = Button(self.window, text="Submit", command=self.Get_Text)
        self.entry = Entry(self.window, text="Enter a password:")
        self.label = Label(self.window, text="make a new password")

    def Get_Text(self):
        password = self.entry.get()
        t = Fernet(base64.urlsafe_b64encode(str.encode(password.zfill(32))))
        self.enc = t.encrypt(password.encode())
        self.write()
        self.window.destroy()

    def open_window(self):
        self.label.pack()
        self.entry.pack()
        self.button.pack()
        self.window.mainloop()

    def write(self):
        data = dict
        with open('Teacher.json', 'r') as file:
            data = json.loads(file.read())
            
        data["Mr.Hafiz"]["Password"] = (self.enc).decode()

        with open('Teacher.json', 'w') as file:
            file.write(json.dumps(data))

        # self.test()
    
    # def test(self):
    #     with open('Teacher.json') as file:
    #         data = json.loads(file.read())
    #         t = Fernet(base64.urlsafe_b64encode(str.encode(("ABC123").zfill(32))))
    #         print(t.decrypt(data["Mr.Hafiz"]["Password"].encode()))

