import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create a new turtle object
my_turtle = turtle.Turtle()
my_turtle.color("red")

# Move the turtle
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)

# Hide the turtle
my_turtle.hideturtle()

# Keep the window open
turtle.done()