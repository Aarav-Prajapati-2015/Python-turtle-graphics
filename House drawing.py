import turtle
# setup
t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)
screen.title("House Drawing")
# Draw a square

t.fillcolor("light blue")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.penup()
t.right(90)
t.forward(100)
t.left(90)  
t.forward(40)
t.left(90)
t.pendown()

# Draw a rectangle
t.fillcolor("brown")
t.begin_fill()
t.forward(35)
t.right(90)
t.forward(25)
t.right(90)
t.forward(35)
t.end_fill()

t.penup()
t.left(180)
t.forward(100)
t.left(90)
t.forward(65)
t.right(130)

# Draw a triangle
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.forward(80)
t.right(100)
t.forward(80)
t.end_fill()

# Finish
t.hideturtle()
screen.exitonclick()