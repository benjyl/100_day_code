import colorgram
from turtle import Turtle, Screen, colormode
import random

# pwd = "c:/Users/btl/OneDrive - Cambridge Consultants/Training/Coding/100_day_code/day 18 - Turtle/hirst_painting/"

# colours = colorgram.extract(pwd+'image.jpg', 30)
# colour_list = []
# for colour in colours:
#     col = colour.rgb[:] # extract RGB tuple from RGB
#     colour_list.append(col)
# print(colour_list)

colour_list = [
    (212, 149, 95),
    (215, 80, 62),
    (47, 94, 142),
    (231, 218, 92),
    (148, 66, 91),
    (22, 27, 40),
    (155, 73, 60),
    (122, 167, 195),
    (40, 22, 29),
    (39, 19, 15),
    (209, 70, 89),
    (192, 140, 159),
    (39, 131, 91),
    (125, 179, 141),
    (75, 164, 96),
    (229, 169, 183),
    (15, 31, 22),
    (51, 55, 102),
    (233, 220, 12),
    (159, 177, 54),
    (99, 44, 63),
    (35, 164, 196),
    (234, 171, 162),
    (105, 44, 39),
    (164, 209, 187),
    (151, 206, 220),
]
tim = Turtle()
screen = Screen()
colormode(255)

tim.hideturtle()


def fill_row(y_coord, colour_list):
    tim.goto(-200, y_coord)
    for i in range(10):
        # tim.pd()
        tim.begin_fill()
        tim.dot(20, random.choice(colour_list))
        tim.end_fill
        # tim.pu()
        tim.fd(50)


tim.pu()
y = -200
tim.speed(0)
for i in range(10):
    fill_row(y, colour_list)
    y += 50


screen.exitonclick()
