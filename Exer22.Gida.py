import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

textEditor = tk.Tk()
textEditor.title("Simple Text Editor")
# setting the icon for the window  
textEditor.iconbitmap("pyicon.ico") 
#function to open the file   
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    textEditor.title(f"Simple Text Editor - {filepath}")
#function to save the file   
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    textEditor.title(f"Simple Text Editor - {filepath}")
#Size of the screen
textEditor.rowconfigure(0, minsize=500, weight=1)
textEditor.columnconfigure(1, minsize=500, weight=1)

#Frame and the two Buttons for open and save as
txt_edit = tk.Text(textEditor)
frm_buttons = tk.Frame(textEditor, relief=tk.SUNKEN, bd=1)
frm_buttons .config(bg='#ffd503')
btn_open = tk.Button(frm_buttons, text="Open",font=('Poppins',8,'bold'),bg='white',fg='black', command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As", font=('Poppins',8,'bold'),bg='white',fg='black',command=save_file)

#padding and positioning of the 2 buttons
btn_open.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
btn_save.grid(row=1, column=0, sticky="ew", padx=10)
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
#function to open the file
#Developed by Crismark E. Gida
#BSIT IV
textEditor.mainloop()
