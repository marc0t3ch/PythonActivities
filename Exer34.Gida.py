# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
messageBox = Tk()
messageBox.title("Dropdown Menu")
# setting the icon for the window  
messageBox.iconbitmap("pyicon.ico")
messageBox.geometry("200x200")
name = Label(messageBox, text = "Developed By: Crismark E. Gida \n BSIT IV", font=('Poppins',8)).place(x = 10, y = 70) 
messagebox.askretrycancel("Application","Do you want to try again?")  
messageBox.mainloop()  
