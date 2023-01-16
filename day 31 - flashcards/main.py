from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
#---------------------------------Reading csv------------------------
data = pd.read_csv("./data/french_words.csv")
to_learn = data.to_dict("records")

#------------------------------display new word----------------------
def new_word():
    
    word = random.choice(to_learn) # gets random French word + translation
    front_word = word["French"]
    back_word = word["English"]
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(canvas_title, text="French",font=("Arial", 40, "italic"), fill="black")
    canvas.itemconfig(canvas_word, text=front_word, font=("Arial", 60, "bold"), fill="black")
    reverse = canvas.after(3000, reverse_card, back_word)
    # canvas.after_cancel(reverse)

def reverse_card(english):
    canvas.itemconfig(canvas_img, image=back_image)
    # canvas_title = canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"), fill="white")
    # canvas_word = canvas.create_text(400, 263, text=english, font=("Arial", 60, "bold"), fill="white")
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=english, fill="white")
    
    
    

#----------------------------------UI Setup--------------------------
frame = Tk()
frame.title("Flash cards")
frame.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)

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
