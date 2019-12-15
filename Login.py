from tkinter import *


window=Tk()

l1=Label(window,text='User:')
l2=Label(window,text='Password:')

e1=Entry(window,textvariable=StringVar())
e2=Entry(window,show='*',textvariable=StringVar())

b1=Button(window,text='Log in')

l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack()

window.mainloop()

import ZooAnimalFrontEnd