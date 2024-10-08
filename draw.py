import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
crown = turtle.Turtle()
crown.speed(5)

# Function to draw one peak of the crown
def draw_peak():
    crown.left(60)
    crown.forward(100)
    crown.right(120)
    crown.forward(100)
    crown.left(60)

# Move turtle to starting position
crown.penup()
crown.goto(-150, 0)
crown.pendown()

# Draw the base of the crown
crown.forward(300)

# Draw three peaks
for _ in range(3):
    draw_peak()

# Draw the right side of the crown
crown.forward(100)

# Hide the turtle and display the result
crown.hideturtle()
turtle.done()
