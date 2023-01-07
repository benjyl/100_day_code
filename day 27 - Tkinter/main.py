from tkinter import *

def button_clicked():
    output = input.get()
    message = "clicked"
    print(message)
    my_label["text"] = output
    
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# methods for changing labels
my_label["text"] = "New Text"
my_label.config(text="Even newer text")

my_label.grid(row=0, column=0) # what creates label on screen - layout of component

button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="Second click")
new_button.grid(row=0, column =2)

#Entry
input = Entry(width=10)
input.grid(row=2, column=3)
 


window.mainloop() # at end of script, everything else want to add in to window comes first