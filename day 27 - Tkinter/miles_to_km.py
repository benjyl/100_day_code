from tkinter import *

window = Tk()
# window.minsize(width=300, height=200)
window.config(padx=30, pady=30)
window.title("Miles to Km converter")


def convert():
    # convert miles to km
    miles = float(miles_input.get())
    km = miles * 1.609
    converted_kms["text"] = round(km, 3)


miles_input = Entry()
miles_input.grid(row=0, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

equal = Label(text="is equal to")
equal.grid(row=1, column=0)

converted_kms = Label(text="0")
converted_kms.grid(row=1, column=1)
kms = Label(text="Km")
kms.grid(row=1, column=2)

calculate = Button(text="Calculate", command=convert)
calculate.grid(row=2, column=1)

for child in window.winfo_children():
    child.grid_configure(padx=10, pady=10)

window.mainloop()
