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
root.title('Purchase Order')#general setup
def about():#the about message box
    messagebox.showinfo(title="Version", message="Purchase Order.py version .2\nA program to log purchases.")

def instr():
    messagebox.showinfo(title="Instructiosn", message="Fill out each area, then press submit.\n(Street 2 is optional)\nTo retrieve previous entry, type in the PO\nnumber then press retrieve.")
def calc(x):
    ttk.Label(root, text=('Tax', ((int(pricevar.get()) * 825) / 10000))).grid(column=4, row=1, sticky=W, padx=5, pady=3)
    finalship = int(shipprice[shipping.curselection()[0]])
    ttk.Label(root, text=('Total', (int(pricevar.get()) + finalship + ((int(pricevar.get()) * 825) / 10000)))).grid(column=4, row=3, sticky=W, padx=5, pady=3)

def submit(*args):#oh boy, the thing that writes stuff to the file (this fella was quite the pain, I assure you) basically just grabs each and every variable and writes them down, also prints out totals and tax
    try:
        infostring=''
        infostring+=povar.get()
        infostring+=','
        infostring+=firstvar.get()
        infostring+=','
        infostring+=lastvar.get()
        infostring+=','
        infostring+=streetvar.get()
        infostring+=','
        if street1var.get()!='':
            infostring+='<>'+(street1var.get())
            infostring+=','
        else:
           pass
        infostring+=statevar.get()
        infostring+=','
        infostring+=cityvar.get()
        infostring+=','
        infostring+=zipvar.get()
        infostring+=','
        infostring+=description.get(1.0,END)[:-1]
        infostring+=','
        infostring+=str(int(pricevar.get())+((int(pricevar.get())*825)/10000))
        infostring+=','
        infostring+=str(dayvar.get())
        infostring+=','
        infostring+=str(monthvar.get())
        infostring+=','
        infostring+=str(yearvar.get())
        infostring+=','
        infostring+=str(shipping.curselection()[0])
        if povar.get()=='' or int(len(povar.get()))!=9 or len(zipvar.get())!=5 or firstvar.get()=='' or lastvar.get()=='' or streetvar.get()=='' or statevar.get()=='' or cityvar.get()=='' or str(zipvar.get())=='' or str(pricevar.get())=='' or description.get(1.0,END)[:-1]=='':
            messagebox.showinfo(title="Error", message="Please check your entries.")
        else:
            file=open('orders.txt','r')
            line = file.readline()
            y=0
            while line:
                if line[0] == povar.get():
                    y=1
                    messagebox.showinfo(title="Error", message="Please check your entries.")
            if y!=1:
                infostring += '\n'
                file.close()
                file = open('orders.txt', 'a')
                file.write(infostring)
                file.close()
            else:
                file.close()
    except:
        print('yodawg')
        messagebox.showinfo(title="Error", message="Please check your entries.")
def retrieve(*args):#retrieves values based on the given number
    x=0
    file=open('orders.txt','r')
    line=file.readline()
    while line:
        line=line.split(',')
        if line[0]==povar.get():
            x=1
            firstvar.set(line[1])
            lastvar.set(line[2])
            streetvar.set(line[3])
            if '<>' in line[4]:
                street1var.set(str(line[4])[2:])
                statevar.set(line[5])
                cityvar.set(line[6])
                zipvar.set(line[7])
                description.delete(1.0,END)
                description.insert(1.0,line[8])
                pricevar.set(line[9])
                dayvar.set(int(line[10]))
                monthvar.set(int(line[11]))
                yearvar.set(int(line[12]))
                shipping.selection_set(int(line[13]))
                ttk.Label(root, text=('Tax',((float(line[9])*825)/10000))).grid(column=4, row=1, sticky=W, padx=5, pady=3)
                finalship=int(shipprice[shipping.curselection()[0]])
                ttk.Label(root, text=('Total',(float(line[9])+finalship+((float(line[9])*825)/10000)))).grid(column=4, row=3, sticky=W, padx=5, pady=3)
            else:
                street1var.set('')
                statevar.set(line[4])
                cityvar.set(line[5])
                zipvar.set(line[6])
                description.delete(1.0,END)
                description.insert(1.0,line[7])
                pricevar.set(line[8])
                dayvar.set(int(line[9]))
                monthvar.set(int(line[10]))
                yearvar.set(int(line[11]))
                shipping.selection_clear(0,2)
                shipping.selection_set(int(line[12]))
                ttk.Label(root, text=('Tax',((float(line[8])*825)/10000))).grid(column=4, row=1, sticky=W, padx=5, pady=3)
                finalship=int(shipprice[shipping.curselection()[0]])
                ttk.Label(root, text=('Total',(float(line[8])+finalship+((float(line[8])*825)/10000)))).grid(column=4, row=3, sticky=W, padx=5, pady=3)
        line=file.readline()
    if x==0:
        messagebox.showinfo(title="Error", message="Entry does not exist.")
    file.close()

TopMenu=Menu(root)#creating toolbar
TopMenu=Menu(root)#creating toolbar
root.config(menu=TopMenu)
root.option_add('*tearOff',False)
SubMenu=Menu(TopMenu)#creating file section of toolbar
TopMenu.add_cascade(label='File',menu=SubMenu)
SubMenu.add_command(label='Exit',command=root.quit)
HelpMenu=Menu(TopMenu)#creating help section of toolbar
TopMenu.add_cascade(label='Help',menu=HelpMenu)
HelpMenu.add_command(label='About',command=about)
HelpMenu.add_command(label='Instructions',command=instr)

povar=StringVar()#setting up all needed variables and lists
firstvar=StringVar()
lastvar=StringVar()
streetvar=StringVar()
street1var=StringVar()
statevar=StringVar()
stateslist=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
cityvar=StringVar()
zipvar=StringVar()
pricevar=StringVar()
shippingvar=StringVar()
shiplist=['1 day','2 day','5 day']
shipprice=['10','7','4']
shiplist=StringVar(value=shiplist)
dayvar=IntVar()
daylist=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
monthvar=IntVar()
monthlist=['1','2','3','4','5','6','7','8','9','10','11','12']
yearvar=IntVar()
yearlist=['2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035','2036','2037','2038','2039','2040']

po=Entry(root,textvariable=povar,width=20)#every single widget, separate by which widget they are
po.grid(column=0, row=0, sticky=(W, E),columnspan=2,padx=5,pady=3)
ttk.Label(root,text='P.O.').grid(column=2,row=0,sticky=W,columnspan=2,padx=5,pady=3)

first=Entry(root,textvariable=firstvar,width=20)
first.grid(column=0, row=1, sticky=(W, E),columnspan=2,padx=5,pady=3)
ttk.Label(root,text='First').grid(column=2,row=1,sticky=W,columnspan=2,padx=5,pady=3)

last=Entry(root,textvariable=lastvar,width=20)
last.grid(column=0, row=2, sticky=(W, E),columnspan=2,padx=5,pady=3)
ttk.Label(root,text='Last').grid(column=2,row=2,sticky=W,columnspan=2,padx=5,pady=3)

street=Entry(root,textvariable=streetvar,width=20)
street.grid(column=0, row=3, sticky=(W, E),columnspan=2,padx=5,pady=3)
ttk.Label(root,text='Street').grid(column=2,row=3,sticky=W,columnspan=2,padx=5,pady=3)

street1=Entry(root,textvariable=street1var,width=20)
street1.grid(column=0, row=4, sticky=(W, E),columnspan=2,padx=5,pady=3)
ttk.Label(root,text='Street(2)').grid(column=2,row=4,sticky=W,columnspan=2,padx=5,pady=3)

state=ttk.Combobox(root,textvariable=statevar,width=2,values=stateslist,state='readonly')
state.grid(column=0, row=5, sticky=(W, E),padx=5,pady=3)
ttk.Label(root,text='State').grid(column=1,row=5,sticky=W,padx=5,pady=3)

city=Entry(root,textvariable=cityvar,width=10)
city.grid(column=0, row=6, sticky=(W, E),padx=5,pady=3)
ttk.Label(root,text='City').grid(column=1,row=6,sticky=W,padx=5,pady=3)

zip=Entry(root,textvariable=zipvar,width=10)
zip.grid(column=0, row=7, sticky=(W, E),padx=5,pady=3)
ttk.Label(root,text='Zip').grid(column=1,row=7,sticky=W,padx=5,pady=3)

description=Text(root,width=20,height=5)
description.grid(column=0, row=8, sticky=(W, E),padx=5,pady=3,columnspan=2)
ttk.Label(root,text='Description').grid(column=2,row=8,sticky=W,padx=5,pady=3)

price=Entry(root,textvariable=pricevar,width=20)
price.grid(column=4,row=0,sticky=(W,E),padx=5,pady=3,columnspan=2)
ttk.Label(root,text='Price').grid(column=6,row=0,sticky=W,padx=5,pady=3)

ttk.Label(root,text='Tax').grid(column=4,row=1,sticky=W,padx=5,pady=3)

shipping=Listbox(root,listvariable=shiplist,height=3,exportselection=False)
shipping.grid(column=4,row=2,sticky=(W,E),padx=5,pady=3,columnspan=2)
ttk.Label(root,text='Shipping').grid(column=6,row=2,sticky=W,padx=5,pady=3)
shipping.bind('<<ListboxSelect>>',calc)

ttk.Label(root,text='Total').grid(column=4,row=3,sticky=W,padx=5,pady=3)

day=Spinbox(root,values=daylist, textvariable=dayvar,width=2,wrap=True)
day.grid(column=4,row=4,sticky=(W,E),padx=5,pady=3)
ttk.Label(root,text='Day').grid(column=4,row=5,sticky=W,padx=5,pady=3)

month=Spinbox(root,values=monthlist, textvariable=monthvar,width=2,wrap=True)
month.grid(column=5,row=4,sticky=(W,E),padx=5,pady=3)
ttk.Label(root,text='Month').grid(column=5,row=5,sticky=W,padx=5,pady=3)

year=Spinbox(root,values=yearlist, textvariable=yearvar,width=2,wrap=True)
year.grid(column=6,row=4,sticky=(W,E),padx=5,pady=3)
ttk.Label(root,text='Year').grid(column=6,row=5,sticky=W,padx=5,pady=3)

ttk.Button(root,text='Submit',command=submit).grid(column=4,row=6,sticky=W,padx=5,pady=3)
ttk.Button(root,text='Retrieve',command=retrieve).grid(column=6,row=6,sticky=W,padx=5,pady=3)

root.columnconfigure(0, weight=1)#sizing
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.rowconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
root.rowconfigure(6, weight=1)
root.columnconfigure(7, weight=1)
root.rowconfigure(7, weight=1)
root.columnconfigure(8, weight=1)
root.rowconfigure(8, weight=1)
root.columnconfigure(9, weight=1)
root.rowconfigure(9, weight=1)
root.columnconfigure(10, weight=1)
root.rowconfigure(10, weight=1)
root.columnconfigure(11, weight=1)
root.rowconfigure(11, weight=1)
ttk.Sizegrip(root).grid(column=999,row=999,sticky=(S,E))

root.mainloop()