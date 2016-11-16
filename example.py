from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#-----------------------------------------------------------------
'''This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.'''
#-----------------------------------------------------------------------

root = Tk()
root.title('Example')

def about():#the about message box
    messagebox.showinfo(title="Version", message="example.py version .1")

def writeFile(*args):#prepares values, writes the values to a file, and finally clears the screen
    file=open('ExampleFile.csv','a')
    tempstring=name.get(),onevar.get(),twovar.get(),threevar.get()
    tempstring=str(tempstring)
    tempstring=tempstring.replace("'",'')
    tempstring=tempstring.replace("(",'')
    tempstring=tempstring.replace(")",'')
    tempstring = tempstring+'\n'
    file.write(tempstring)
    onevar.set(False)
    twovar.set(False)
    threevar.set(False)
    namevar.set('')
    file.close()

def cancelFunc():#clears the screen
    onevar.set(False)
    twovar.set(False)
    threevar.set(False)
    namevar.set('')

TopMenu = Menu(root)#creating toolbar
root.config(menu=TopMenu)
root.option_add('*tearOff',False)
SubMenu = Menu(TopMenu)#creating file section of toolbar
TopMenu.add_cascade(label='File', menu=SubMenu)
SubMenu.add_command(label='Exit', command=root.quit)
HelpMenu=Menu(TopMenu)#creating help section of toolbar
TopMenu.add_cascade(label='Help', menu=HelpMenu)
HelpMenu.add_command(label='About', command=about)

content = ttk.Frame(root, padding=(3, 3, 12, 12))#general setup
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)

namevar=StringVar()#name box
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content,textvariable=namevar)

onevar = BooleanVar()#variable setup
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(False)#variable setup
twovar.set(False)
threevar.set(False)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)#checkboxes
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay", command=writeFile)#buttons
cancel = ttk.Button(content, text="Cancel", command=cancelFunc)

content.grid(column=0, row=0, sticky=(N, S, E, W))#grid setup from here on
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()
