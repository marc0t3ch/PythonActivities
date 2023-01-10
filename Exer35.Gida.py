from tkinter import *

class showWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number',font=('Poppins',12),bg='green',fg='white')
        self.lbl2=Label(win, text='Second number',font=('Poppins',12),bg='green',fg='white')
        self.lbl3=Label(win, text='Result',font=('Poppins',12),bg='green',fg='white')
        self.t1=Entry(font=('Poppins',12,'bold'),bd=2)
        self.t2=Entry(font=('Poppins',12,'bold'),bd=2)
        self.t3=Entry(font=('Poppins',12,'bold'),bd=2)
        self.btn1 = Button(win, text='Add',font=('Poppins',12,'bold'))
        self.btn2=Button(win, text='Subtract',font=('Poppins',12,'bold'))
        self.lbl1.place(x=50, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=50, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Add',font=('Poppins',12,'bold'),width=8,bg='yellow',command=self.add)
        self.b2=Button(win, text='Subtract',font=('Poppins',12,'bold'),bg='orange',fg='white')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=200, y=150)
        self.b2.place(x=320, y=150)
        self.lbl3.place(x=100, y=220)
        self.t3.place(x=200, y=220)
        
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
        
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

minusAdd=Tk()
mywin=showWindow(minusAdd)
minusAdd.title('Add & Subtract Calculator')
minusAdd.geometry("500x300+10+10")
# setting the icon for the window  
minusAdd.iconbitmap("pyicon.ico")
# disabling the resizable option for better UI  
minusAdd.resizable(0, 0)
minusAdd.config(bg='green')

minusAdd.mainloop()
