from tkinter import *

def donothing():
    print('nogobro')

root=Tk()

topmenu=Menu(root)
root.config(menu=topmenu)

submenu=Menu(topmenu)
topmenu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='new project...',command=donothing)
submenu.add_command(label='new',command=donothing)
submenu.add_separator()
submenu.add_command(label='exit',command=root.quit)

editmenu=Menu(topmenu)
topmenu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='redo',command=donothing)

root.mainloop()