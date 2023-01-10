from tkinter import *  

def new():
    lbl_result =Label(dropDownMenu, text="New File                    ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def open():
    lbl_result =Label(dropDownMenu, text="Open a File            ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def save():
    lbl_result =Label(dropDownMenu, text="Save your File         ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def saveas():
    lbl_result =Label(dropDownMenu, text="Save as new File ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def close():
    lbl_result =Label(dropDownMenu, text="Close File          ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def undo():
    lbl_result =Label(dropDownMenu, text="Undo Changes           ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def cut():
    lbl_result =Label(dropDownMenu, text="Cut a File           ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def copy():
    lbl_result =Label(dropDownMenu, text="Copy a File                     ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def paste():
    lbl_result =Label(dropDownMenu, text="Paste an object           ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def delete():
    lbl_result =Label(dropDownMenu, text="Delete a File           ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def selectAll():
    lbl_result =Label(dropDownMenu, text="Select All text           ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)
def about():
    lbl_result =Label(dropDownMenu, text="About the File          ",font=('Poppins',20,'bold'))
    lbl_result.place(x=40,y=40)

dropDownMenu = Tk()
dropDownMenu.title("Dropdown Menu")
# setting the icon for the window  
dropDownMenu.iconbitmap("pyicon.ico")
# setting the size and position of the window  
dropDownMenu.geometry("320x380+320+380")  
# disabling the resizable option for better UI  
dropDownMenu.resizable(0, 0)


name = Label(dropDownMenu, text = "Developed By: Crismark E. Gida \n BSIT IV", font=('Poppins',8)).place(x = 70, y = 300) 
#creates menubar
menubar = Menu(dropDownMenu,background='blue', fg='white')
# Sets menubar background color and active select but does not remove 3d  effect/padding
menubar.config(bg = "GREEN",fg='red',activebackground='red',activeforeground='pink',relief=FLAT)

filemenu = Menu(menubar, tearoff=0,font=('Poppins',12))
filemenu.add_command(label="New",font=('Poppins',12), command=new)
filemenu.add_command(label="Open",font=('Poppins',12), command=open)
filemenu.add_command(label="Save",font=('Poppins',12), command=save)
filemenu.add_command(label="Save as...",font=('Poppins',12), command=saveas)
filemenu.add_command(label="Close",font=('Poppins',12), command=close)

filemenu.add_separator()

filemenu.add_command(label="Exit",font=('Poppins',12), command=dropDownMenu.quit)
menubar.add_cascade(label="File",font=('Poppins',12), menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo",font=('Poppins',12), command=undo)

editmenu.add_separator()

editmenu.add_command(label="Cut",font=('Poppins',12), command=cut)
editmenu.add_command(label="Copy",font=('Poppins',12), command=copy)
editmenu.add_command(label="Paste",font=('Poppins',12), command=paste)
editmenu.add_command(label="Delete",font=('Poppins',12), command=delete)
editmenu.add_command(label="Select All",font=('Poppins',12), command=selectAll)

menubar.add_cascade(label="Edit",font=('Poppins',12), menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...",font=('Poppins',12), command=about)
menubar.add_cascade(label="Help",font=('Poppins',12), menu=helpmenu)

dropDownMenu.config(menu=menubar)
dropDownMenu.mainloop()
