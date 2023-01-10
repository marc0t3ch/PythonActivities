import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# Set up the window
window = tk.Tk()
window.configure(bg='#fff9ef')
window.title("Temperature Converter")
window.resizable(width=False, height=False)
# setting the icon for the window  
window.iconbitmap("pyicon.ico") 

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10,font=('Poppins',16,'bold'))
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}",font=('Poppins',16,'bold'),bg='#fff9ef')

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",font=('Poppins',12,'bold'),
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}",font=('Poppins',16,'bold'),bg='#fff9ef')

# Set up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=40)
btn_convert.grid(row=0, column=1, pady=40)
lbl_result.grid(row=0, column=2, padx=40)

# Run the application
window.mainloop()
