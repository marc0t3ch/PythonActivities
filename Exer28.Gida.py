 
from tkinter import *
 
def addNumbers():
    res=int(e1.get())+int(e2.get())
    myText.set(res)
 
addCalcu = Tk()
addCalcu.title("Addition Calculator")
# setting the icon for the window  
addCalcu.iconbitmap("pyicon.ico")
# setting the size and position of the window  
addCalcu.geometry("330x150+330+150")  
# disabling the resizable option for better UI  
addCalcu.resizable(0, 0)
name = Label(addCalcu, text = "Developed By: Crismark E. Gida \n BSIT IV", font=('Poppins',8)).place(x = 80, y = 90) 
myText=StringVar()
Label(addCalcu, text="First",font=('Poppins',10)).grid(row=0, sticky=W)
Label(addCalcu, text="Second",font=('Poppins',10)).grid(row=1, sticky=W)
Label(addCalcu, text="Result:",font=('Poppins',10)).grid(row=3, sticky=W)
result=Label(addCalcu, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(addCalcu,font=('Poppins',10))
e2 = Entry(addCalcu,font=('Poppins',10))
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
b = Button(addCalcu, text="Calculate",font=('Poppins',10), command=addNumbers)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
mainloop()
