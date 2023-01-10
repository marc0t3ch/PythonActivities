from tkinter import *  

displayLblFrame = Tk()
displayLblFrame.title("Label Frame")
# setting the icon for the window  
displayLblFrame.iconbitmap("pyicon.ico")
labelframe = LabelFrame(displayLblFrame, text="Positive Comments",font=('Poppins',10,'bold'))
labelframe.pack(fill="both", expand="yes")
 
left = Label(labelframe, text="Place to put the positive comments",font=('Poppins',10))
left.pack(pady=20)

labelframe2 = LabelFrame(displayLblFrame, text="Negative Comments",font=('Poppins',10,'bold'))
labelframe2.pack(fill="both", expand="yes")
 
left = Label(labelframe2, text="Place to put the negative comments\n\nDeveloped By: Crismark E. Gida \n BSIT IV",font=('Poppins',10))
left.pack(pady=20)

displayLblFrame.mainloop()
