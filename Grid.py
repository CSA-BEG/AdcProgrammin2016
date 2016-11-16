#Trey Grant 10/7/16
from tkinter import *
from tkinter import ttk

def login():
    user.set('')
    pasw.set('')

root=Tk()

topmenu=Menu(root)
root.title("Login")
root.config(menu=topmenu)

mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)

submenu=Menu(topmenu)
topmenu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='exit',command=root.quit)

user=StringVar()
pasw=StringVar()

usern=ttk.Entry(mainframe, width=12, textvariable=user)
usern.grid(column=1, row=0, sticky=W)
passw=ttk.Entry(mainframe, width=12, textvariable=pasw)
passw.grid(column=1, row=1, sticky=W)
login=ttk.Button(mainframe, text="Login", command=login,width=25)
login.grid(column=1,row=3,sticky=W,columnspan=2)
ttk.Label(mainframe,text='Username').grid(column=0,row=0,sticky=(W,N))
ttk.Label(mainframe,text='Password').grid(column=0,row=1,sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

usern.focus()
root.bind('<Return>', login)
root.mainloop()
