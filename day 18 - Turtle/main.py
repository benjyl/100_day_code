from turtle import Turtle, Screen
import random as rd

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("red")

# #create 100 by 100 square
# for i in range(4):
#     tim.fd(100)
#     tim.right(90)
# tim.pu()
# tim.setx(-50)
# draw dashed line
# for i in range(15):
#     tim.pd()
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)

def draw_shape(sides):
    angle = 360/sides
    for j in range(sides):
        tim.fd(100)
        tim.right(angle)

def random_walk():
    """randomly choose direction of travel and move forward 20
    """
    angles = [0, 90, 180, 270]
    tim.fd(20)
    tim.setheading(rd.choice(angles))

def random_colour():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r,g,b)


screen.colormode(255) # sets colour RGB to between 0 an 255
'''
# create shapes triangle to decagon in random colors
sides = 3
while sides <=10:
    tim.pencolor(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
    draw_shape(sides)
    sides+=1
'''

'''
tim.speed(0) # 0 = fastest, else, 1-10 goes from slow to fast
tim.pensize(10)
# colour = random_colour()
while True:
    
    tim.pencolor(random_colour()) # generate random colour
    random_walk()
'''
tim.speed(0)
# Generate multiple circles at tilts

stepsize = 5
def draw_spirograph(step):
    for i in range(int(360/stepsize)):
        tim.pencolor(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + step)

draw_spirograph(5)
screen.exitonclick()