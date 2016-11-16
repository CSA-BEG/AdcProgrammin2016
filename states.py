#Trey Grant 9/19/16
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("States & names")

mainframe = ttk.Frame(root, padding="6 6 6 6")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)#general tkinter setup til now

def gen(*args):#just some good 'ol greeting functions
    namE=name.get()
    statE=state.get()
    greeting=('Hello '+namE+' from '+statE+'!')#simply creates the label
    ttk.Label(mainframe,text=greeting).grid(column=2,row=1,sticky=W)
nam=StringVar()
name=ttk.Entry(mainframe,textvariable=nam,width=10)#name entry box
name.grid(column=1,row=1,sticky=W)
stat=StringVar()
state=ttk.Combobox(mainframe,textvariable=stat,width=10,values=('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachussetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvannia', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'))
state.grid(column=2,row=3,sticky=W)#state entry box
state.state(['readonly'])
state.bind('<<ComboboxSelected>>', gen)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)#general tkinter setup after this

name.focus()

root.mainloop()
