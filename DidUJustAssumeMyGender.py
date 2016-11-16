#Why'd you block all the skeletor laugh youtube vids man? Its just not right.
#Trey Grant 8/31/16
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Login")

def delete(*args):
    name.delete(0,'end')
def delete1(*args):
    age.delete(0,'end')
def clearscreen(*args):
    name.delete(0,'end')
    name.insert(0,'Name')
    age.delete(0,'end')
    age.insert(0,'Age')
    gender.set(0)

mainframe = ttk.Frame(root, padding="6 6 6 6")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)

nam=StringVar()
name=ttk.Entry(mainframe,textvariable=nam,width=12)
name.grid(column=0, row=0, sticky=(N, W, E, S))
name.insert(0,'Name')
ag=StringVar()
age=ttk.Entry(mainframe,textvariable=ag,width=12)
age.grid(column=0, row=1, sticky=(N, W, E, S))
age.insert(0,'Age')
gender=StringVar()
male=ttk.Radiobutton(mainframe, text='Male', variable=gender,value=1)
male.grid(column=0,row=2,sticky=W)
female=ttk.Radiobutton(mainframe, text='Female', variable=gender,value=2)
female.grid(column=1,row=2,sticky=W)
other=ttk.Radiobutton(mainframe, text='Other', variable=gender,value=3)
other.grid(column=2,row=2,sticky=W)
clear=ttk.Button(mainframe,text='Subtim',command=clearscreen)
clear.grid(column=2,row=3,sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#root.bind('<Return>', calculate)
name.bind("<Button-1>", delete)
age.bind("<Button-1>", delete1)
root.mainloop()
