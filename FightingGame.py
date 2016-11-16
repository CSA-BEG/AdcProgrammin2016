from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
'''-----------------------------------------------------------------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
-----------------------------------------------------------------------'''

global lhealth
global rhealth
global temphealth2
global temphealth
rhealth=30
lhealth=30

root = Tk()
root.title('The Presidential Debate')

def about():#the about message box
    messagebox.showinfo(title="Version", message="FightingGame.py version .1")

def fight():
    x=int(random.randrange(0,3))
    rfighters.selection_clear(0,2)
    global temphealth2
    global temphealth
    try:
        temphealth.grid_remove()
    except:
        pass
    try:
        temphealth2.grid_remove()
    except:
        pass
    global lhealth
    global rhealth
    rfighters.selection_set(x)
    lfight=lstats[lfighters.curselection()[0]]
    rfight=rstats[rfighters.curselection()[0]]
    if lfight[0]>rfight[1]:
        rhealth-=lfight[0]
    if rfight[0]>lfight[1]:
        lhealth-=rfight[0]
    if lhealth<=0:
        messagebox.showinfo(title="Victor", message="Hillary Wins!")
        root.quit()
    if rhealth<=0:
        messagebox.showinfo(title="Victor", message="Trump Wins!")
        root.quit()
    temphealth=ttk.Label(root, text='Health - ' + str(lhealth)).grid(column=0, row=0, sticky=W)
    temphealth2=ttk.Label(root, text='Health - ' + str(rhealth)).grid(column=2, row=0, sticky=W)

def llabels(e):
    ttk.Label(root, text=lstats[lfighters.curselection()[0]]).grid(column=0, row=7, sticky=W)

def rlabels(e):
    ttk.Label(root, text=rstats[rfighters.curselection()[0]]).grid(column=2, row=7, sticky=W)

TopMenu = Menu(root)#creating toolbar
root.config(menu=TopMenu)
root.option_add('*tearOff',False)
SubMenu = Menu(TopMenu)#creating file section of toolbar
TopMenu.add_cascade(label='File', menu=SubMenu)
SubMenu.add_command(label='Exit', command=root.quit)
HelpMenu=Menu(TopMenu)#creating help section of toolbar
TopMenu.add_cascade(label='Help', menu=HelpMenu)
HelpMenu.add_command(label='About', command=about)

ttk.Label(root,text='Trump').grid(column=0,row=1,sticky=W)
ttk.Label(root,text='Hillary').grid(column=2,row=1,sticky=W)

fightersl=["WRONG",'Small Loan of a Million Dollars','Build the Wall']
lstats=[[2,2],[2,1],[3,1]]
fightl=StringVar(value=fightersl)
lfighters=Listbox(root,height=3,listvariable=fightl,exportselection=False,width=28)
lfighters.grid(column=0,row=2,sticky=W,padx=5,pady=5,rowspan=5)

fightersr=["Chillin' in Cedar Rapids",'Pokemon Go to the Polls','DELETE']
rstats=[[2,2],[3,1],[2,1]]
fightr=StringVar(value=fightersr)
rfighters=Listbox(root,height=3,listvariable=fightr,exportselection=False,width=23)
rfighters.grid(column=2,row=2,sticky=W,padx=5,pady=5,rowspan=5)

lfighters.bind('<<ListboxSelect>>', llabels)
rfighters.bind('<<ListboxSelect>>', rlabels)

ttk.Label(root,text='Wins').grid(column=1,row=3,sticky=W)
ttk.Label(root,text='Losses').grid(column=1,row=5,sticky=W)
ttk.Label(root,text='--').grid(column=1,row=2,sticky=W)
ttk.Label(root,text='--').grid(column=1,row=4,sticky=W)
ttk.Label(root,text='Stats').grid(column=0,row=6,sticky=W)
ttk.Label(root,text='Stats').grid(column=2,row=6,sticky=W)
ttk.Label(root,text='--').grid(column=0,row=7,sticky=W)
ttk.Label(root,text='--').grid(column=2,row=7,sticky=W)

temphealth=ttk.Label(root,text='Health - 30')
temphealth.grid(column=0,row=0,sticky=W)
temphealth2=ttk.Label(root,text='Health - 30')
temphealth2.grid(column=2,row=0,sticky=W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=10)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=10)
root.columnconfigure(2, weight=1)
root.rowconfigure(2, weight=10)
root.rowconfigure(3, weight=10)
root.rowconfigure(4, weight=10)
root.rowconfigure(5, weight=10)
root.rowconfigure(6, weight=10)
root.rowconfigure(7, weight=10)

ttk.Button(root,text='Fight',command=fight).grid(column=1,row=7)

root.mainloop()
