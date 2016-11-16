#What burns aside from witches? Wood. Wood floats. What also floats? A duck. Therefore if a person weighs the same as a duck, they are a witch.
#Trey Grant 9/9/16
from tkinter import *
from tkinter import ttk
import codecs
def login(*args):
    name=str(user.get()).lower()
    word=str(pasw.get()).lower()
    yorn=str(yon.get())
    loginstuffs=name,word
    loginstuffs=str(loginstuffs)
    loginstuffs=loginstuffs.replace("'",'')
    loginstuffs=loginstuffs.replace("(",'')
    loginstuffs=loginstuffs.replace(")",'')
    loginstuffs=loginstuffs.replace(",",'')
    file=open('rot13.txt','r')
    for y in file:#you used to scold me for using variables like this, and what do you give us?
        i=y.split()
        e=[]
        e.append(codecs.encode(i[0],'rot13'))
        e.append(codecs.encode(i[1],'rot13'))
        j=' '.join(e)
        if j==loginstuffs:
            yon.set('Login\nSuccessful')
            break
        else:
            pass
    file.close
    if yon.get()!='Login\nSuccessful':
        yon.set('Login\nFailed')

root = Tk()
root.title("Login")

mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)

user=StringVar()
pasw=StringVar()
yon=StringVar()

ttk.Label(mainframe,textvariable=yon).grid(column=1,row=3,sticky=W)
frame=ttk.Frame(mainframe,relief=SUNKEN,padding=(5,10))
frame.grid(row=1,column=1,rowspan=2,columnspan=1,sticky=(N,S,W,E))
usern=ttk.Entry(mainframe, width=12, textvariable=user)
usern.grid(column=1, row=1, sticky=(W,E))
passw=ttk.Entry(mainframe, width=12, textvariable=pasw)
passw.grid(column=1, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Login", command=login).grid(column=2, row=3, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=20, pady=5)

usern.focus()
root.bind('<Return>', login)

root.mainloop()
