import turtle 
import os
import pandas as pd

pwd = os.getcwd()+"/day 25/us-states-game-start/"
print(pwd)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./day 25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.pu()
pen.hideturtle()

# # to get coords of point on screen when click mouse
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

score = 0 # keep track of user states guessed correctly 
data = pd.read_csv(pwd+"50_states.csv")
correct_guesses = []

while len(correct_guesses) <50:   
     
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States guessed correctly", prompt="What's the name of another state?").title()
    
    if answer_state == "Exit":
        states_missed = data[~data.state.isin(correct_guesses)]
        states_missed.to_csv("./day 25/us-states-game-start/states_to_learn.csv")
        break
    
    if answer_state in data["state"].unique() and answer_state not in correct_guesses: # could also turn data["state"] into list
        x = int(data[data["state"] == answer_state].x) # x coord of state
        y = int(data[data["state"] == answer_state].y) # y coord of state
        pen.goto(x=x, y=y)
        pen.write(answer_state)
        correct_guesses.append(answer_state)
        # print(correct_guesses)
        
    elif answer_state in data["state"].unique() and answer_state in correct_guesses:
        print("already guessed")

