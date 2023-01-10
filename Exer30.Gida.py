from tkinter import *  
  
deletingList = Tk()  
deletingList.title("Delete Item in ListBox")
# setting the icon for the window  
deletingList.iconbitmap("pyicon.ico")
# setting the size and position of the window  
deletingList.geometry("320x420+320+420")  
# disabling the resizable option for better UI  
deletingList.resizable(0, 0)
name = Label(deletingList, text = "Developed By: Crismark E. Gida \n BSIT IV", font=('Poppins',8)).place(x = 70, y = 380)   
lbl = Label(deletingList,text = "A list of favourite countries...",font=('Poppins',12))  
  
listbox = Listbox(deletingList,font=('Poppins',12))   
listbox.insert(1,"India")    
listbox.insert(2, "USA")    
listbox.insert(3, "Japan")   
listbox.insert(4, "Australia")  
  
#this button will delete the selected item from the list     
btn = Button(deletingList, text = "delete",font=('Poppins',12),width=10, command = lambda listbox=listbox: listbox.delete(ANCHOR))  
  
lbl.pack()    
listbox.pack()   
btn.pack()  
deletingList.mainloop()  
