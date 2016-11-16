#Trey Grant 9/2/16
from tkinter import *
from tkinter import ttk
def calculate(*args):
    try:
        val=0
        valu=0
        taxes=0
        shipi=str(ship.get())
        shipi=int(shipi)
        if shipi<=2:
            valu+=25
        elif shipi==3:
            valu+=10
        elif shipi>3:
            valu+=5
        if item.get()!="":
            file=open('items.txt','r')
            value=str(item.get().lower().replace(" ",""))
            num=int(count.get())
            line=file.readline()
            line=line.split()
            i=line[0]
            while line:
                if i==value:
                    val+=num*(float(line[1]))
                    taxes+=num*(val*.0825)
                    valu+=(val+(taxes))
                    break
                else:
                    if line==[]:
                        break
                    else:
                        line=file.readline()
                        line=line.split()
                        i=line[0]
            file.close()
            line=''
        else:
            pass
        if item2.get()!="":
            file=open('items.txt','r')
            value=str(item2.get().lower().replace(" ",""))
            num=int(count2.get())
            line=file.readline()
            line=line.split()
            i=line[0]
            while line:
                if i==value:
                    val+=num*(float(line[1]))
                    taxes+=num*(val*.0825)
                    valu+=(val+(taxes))
                    break
                else:
                    if line==[]:
                        break
                    else:
                        line=file.readline()
                        line=line.split()
                        i=line[0]
            file.close()
            line=''
        else:
            pass
        if item3.get()!="":
            file=open('items.txt','r')
            value=str(item3.get().lower().replace(" ",""))
            num=int(count3.get())
            line=file.readline()
            line=line.split()
            i=line[0]
            while line:
                if i==value:
                    val+=num*(float(line[1]))
                    taxes+=num*(val*.0825)
                    valu+=(val+(taxes))
                    break
                else:
                    if line==[]:
                        break
                    else:
                        line=file.readline()
                        line=line.split()
                        i=line[0]
            file.close()
            line=''
        else:
            pass
        if item4.get()!="":
            file=open('items.txt','r')
            value=str(item4.get().lower().replace(" ",""))
            num=int(count4.get())
            line=file.readline()
            line=line.split()
            i=line[0]
            while line:
                if i==value:
                    val+=num*(float(line[1]))
                    taxes+=num*(val*.0825)
                    valu+=(val+(taxes))
                    break
                else:
                    if line==[]:
                        break
                    else:
                        line=file.readline()
                        line=line.split()
                        i=line[0]
            file.close()
            line=''
        else:
            pass
        cost.set(valu)
        tax.set(taxes)
    except ValueError:
        pass

root = Tk()
root.title("Order Form")

mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)

item=StringVar()
item2=StringVar()
item3=StringVar()
item4=StringVar()
count=StringVar()
count2=StringVar()
count3=StringVar()
count4=StringVar()
cost=StringVar()
ship=StringVar()
tax=StringVar()

count_entry = ttk.Entry(mainframe, width=6, textvariable=count)
count_entry.grid(column=2, row=5, sticky=(W, E))
count2_entry = ttk.Entry(mainframe, width=6, textvariable=count2)
count2_entry.grid(column=2, row=4, sticky=(W, E))
count3_entry = ttk.Entry(mainframe, width=6, textvariable=count3)
count3_entry.grid(column=2, row=3, sticky=(W, E))
count4_entry = ttk.Entry(mainframe, width=6, textvariable=count4)
count4_entry.grid(column=2, row=2, sticky=(W, E))
item_entry = ttk.Entry(mainframe, width=6, textvariable=item)
item_entry.grid(column=3, row=5, sticky=(W, E))
item2_entry = ttk.Entry(mainframe, width=6, textvariable=item2)
item2_entry.grid(column=3, row=4, sticky=(W, E))
item3_entry = ttk.Entry(mainframe, width=6, textvariable=item3)
item3_entry.grid(column=3, row=3, sticky=(W, E))
item4_entry = ttk.Entry(mainframe, width=6, textvariable=item4)
item4_entry.grid(column=3, row=2, sticky=(W, E))
ship_entry=ttk.Entry(mainframe,width=6,textvariable=ship)
ship_entry.grid(column=2,row=6,sticky=(W,E))

ttk.Label(mainframe,textvariable=cost).grid(column=2,row=8,sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=9, sticky=W)
ttk.Label(mainframe, text="Shipping Days").grid(column=3, row=6, sticky=W)
ttk.Label(mainframe,text='Total').grid(column=3,row=8,sticky=W)
ttk.Label(mainframe,text='Items').grid(column=3,row=1,sticky=W)
ttk.Label(mainframe,text='Tax').grid(column=3,row=7,sticky=W)
ttk.Label(mainframe,textvariable=tax).grid(column=2,row=7,sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

item_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
