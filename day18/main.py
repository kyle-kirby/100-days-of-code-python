# Takes the color palette from a .jpg and recreates a "Hirst" painting utilizing the Turtle library
import turtle
from turtle import Turtle,Screen
import random


def turn_left():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)


def turn_right():
    tim.penup()
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(50)

def stamp():
    for _ in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()


turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.hideturtle()
tim.speed(0)
colors_list = [(226, 231, 236), (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230)]

tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)
tim.pendown()

for _ in range(5):
    stamp()
    turn_left()
    stamp()
    turn_right()

screen = Screen()
screen.exitonclick()
