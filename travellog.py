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
root.title('Travel Log')

def about():#the about message box
    messagebox.showinfo(title="Version", message="travellog.py version .1\nA program to log destinations events during travel.")

def progress1(e):
    p["value"]=33
    progress2()

def progress2():
    if t.compare("end-1c", "!=", "1.0"):
        p["value"]=66

def progress3():
    p["value"]=100

def clearall():
    country.selection_clear(0,END)
    t.delete('1.0', END)

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

countryl=['China','India','Indonesia','Brazil','Pakistan','Nigeria','Bangladesh','Russia','Mexico','Japan','Philippines','Ethiopia','Vietnam','Egypt','Germany','Iran','Turkey','Thailand','United Kingdom','France']
country=Listbox(root,height=5,listvariable=StringVar(value=countryl),exportselection=False,width=28)
country.grid(column=0,row=0,sticky=W,padx=5,pady=5)

t=Text(root,width=21,height=6)
t.grid(column=0,row=1,sticky=W,padx=5,pady=5)

s=ttk.Scrollbar(root,orient=VERTICAL,command=country.yview)
country.configure(yscrollcommand=s.set)
s.grid(column=1,row=0,sticky=(N,S))

p=ttk.Progressbar(root,orient=VERTICAL,length=200,mode='determinate')
p.grid(column=6,row=0,rowspan=2)

butto=ttk.Button(root,text='Submit',command=progress3)
butto.grid(column=2,row=0,sticky=W,padx=5,pady=5)

buto=ttk.Button(root,text='Clear',command=clearall)
buto.grid(column=2,row=1,sticky=W,padx=5,pady=5)

country.bind('<<ListboxSelect>>', progress1)

progress2()

root.mainloop()