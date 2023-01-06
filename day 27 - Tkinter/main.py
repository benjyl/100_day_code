from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack() # what creates label on screen - layout of component

# methods for changing labels
my_label["text"] = "New Text"
my_label.config(text="Even newer text")

def button_clicked():
    output = input.get()
    message = "clicked"
    print(message)
    my_label["text"] = output
    
#Entry
input = Entry(width=10)
input.pack()
 
button = Button(text="Click me", command=button_clicked)
button.pack()





window.mainloop() # at end of script, everything else want to add in to window comes first