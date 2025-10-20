import turtle 

# Setup
t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)
screen.title("Face Drawing")

# Draw face out line
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# go to left eye
t.penup()
t.left(90)
t.forward(145)
t.left(90)
t.forward(40)
t.pendown()

# Draw left eye
t.fillcolor("black")
t.begin_fill()
t.circle(15)
t.end_fill()

# Go to right eye
t.penup()
t.right(180)
t.forward(80)
t.pendown()

# Draw right eye
t.fillcolor("black")
t.begin_fill()
t.right(180)
t.circle(15)
t.end_fill()

# Go to nose
t.penup()
t.forward(40)
t.right(90)
t.backward(60)
t.right(180)
t.pendown()

# Draw nose
t.color("black")
t.pensize(5)
t.forward(25)

# Go to mouth
t.penup()
t.forward(35)
t.pendown()

# Draw mouth
t.right(90)
t.forward(35)
t.right(180)
t.forward(70)

# Finish
t.hideturtle()
screen.exitonclick()