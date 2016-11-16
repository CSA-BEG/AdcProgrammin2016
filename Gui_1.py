#Trey Grant 9/19/16
from tkinter import *
from tkinter import ttk
import getpass
import csv
import time
import os
import re
import hashlib
import RPi.GPIO as io
from datetime import datetime
io.setmode(io.BCM)
pir_pin = 24
power_pin = 27
os.system("clear")
io.setup(pir_pin, io.IN)
io.setup(power_pin, io.OUT)
io.output(power_pin, False)
PERIOD_OF_TIME = 1800
root = Tk()
root.title("Login")

mainframe = ttk.Frame(root, padding="6 6 6 6")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)#general tkinter setup til now

def forgotpassword():
    ttk.Label(mainframe,text='You forgot it!').grid(row=1,column=3,sticky=W)

def login(*args):
        global z
        try:
            z=0
            f2 = open('hashd.csv', 'r')
            f = open("Logins.txt", "a")
            students = csv.reader(f2)
            username = str(nam.get())
            password = str(pas.get())
            name.delete(0, 'end')
            passw.delete(0, 'end')
            username_rowgetnumyo = 2  # change host_row to the corresponding row - 1 (ie; row 45, put in 44) in google's csv
            password_rowgetnum = 3  # master_row to the schools student list
            salt = "gnuvie:^)"
            for hosts_rowyo in students:
                row = 1
                username = username.replace("@chaparralstaracademy.com", "")
                hosts_rowyo[username_rowgetnumyo] = hosts_rowyo[username_rowgetnumyo].replace(
                    "@chaparralstaracademy.com", "")
                hosts_rowyo[username_rowgetnumyo] = hosts_rowyo[username_rowgetnumyo].zfill(4)
                print(str(hashlib.sha256(username.encode("UTF-8")).hexdigest())+" username "+hosts_rowyo[username_rowgetnumyo]+"\n"+str(hashlib.sha256(password.encode("UTF-8")).hexdigest())+" password "+hosts_rowyo[password_rowgetnum])
                if (username == "displayport:^)"):
                    exit()
                if (hashlib.md5((salt + username).encode("UTF-8")).hexdigest() == hosts_rowyo[username_rowgetnumyo]) & (
                    hashlib.md5((salt + password).encode("UTF-8")).hexdigest() == hosts_rowyo[password_rowgetnum]):
                    #print("Logging in.", end=""),
                    #time.sleep(1)
                    #print(".", end=""),
                    #time.sleep(1)
                    #print(".")
                    #time.sleep(3)
                    #os.system("clear")
                    ttk.Label(mainframe,text="Logging in complete! Plug in your chromebook now.").grid(column=1,row=4)
                    z=1
                    f.write(username + " " + str(datetime.now()) + "\n")
                    f.close()
                    start = time.time()
                    while True:
                        io.output(power_pin, True)
                        
                        if time.time() > start + PERIOD_OF_TIME:
                        #     print("POWER OFF")
                             #time.sleep(1)
                             io.output(power_pin, False)
                             #time.sleep(3)
                             login()
                             break
                        #print("It works!")
                        break
                    break
            if z!=1:
                #print("Logging in.", end=""),
                #time.sleep(1)
                #print(".", end=""),
                #time.sleep(1)
                #print(".")
                #time.sleep(3)
                #os.system("clear")
                ttk.Label(mainframe,text="Error logging in, please try again! ").grid(column=1,row=4)
                f2.close()
                f.close()
        except KeyboardInterrupt:
            #print("Error, please try again! ")
            login()

nam=StringVar()
name=ttk.Entry(mainframe,textvariable=nam,width=20)#username entry box
name.grid(column=1,row=1,sticky=W)
ttk.Label(mainframe,text='Name').grid(row=1,column=2,sticky=W)

pas=StringVar()
passw=ttk.Entry(mainframe,textvariable=pas,width=20,show="*")#password entry box
passw.grid(column=1,row=2,sticky=W)
ttk.Label(mainframe,text='Password').grid(row=2,column=2,sticky=W)

log=ttk.Button(mainframe,text='Login',command=login)
log.grid(column=1,row=3,sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)#general tkinter setup after this

name.focus()
root.bind('<Return>',login)

root.mainloop()
