from tkinter import *
from functools import partial


def validateCred(username, password):
    print("Username:", username.get())
    print("Password:", password.get())
    return



#Window Specifications

window=Tk()
window.geometry('400x150')
window.title("ZooAnimals Login")

#Text box Creation for user 
l1=Label(window,text="Username:")
l1.grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(window, textvariable=username)
usernameEntry.grid(row=0, column=1)

#Text box Creation for password
l2=Label(window,text="Password:")
l2.grid(row=1, column=0)
password = StringVar()
passwordEntry= Entry(window, textvariable=password, show='*')
passwordEntry.grid(row=1, column=1)

#validation creation
validateCred = partial(validateCred, username, password)

#Button Creation

b1=Button(window,text="login",command=window.destroy)
b1.grid(row=4,column=1)
    

window.mainloop()

import ZooAnimalFrontEnd