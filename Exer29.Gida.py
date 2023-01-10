
from tkinter import *
  
creatingList = Tk()  
creatingList.title("ListBox")
# setting the icon for the window  
creatingList.iconbitmap("pyicon.ico")
# setting the size and position of the window  
creatingList.geometry("320x380+320+380")  
# disabling the resizable option for better UI  
creatingList.resizable(0, 0)
name = Label(creatingList, text = "Developed By: Crismark E. Gida \n BSIT IV", font=('Poppins',8)).place(x = 70, y = 330) 
  
lbl = Label(creatingList,text = "A list of favourite countries...",font=('Poppins',12))  


listbox = Listbox(creatingList,font=('Poppins',12))  
  
listbox.insert(1,"India")  
  
listbox.insert(2, "USA")  
  
listbox.insert(3, "Japan")  
  
listbox.insert(4, "Australia")  
  
lbl.pack()  
listbox.pack()  
creatingList.mainloop()  
