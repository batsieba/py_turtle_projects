import random
from turtle import Turtle, Screen, colormode
from random import randint

# ------------------The shape builder ----------------------
# def draw_shape(sides):
#     """this function draws shapes based on the number of sides"""
#     angle = 360 / sides
#     for i in range(sides):
#         tim.forward(100)
#         tim.right(angle)

# # sides 3 to 8 shapes
# tim = Turtle()
# colormode(255)
# tim.speed("fastest")
# i = 3
# while i <= 8:
#     tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     draw_shape(i)
#     i += 1
#

# ------------------------The Random Walk challenge----------------------------
# def walk():
#     """this function walks in some random direction"""
#     direction = [0, 90, 180, 270]
#     tim.forward(50)
#     wid_size = 3
#     tim.width(wid_size)
#     tim.setheading(random.choice(direction))
#     wid_size += 1
#
#
# def random_color():
#     return tim.color(randint(0, 255), randint(0, 255), randint(0, 255))

#
# tim = Turtle()
# colormode(255)
# tim.speed("fastest")
# start = 0
# while start <= 90:
#     random_color()
#     walk()
#     start += 1
#

# -------------------Make a spirograph-------------------------------
# def random_color():
#    return tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
#
#
# tim = Turtle()
# colormode(255)
# tim.speed("fastest")
# # tim.pensize(10)
#
#
# def draw_spirograph(size):
#     """draws a spirograph"""
#     for i in range(int(360/size)):
#         random_color()
#         tim.circle(100)
#         tim.setheading(tim.heading() + size)
#
# draw_spirograph(5)


# ------------ small circles in 7 rows ---------------

def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def filled_circles(radius):
    """draws a filled circle"""
    ran_col = random_color()
    tim.color(ran_col)
    tim.fillcolor(ran_col)
    tim.begin_fill()
    tim.circle(radius)
    tim.end_fill()
    tim.penup()


tim = Turtle()
colormode(255)
tim.speed("fastest")

circle_radius = 15
x = 0
y = 0
for i in range(7):
    for j in range(12):
        filled_circles(circle_radius)
        tim.setx(x)
        tim.sety(y)
        tim.pendown()
        x += circle_radius * 3
    x = 0
    y -= circle_radius * 3
    filled_circles(circle_radius)


screen = Screen()
screen.exitonclick()