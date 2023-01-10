# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
radioButton = Tk()

# Set the size of the window
radioButton.geometry("350x270")
# disabling the resizable option for better UI  
radioButton.resizable(0, 0)
radioButton.title("Radio Button")
# setting the icon for the window  
radioButton.iconbitmap("pyicon.ico")
# Define a function to get the output for selected option
def selection():
   selected = "You selected the option " + str(radio.get())
   label.config(text=selected,font=('Poppins',11))

radio = IntVar()
Label(text="Your Favourite programming language:", font=('Poppins',11,'bold')).pack()

# Define radiobutton for each options
r1 = Radiobutton(radioButton, text="C++", variable=radio, value=1,font=('Poppins',11), command=selection)
r1.pack(anchor=W)
r2 = Radiobutton(radioButton, text="Python", variable=radio, value=2,font=('Poppins',11), command=selection)
r2.pack(anchor=W)
r3 = Radiobutton(radioButton, text="Java", variable=radio, value=3,font=('Poppins',11), command=selection)
r3.pack(anchor=W)

# Define a label widget
label = Label(radioButton)
label.pack()
name = Label(radioButton, text = "Developed By: Crismark E. Gida \n BSIT IV", font=('Poppins',8)).place(x = 70, y = 200) 

radioButton.mainloop()
