"""
Front End program to handle animal information-
Species, Name, Age, Feeding Schedule
"""

from tkinter import *

# Window outline and creation

window=Tk()

window.wm_title("ZooAnimals")

l1=Label(window,text="Species")
l1.grid(row=0,column=0)

l2=Label(window,text="Name")
l2.grid(row=0,column=2)

l3=Label(window,text="Age")
l3.grid(row=1,column=0)

l4=Label(window,text="Feeding")
l4.grid(row=1,column=2)

# Text box creation and specs

Species_text=StringVar()
e1=Entry(window, textvariable=Species_text)
e1.grid(row=0, column=1)

Name_text=StringVar()
e2=Entry(window, textvariable=Name_text)
e2.grid(row=0, column=3)

Age_text=StringVar()
e3=Entry(window, textvariable=Age_text)
e3.grid(row=1, column=1)

Feed_text=StringVar()
e4=Entry(window, textvariable=Feed_text)
e4.grid(row=1, column=3)

#Results box creation

result1=Listbox(window, height=6,width=35)
result1.grid(row=2,column=0,rowspan=6,columnspan=2)

#Scroll bar creation

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

result1.configure(yscrollcommand=sb1.set)
sb1.configure(command=result1.yview)

#Button Creation

b1=Button(window,text="View All", width=12)
b1.grid(row=2,column=3)

b2=Button(window,text="Search", width=12)
b2.grid(row=3,column=3)

b3=Button(window,text="Create", width=12)
b3.grid(row=4,column=3)

b4=Button(window,text="Update", width=12)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete", width=12)
b5.grid(row=6,column=3)

b6=Button(window,text="End", width=12)
b6.grid(row=7,column=3)

window.mainloop()