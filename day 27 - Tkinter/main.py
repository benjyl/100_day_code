import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack() # what creates label on screen - layout of component


window.mainloop() # at end of script, everything else want to add in to window comes first