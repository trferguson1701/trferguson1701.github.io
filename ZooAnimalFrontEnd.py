"""
Front End program to handle animal information-
Species, Name, Age, Feeding Schedule
"""

from tkinter import *

window=Tk()

window.wm_title("ZooAnimals")

l1=Label(window,text="Species")
l1.grid(row=0,column=0)

l2=Label(window,text="Name")
l2.grid(row=0,column=2)

l3=Label(window,text="Age")
l3.grid(row=1,column=0)

l4=Label(window,text="Feeding Schedule")
l4.grid(row=1,column=2)



window.mainloop()