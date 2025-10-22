import turtle
import math

# Set up
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
screen.title("Pattern 2")
t.pensize(2)
t.color("cyan")
d = 10

# Draw pattern
for _ in range(100):
    t.forward(d)
    d = d+5
    t.left(90)

# Finish
t.hideturtle()
turtle.done()