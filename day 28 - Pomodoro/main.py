from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
#hex codes from https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(row=0, column=1)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #highlightthickness sets thickness of border around canvas
filename = PhotoImage(file="tomato.png") # reads through a file and gets hold of particular image at particular file loc
canvas.create_image(100, 112, image=filename) # image cut off when using x = 100, so if move to right slightly (103), see whole tomato 
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

#start button
start = Button(text="Start")
start.grid(row=2, column=0)

# reset button
reset = Button(text="Reset")
reset.grid(row=2, column=2)

# tick mark
tick_labels= Label(text="✔", fg=GREEN, bg=YELLOW)
tick_labels.grid(row=3, column=1)




window.mainloop()
