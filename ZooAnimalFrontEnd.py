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

l4=Label(window,text="Feeding Schedule")
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




window.mainloop()