"""
Front End program to handle animal information-
Species, Name, Age, Feeding Schedule
"""

from tkinter import *
import ZooAnimalBackend

def get_selected_row(event):
    global selected_tuple
    index=result1.curselection()[0]
    selected_tuple=result1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    

#View all functionality
def view_command():
    result1.delete(0,END)
    for row in ZooAnimalBackend.view():
        result1.insert(END,row)


#Search Functionality
def search_command():
    result1.delete(0,END)
    for row in ZooAnimalBackend.search(Species_text.get(),Name_text.get(),Age_text.get(),Feed_text.get()):
        result1.insert(END,row)

#Create Functionality
def create_command():
    ZooAnimalBackend.insert(Species_text.get(),Name_text.get(),Age_text.get(),Feed_text.get())
    result1.delete(0,END)
    result1.insert(END,(Species_text.get(),Name_text.get(),Age_text.get(),Feed_text.get()))

#Delete Functionality
def delete_command():
    ZooAnimalBackend.delete(selected_tuple[0])

#Update Functionality
def update_command():
    ZooAnimalBackend.update(selected_tuple[0],Species_text.get(),Name_text.get(),Age_text.get(),Feed_text.get())




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
e1=Entry(window, textvariable=Species_text,bg="PaleGreen3")
e1.grid(row=0, column=1)

Name_text=StringVar()
e2=Entry(window, textvariable=Name_text,bg="PaleGreen3")
e2.grid(row=0, column=3)

Age_text=StringVar()
e3=Entry(window, textvariable=Age_text,bg="PaleGreen3")
e3.grid(row=1, column=1)

Feed_text=StringVar()
e4=Entry(window, textvariable=Feed_text,bg="PaleGreen3")
e4.grid(row=1, column=3)

#Results box creation

result1=Listbox(window, height=6,width=35)
result1.grid(row=2,column=0,rowspan=6,columnspan=2)

#Scroll bar creation

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

result1.configure(yscrollcommand=sb1.set)
sb1.configure(command=result1.yview)

result1.bind('<<ListboxSelect>>',get_selected_row)

#Button Creation

b1=Button(window,text="View All", width=12,command=view_command,bg="green")
b1.grid(row=2,column=3)

b2=Button(window,text="Search", width=12,command=search_command,bg="green")
b2.grid(row=3,column=3)

b3=Button(window,text="Create", width=12,command=create_command,bg="green")
b3.grid(row=4,column=3)

b4=Button(window,text="Update", width=12,command=update_command,bg="green")
b4.grid(row=5,column=3)

b5=Button(window,text="Delete", width=12,command=delete_command,bg="green")
b5.grid(row=6,column=3)

b6=Button(window,text="End", width=12,command=window.destroy,bg="red")
b6.grid(row=7,column=3)



window.configure(bg="Gray")
window.mainloop()