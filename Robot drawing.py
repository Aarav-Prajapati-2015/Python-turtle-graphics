import turtle

# Set up
t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)
screen.bgcolor("lightblue")
screen.title("Robot Drawing")

#Draw head
t.fillcolor("gray")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# Go to left eye
t.penup()
t.forward(25)
t.left(90)
t.forward(75)
t.pendown()

# Draw left eye
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.forward(20)
    t.right(90)
t.end_fill()

# Go to right eye
t.penup()
t.right(90)
t.forward(60)
t.left(90)
t.pendown()

# Draw right eye
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.forward(20)
    t.left(90)
t.end_fill()

# Finish left eye
t.penup()
t.forward(10)
t.left(90)
t.forward(10)
t.pensize(5)
t.pencolor("black")
t.pendown()
t.dot()

# Finish right eye
t.penup()
t.forward(40)
t.pendown()
t.dot()

# Go to mouth
t.penup()
t.left(90)
t.forward(60)
t.left(90)
t.pencolor("white")
t.pendown()

# Draw mouth
t.forward(50)

# Go to Neck
t.penup()
t.right(90)
t.forward(25)
t.right(90)
t.forward(20)
t.left(90)
t.color("black")
t.pensize(1)
t.pendown()

# Draw Neck
t.fillcolor("gray")
t.begin_fill()
for _ in range(2):
    t.forward(25)
    t.right(90)
    t.forward(20)
    t.right(90)
t.forward(25)
t.right(90)    
t.end_fill()

# Draw arms
t.fillcolor("yellow")
t.begin_fill()
t.forward(100)    
t.left(90)
t.forward(20)
t.left(90)
t.forward(180)
t.left(90)
t.forward(20)
t.left(90)
t.forward(100)
t.end_fill()

# Draw Hands
t.fillcolor("grey")
t.begin_fill()
t.forward(60)
t.left(90)
t.forward(20)
t.left(90)
t.forward(140)
t.left(90)
t.forward(20)
t.left(90)
t.end_fill()

# Go to the body
t.penup()
t.forward(160)
t.left(90)
t.forward(20)
t.left(90)
t.forward(50)
t.right(90)
t.pendown()

# Draw body
t.fillcolor("grey")
t.begin_fill()
for _ in range(2):
    t.forward(110)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

# Draw left leg
t.fillcolor("grey")
t.begin_fill()
t.forward(180)
t.left(90)
t.forward(20)
t.left(90)  
t.forward(70)
t.end_fill()

# Go to right leg
t.penup()   
t.right(90)
t.forward(40)
t.right(90)
t.pendown()

# Draw right leg
t.fillcolor("grey")
t.begin_fill()
for _ in range(2):
    t.forward(70)
    t.left(90)
    t.forward(20)
    t.left(90)
t.end_fill()

# Finish
t.hideturtle()
turtle.done()