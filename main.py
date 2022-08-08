from ast import Try
from operator import imod
from student_gui import student_gui
from login_gui import *

lgui = login_gui()
lgui.open_window()

if login_gui.login == True:
    sgui = student_gui()
    sgui.open_window()


