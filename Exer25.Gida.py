# Python program to create a table
from tkinter import *
 
class Table:
    def __init__(self,createTable):
        
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):     
                self.e = Entry(createTable, width=15, fg='blue',
                               font=('Poppins',16))            
                self.e.grid(pady=1,row=i, column=j)
                self.e.insert(END, lst[i][j])
 
# take the data
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
createTable = Tk()
createTable.title("Table in Tkinter")  
# setting the size and position of the window  
createTable.geometry("750x280+750+280")  
# disabling the resizable option for better UI
# setting the icon for the window  
createTable.iconbitmap("pyicon.ico") 
createTable.resizable(0, 0)
name = Label(createTable, text = "Developed By: Crismark E. Gida \n BSIT IV", font=('Poppins',16)).place(x = 200, y = 210) 
t = Table(createTable)
createTable.mainloop()
