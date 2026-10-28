from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_output.config(text=f"{km:.2f}")
    
#window
window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

label = Label(text="is equal to")
label.grid(row=1, column=0)

#Kilometers
km_label = Label(text="Km")
km_label.grid(row=1, column=2)
km_output = Label(text="0")
km_output.grid(row=1, column=1)

#Miles
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_input = Entry()
miles_input.grid(row=0, column=1)

#Button
button1 = Button(text="Calculate", command=calculate)
button1.grid(row=2, column=1)

window.mainloop()

