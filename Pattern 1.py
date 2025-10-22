import turtle
import math

# Set up
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
screen.title("Pattern 1")
t.pensize(2)
t.color("cyan")
d = 10

# Draw pattern
for _ in range(55):
    t.circle(d,90)
    d = d + 5

# Finish
t.hideturtle()
turtle.done()    