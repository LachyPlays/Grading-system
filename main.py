from student_gui import student_gui
from login_gui import *

lgui = login_gui()
lgui.open_window()

if lgui.login == True:
    sgui = student_gui()
    sgui.open_window()



