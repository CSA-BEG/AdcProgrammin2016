#My code didn't work, so I tried selling my soul to the devil, now my code doesn't work, and I'm ginger.
#Trey Grant 9/12/16
from tkinter import ttk
from tkinter import *
root = Tk()
root.title("It's called a check BOX oh brainless ones.")
def hiya():
    ttk.Label(mainframe,text='Hiya!').grid(column=1,row=2,sticky=W)
def yeah():
    vari=str(yon.get())
    var=str(noy.get())
    if vari=='1':
        if var!='1':
            hi.state(['!disabled'])
        else:
            hi.state(['disabled'])
    else:
        hi.state(['disabled'])
def nah():
    vari=yon.get()
    var=noy.get()
    if vari=='1':
        if var!='1':
            hi.state(['!disabled'])
        else:
            hi.state(['disabled'])
    else:
        hi.state(['disabled'])
mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)

yon=IntVar()
noy=IntVar()
yes=ttk.Checkbutton(mainframe,text='Yes',variable=yon,command=yeah)
yes.grid(column=1,row=1,sticky=W)
no=ttk.Checkbutton(mainframe,text='No',variable=noy,command=nah)
no.grid(column=2,row=1,sticky=W)
hi=ttk.Button(mainframe, text="Hi",command=hiya)
hi.grid(column=2, row=2, sticky=W)
hi.state(['disabled'])
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', hi)

root.mainloop()
