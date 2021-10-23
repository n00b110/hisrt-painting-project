from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
screen.colormode(255)

colors_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209), (227, 173, 177), (68, 63, 58), (111, 140, 142), (255, 194, 0), (178, 196, 202)]

def hirst_draw(distance=50, size=20):
    dots = []
    angle = 90
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(-200, -200)
    for num in range(100):
        color = random.choice(colors_list)
        turtle.dot(size, color)
        turtle.penup()
        turtle.forward(50)
        dots.append(num)

        if len(dots) % 10 == 0:
            turtle.left(angle)
            turtle.forward(50)  # 10 is the number of dots in a row!
            turtle.left(angle)
            turtle.forward(distance*10)
            turtle.setheading(0)
            continue


hirst_draw()

screen.exitonclick()