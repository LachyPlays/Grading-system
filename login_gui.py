import json
import base64
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet

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
            in_password = self.Entry.get()
            key = Fernet(base64.urlsafe_b64encode(str.encode(in_password.zfill(32))))
            dec_password = str

            try:
                dec_password = key.decrypt(self.tdata[self.username]["Password"].encode()).decode()
            except:
                self.window.destroy()
                messagebox.showerror("Login error", "Invalid username and or password")

            try:
                if dec_password == in_password:
                    self.window.destroy()
                    self.login = True
                else:
                    self.window.destroy()
                    messagebox.showerror("Login error", "Invalid username and or password")
            except:
                self.window.destroy()
                messagebox.showerror("Login error", "Invalid username and or password")

            delattr(self, "username")

