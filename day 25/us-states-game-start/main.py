import turtle 
import os

pwd = os.getcwd()
print(pwd)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./day 25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # to get coords of point on screen when click mouse
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

answer_state = screen.textinput(title="Guess the State", prompt="What's the name of another state?")
print(answer_state)