# import all functions from the tkinter  
from tkinter import *
 
# import messagebox class from tkinter
from tkinter import messagebox
 
# Function for clearing the 
# contents of all text entry boxes
def clearAll() :
 
    # deleting the content from the entry box
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    givenDayField.delete(0, END)
    givenMonthField.delete(0, END)
    givenYearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)
 
# function for checking error
def checkError() :
 
    # if any of the entry field is empty
    # then show an error message and clear
    # all the entries
    if (dayField.get() == "" or monthField.get() == ""
        or yearField.get() == "" or givenDayField.get() == ""
        or givenMonthField.get() == "" or givenYearField.get() == "") :
 
        # show the error message
        messagebox.showerror("Input Error","Enter th correct Input!")
 
        # clearAll function calling
        clearAll()
         
        return -1
 
# function to calculate Age
def calculateAge() :
 
    # check for error
    value = checkError()
 
    # if error is occur then return
    if value ==  -1 :
        return
    else : 
        # take a value from the respective entry boxes
        # get method returns current text as string
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())
 
        given_day = int(givenDayField.get())
        given_month = int(givenMonthField.get())
        given_year = int(givenYearField.get())

        # if birth date is greater then given birth_month
        # then donot count this month and add 30 to the date so
        # as to subtract the date and get the remaining days
        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
         
        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[birth_month-1]
                     
                     
        # if birth month exceeds given month, then
        # donot count this year and add 12 to the
        # month so that we can subtract and find out
        # the difference
        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12
                     
        # calculate day, month, year
        calculated_day = given_day - birth_day;
        calculated_month = given_month - birth_month;
        calculated_year = given_year - birth_year;
 
        # calculated day, month, year write back
        # to the respective entry boxes
 
        # insert method inserting the 
        # value in the text entry box.
        rsltDayField.insert(10, str(calculated_day))
        rsltMonthField.insert(10, str(calculated_month))
        rsltYearField.insert(10, str(calculated_year))
     
 
# Driver Code
if __name__ == "__main__" :
 
    # Create a GUI window
    ageCalculator = Tk()
 
    # Set the background colour of GUI window 
    ageCalculator.configure(background = "#F7EFE8")
    # setting the icon for the window  
    ageCalculator.iconbitmap("pyicon.ico") 
    # set the name of tkinter GUI window
    ageCalculator.title("Age Calculator")
 
     # Set the configuration of GUI window
    ageCalculator.geometry("525x350")
    ageCalculator.resizable(0, 0)
    name = Label(ageCalculator, text = "Developed By: Crismark E. Gida \n BSIT IV",bg = "#F7EFE8", font=('Poppins',8)).place(x = 150, y = 290) 
    # Create a Date Of Birth : label
    dob = Label(ageCalculator, text = "Date Of Birth", bg = "yellow", fg = "green", font=('Poppins',8), width=18)
 
    # Create a Given Date : label
    givenDate = Label(ageCalculator, text = "Given Date", bg = "yellow", fg = "green", font=('Poppins',8), width=18)
 
    # Create a Day : label
    day = Label(ageCalculator, text = "Day", bg = "#F7EFE8",font=('Poppins',8))
 
    # Create a Month : label
    month = Label(ageCalculator, text = "Month", bg = "#F7EFE8", font=('Poppins',8))
 
    # Create a Year : label
    year = Label(ageCalculator, text = "Year", bg = "#F7EFE8", font=('Poppins',8))
 
    # Create a Given Day : label
    givenDay = Label(ageCalculator, text = "Given Day", bg = "#F7EFE8", font=('Poppins',8))
 
    # Create a Given Month : label
    givenMonth = Label(ageCalculator, text = "Given Month", bg = "#F7EFE8", font=('Poppins',8))
 
    # Create a Given Year : label
    givenYear = Label(ageCalculator, text = "Given Year", bg = "#F7EFE8", font=('Poppins',8))
 
    # Create a Years : label
    rsltYear = Label(ageCalculator, text = "Years", bg = "#F7EFE8", font=('Poppins',8))
 
    # Create a Months : label
    rsltMonth = Label(ageCalculator, text = "Months", bg = "#F7EFE8", font=('Poppins',8))
 
    # Create a Days : label
    rsltDay = Label(ageCalculator, text = "Days", bg = "#F7EFE8", font=('Poppins',8))
 
    # Create a Resultant Age Button and attached to calculateAge function
    resultantAge = Button(ageCalculator, text = "Resultant Age", fg = "black", bg = "#d9fb83", command = calculateAge)
 
    # Create a Clear All Button and attached to clearAll function
    clearAllEntry = Button(ageCalculator, text = "Clear All", fg = "black", bg = "#d9fb83", command = clearAll)
 
    # Create a text entry box for filling or typing the information. 
    dayField = Entry(ageCalculator)
    monthField = Entry(ageCalculator)
    yearField = Entry(ageCalculator)
     
    givenDayField = Entry(ageCalculator)
    givenMonthField = Entry(ageCalculator)
    givenYearField = Entry(ageCalculator)
     
    rsltYearField = Entry(ageCalculator)
    rsltMonthField = Entry(ageCalculator)
    rsltDayField = Entry(ageCalculator)
 
 
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure .
    dob.grid(row = 0, column = 1)
     
    day.grid(row = 1, column = 0)
    dayField.grid(row = 1, column = 1)
     
    month.grid(row = 2, column = 0)
    monthField.grid(row = 2, column = 1)
     
    year.grid(row = 3, column = 0)
    yearField.grid(row = 3, column = 1)
     
    givenDate.grid(row = 0, column = 4)
     
    givenDay.grid(row = 1, column = 3)
    givenDayField.grid(row = 1, column = 4)
     
    givenMonth.grid(row = 2, column = 3)
    givenMonthField.grid(row = 2, column = 4)
     
    givenYear.grid(row = 3, column = 3)
    givenYearField.grid(row = 3, column = 4)
     
    resultantAge.grid(row = 4, column = 2)
     
    rsltYear.grid(row = 5, column = 2)
    rsltYearField.grid(row = 6, column = 2)
     
    rsltMonth.grid(row = 7, column = 2)
    rsltMonthField.grid(row = 8, column = 2)
     
    rsltDay.grid(row = 9, column = 2)
    rsltDayField.grid(row = 10, column = 2)
 
    clearAllEntry.grid(row = 15, column = 2)
 
    # Start the GUI
    ageCalculator.mainloop()   
