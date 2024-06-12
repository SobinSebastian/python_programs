import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Circle with Turtle")
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# Set the speed of the turtle
t.speed(1)  # 1 is the slowest, 10 is the fastest

# Draw a circle with radius 100
t.circle(100)

# Hide the turtle after drawing
t.hideturtle()

# Finish drawing
turtle.done()
