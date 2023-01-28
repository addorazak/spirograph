import turtle
from turtle import Turtle, Screen
import random

raz = Turtle()
screen = Screen()
screen.bgcolor('black')

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = r, g, b
    return color


tim = Turtle()
tim.speed('fastest')


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(int(input("Enter the size  of gap you want in your spirograph: ")))


screen.exitonclick()
