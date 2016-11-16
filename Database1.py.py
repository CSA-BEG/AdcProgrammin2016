#Trey Grant 9/19/16
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("States & names")

mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)#general tkinter setup til now

ttk.Label(mainframe,text='First Name').grid(column=2,row=1,sticky=W)#setting up labels
ttk.Label(mainframe,text='Last Name').grid(column=2,row=2,sticky=W)

def policy_check(*args):
    acc=str(accept.get())
    if acc!='2':
        done.state(['!disabled'])
    else:
        done.state(['disabled'])

def check(*args):
    file=open('log1.csv','a')
    firstn=str(firstname.get())
    lastn=str(lastname.get())
    bisn=str(businessstuffs.get())
    statn=str(stat.get())
    if firstn=='':
        ttk.Label(mainframe,text='Please fill out the form to completion before submiting.').grid(column=1,row=6,sticky=W)
        return
    elif lastn=='':
        ttk.Label(mainframe,text='Please fill out the form to completion before submiting.').grid(column=1,row=6,sticky=W)
        return
    elif bisn=='':
        ttk.Label(mainframe,text='Please fill out the form to completion before submiting.').grid(column=1,row=6,sticky=W)
        return
    elif statn=='':
        ttk.Label(mainframe,text='Please fill out the form to completion before submiting.').grid(column=1,row=6,sticky=W)
        return
    firstname.set("")
    lastname.set("")
    businessstuffs.set("")
    accept.set("")
    stat.set("")
    templist=firstn+','+lastn+','+bisn+','+statn+'\n'
    file.write(templist)
    file.close()
    done.state(['disabled'])

firstname=StringVar()#setting up variables
lastname=StringVar()
businessstuffs=StringVar()
accept=StringVar()
stat=StringVar()

first=ttk.Entry(mainframe,textvariable=firstname,width=15)#setting up widgets
last=ttk.Entry(mainframe,textvariable=lastname,width=15)
bus=ttk.Radiobutton(mainframe,text='Business',variable=businessstuffs,value=1)
res=ttk.Radiobutton(mainframe,text='Residential',variable=businessstuffs,value=2)
oth=ttk.Radiobutton(mainframe,text='Other',variable=businessstuffs,value=3)
sta=ttk.Combobox(mainframe,textvariable=stat,values=('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachussetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvannia', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'),state='readonly')
policy=ttk.Checkbutton(mainframe,text='Accept Policy',variable=accept,onvalue=1,offvalue=2,command=policy_check)
done=ttk.Button(mainframe,text='submit',command=check)
done.state(['disabled'])

first.grid(column=1,row=1,sticky=W)#setting up grid
last.grid(column=1,row=2,sticky=W)
bus.grid(column=1,row=3,sticky=W)
res.grid(column=2,row=3,sticky=W)
oth.grid(column=3,row=3,sticky=W)
policy.grid(column=1,row=5,sticky=W)
sta.grid(column=1,row=4,sticky=W)
done.grid(column=2,row=5,sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)#general tkinter setup after this
first.focus()
root.bind('<Return>', check)
root.mainloop()
