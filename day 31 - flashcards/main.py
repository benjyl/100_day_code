from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------------Reading csv------------------------
# check if words_to_learn file exists and if so, save to data otherwise use the french_words.csv
try:
    data = pd.read_csv("./data/words_to_learn.csv")
    to_learn = data.to_dict("records")
    print("Success")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
    to_learn = data.to_dict("records")
    print("fail")

current_card = {}
# ------------------------------display new word----------------------
def new_word():
    global current_card, flip_timer  # allows me to update current card so stored for use in other functions

    frame.after_cancel(flip_timer)
    current_card = random.choice(to_learn)  # gets random French word + translation
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(
        canvas_title, text="French", font=("Arial", 40, "italic"), fill="black"
    )
    canvas.itemconfig(
        canvas_word,
        text=current_card["French"],
        font=("Arial", 60, "bold"),
        fill="black",
    )
    #
    flip_timer = canvas.after(3000, func=reverse_card)


def reverse_card():
    # get error when start and wait more than 3s, no english in dictionary yet so check for key error and do nothing
    try:
        canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")
    except KeyError:
        pass
    else:
        canvas.itemconfig(canvas_img, image=back_image)
        canvas.itemconfig(canvas_title, text="English", fill="white")


def known():
    try:
        to_learn.remove(current_card)
        data = pd.DataFrame(to_learn)
        data.to_csv("./data/words_to_learn.csv", index=False, encoding="utf-8-sig")
        new_word()
    except (ValueError):
        new_word()


# ----------------------------------UI Setup--------------------------
frame = Tk()
frame.title("Flash cards")
frame.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = frame.after(
    3000, func=reverse_card
)  # required so can use after_cancel at start of each new word run

# canvas image background setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")  # background for french
back_image = PhotoImage(file="./images/card_back.png")  # background for english
canvas_img = canvas.create_image(400, 263, image=front_img)  # canvas image

# add text to canvas
canvas_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# tick button
tick = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick, bg=BACKGROUND_COLOR, command=known)
tick_button.grid(column=1, row=1)

# cross button
cross = PhotoImage(file="./images/wrong.png")
tick_button = Button(image=cross, bg=BACKGROUND_COLOR, command=new_word)
tick_button.grid(column=0, row=1)

new_word()


frame.mainloop()
