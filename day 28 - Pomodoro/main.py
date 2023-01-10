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
reps = 0
timer = None # global timer variable, set up in count_down and reset in timer reset

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    # Reset timer to go back to no 00:00 and no ticks
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    tick_labels.config(text="")
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_secs = WORK_MIN*60
    short_break_secs = SHORT_BREAK_MIN*60
    long_break_secs = LONG_BREAK_MIN*60

    if reps%2 != 0:
        count_down(int(work_secs))
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(int(long_break_secs))
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(int(short_break_secs))
        timer_label.config(text="Break", fg=PINK)

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# GUI event driven, uses window.mainloop, so if tried using time module and creating
#  while loop to count down every second, will never reach mainloop and GUI never launches

# .after() has *args so any input after function is passed to the function
def count_down(count):
    mins = count//60
    secs = count%60
    canvas.itemconfig(timer_text, text=f"{mins:0>2d}:{secs:0>2d}")
    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1) 
    else:
        start_timer()
        tick_labels.config(text=int((reps)/2)* "✔") # add tick for every work session completed
    
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
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

#start button
start = Button(text="Start",command=start_timer)
start.grid(row=2, column=0)

# reset button
reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

# tick mark
tick_labels= Label(fg=GREEN, bg=YELLOW)
tick_labels.grid(row=3, column=1)




window.mainloop()
