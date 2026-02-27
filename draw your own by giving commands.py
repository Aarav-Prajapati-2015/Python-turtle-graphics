import turtle
t = turtle.Turtle()


def draw_square():
    for i in range(4):
        t.forward(100)
        t.left(90)


def draw_triangle():
    for i in range(3):
        t.forward(100)
        t.left(120)


def draw_circle():
    t.circle(100)


def draw_rectangle():
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)


def draw_pentagoan():
    for i in range(5):
        t.forward(100)
        t.left(72)


def draw_hexagoan():
    for i in range(6):
        t.forward(100)
        t.left(60)


def draw_octagon():
    for i in range(8):
        t.forward(100)
        t.left(45)


def draw_nonagoan():
    for i in range (9):
        t.forward(100)
        t.left(40)


def draw_decagon():
    for i in range (10):
        t.forward(100)
        t.left(36)


def draw_robot():
    # Set up
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    t.speed(0)
    screen.title("Robot Drawing")

    # Draw head
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
        t.left(90)
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


def draw_stickman():
    # Setup
    screen = turtle.Screen()
    t.speed(0)
    screen.title("Sticky Man Drawing")
    screen.bgcolor("light blue")

    # Face 
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

    # Go to body
    t.penup()
    t.right(90)
    t.forward(23)
    t.right(90)
    t.forward(32)
    t.left(90)
    t.pendown()

    # Draw body
    t.forward(200)

    # Draw legs
    t.right(30)
    t.forward(100)
    t.backward(100)
    t.left(60)
    t.forward(100)
    t.backward(100)
    t.right(210)

    # Go to arms
    t.penup()
    t.forward(150)
    t.right(70)
    t.pendown()

    # Draw arms
    t.forward(100)
    t.backward(100)
    t.left(140)
    t.forward(100)
    t.backward(100)


def draw_house():
    # setup
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

def draw_face():
    # Setup
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

i = input("Tell me what you have to draw ("
"square, robot, stickman, house, face, triangle, circle, rectangle, pentagon, hexagon, octagon, nonagon, decagon): ")
if i == "square":
    draw_square()
elif i == "robot":
    draw_robot()
elif i == "stickman":
    draw_stickman()
elif i == "house":
    draw_house()
elif i == "face":
    draw_face()
elif i == "triangle":
    draw_triangle()
elif i == "circle":
    draw_circle()
elif i == "rectangle":
    draw_rectangle()
elif i == "pentagon":
    draw_pentagoan()
elif i == "hexagon":
    draw_hexagoan()
elif i == "octagon":
    draw_octagon()
elif i == "nonagon":
    draw_nonagoan()
elif i == "decagon":
    draw_decagon()        

    
    
turtle.done()    