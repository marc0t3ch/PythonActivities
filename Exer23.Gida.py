#Tkinter Email Validation in python
import tkinter as tk
from tkinter import ttk
import re

class App(tk.Tk):
    def __init__(emailValidation):
        super().__init__()

        emailValidation.title('Tkinter Email Validation Validation')
        # setting the icon for the window  
        emailValidation.iconbitmap("pyicon.ico") 
        emailValidation.create_widgets()

    def create_widgets(emailValidation):
        emailValidation.columnconfigure(0, weight=1)
        emailValidation.columnconfigure(1, weight=3)
        emailValidation.columnconfigure(2, weight=1)

        # label
        ttk.Label(text='Email:',font=('Poppins',10)).grid(row=0, column=0, padx=5, pady=20)

        # email entry
        vcmd = (emailValidation.register(emailValidation.validate), '%P')
        ivcmd = (emailValidation.register(emailValidation.on_invalid),)

        emailValidation.email_entry = ttk.Entry(emailValidation, width=50,font=('Poppins',10))
        emailValidation.email_entry.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        emailValidation.email_entry.grid(row=0, column=1, columnspan=2, padx=5)

        emailValidation.label_error = ttk.Label(emailValidation, foreground='red',font=('Poppins',10,'bold'))
        emailValidation.label_error.grid(row=1, column=1, sticky=tk.W, padx=5)

        # button
        emailValidation.send_button = ttk.Button(text='Send').grid(row=0, column=4, padx=5)
        ttk.Style().configure("TButton", padding=1, relief="flat",
        background="black",font=('Poppins',9))
    #Show message function
    def show_message(emailValidation, error='', color='black'):
        emailValidation.label_error['text'] = error
        emailValidation.email_entry['foreground'] = color
        
    #Validate the email entry
    def validate(emailValidation, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value) is None:
            return False

        emailValidation.show_message('Valid Email', 'blue')
        return True
    
    #Show the error message if the data is not valid
    def on_invalid(emailValidation):
        emailValidation.show_message('Please enter a valid email', 'blue')


if __name__ == '__main__':
    app = App()
    app.mainloop()
