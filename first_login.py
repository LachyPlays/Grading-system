from logging import error
import os
import make_hash

def run():
    with open('main.txt', "r") as file:
        text = file.read()
        if text == 'False':
            return  False
        if text == 'True':
            hgui = make_hash.hash_gui()
            hgui.open_window()
            with open('main.txt', 'w') as file:
                file.write("False")
            return True
        else:
            error("Firstlogin file invalid format")

