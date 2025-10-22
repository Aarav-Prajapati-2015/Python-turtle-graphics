import turtle

# Set up
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
t.speed(0)
screen.title("Flower Drawing")

 # Draw stem
t.pensize(10)
t.color("green")
t.right(90)
t.forward(200)
    
# Draw flower
t.pensize(2)
t.penup()
t.goto(0, 0)
t.pendown()
t.color("red", "yellow")
for _ in range(12):    
    t.begin_fill()
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(150)
    t.end_fill()    

# Finish
t.hideturtle()
turtle.done()