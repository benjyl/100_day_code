from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
#---------------------------------Reading csv------------------------
data = pd.read_csv("./data/french_words.csv")
data = data.to_dict("records")

#------------------------------display new word----------------------
def new_word():
    word = random.choice(data)
    front_word = word["French"]
    canvas.itemconfig(canvas_title, text="French")
    canvas.itemconfig(canvas_word, text=front_word)    

#----------------------------------UI Setup--------------------------
frame = Tk()
frame.title("Flash cards")
frame.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=background_img)

# add text to canvas
canvas_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# tick button
tick = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick, bg=BACKGROUND_COLOR, command=new_word)
tick_button.grid(column=1, row=1)

# cross button
cross = PhotoImage(file="./images/wrong.png")
tick_button = Button(image=cross, bg=BACKGROUND_COLOR, command=new_word)
tick_button.grid(column=0, row=1)

frame.mainloop()
