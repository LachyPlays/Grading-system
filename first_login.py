import os

def run():
    with open('main.txt', "rt") as file:
        text = file.read()

        if text == 'False':
            return  False
        if text == 'True':
            with open('main.txt', 'wt') as file:
                file.write("False")
            return True
        else:
            error("Firstlogin file invalid format")

