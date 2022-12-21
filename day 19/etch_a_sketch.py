from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    
def move_back():
    tim.back(10)
    
def clockwise():
    tim.right(10)
    
def anticlockwise():
    tim.left(10)
    
def clear_screen():
    # tim.clear()
    tim.reset()
    

screen.listen()
# # waiting for space key before calling move_forward()
# screen.onkey(fun=move_forward, key="space") # higher order function, using function as input to another

screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_back, key="s")
screen.onkeypress(fun=clockwise, key="d")
screen.onkeypress(fun=anticlockwise, key="a")
screen.onkey(fun=clear_screen, key="c")



screen.exitonclick()