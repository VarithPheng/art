import turtle

def draw_crown(t, x, y, scale=1):
    t.penup()
    t.goto(x - (37.5 * scale), y + (48 * scale))
    t.pendown()
    t.setheading(0)
    
    # Set crown color to yellow
    t.pencolor("gold")
    t.fillcolor("yellow")
    
    # Draw and fill the rectangular base
    t.begin_fill()
    for _ in range(2):
        t.forward(75 * scale)
        t.left(90)
        t.forward(12.5 * scale)
        t.left(90)
    t.end_fill()

    # Draw and fill the peaks without bottom lines
    peak_positions = [-37.5, -12.5, 12.5]
    for peak_x in peak_positions:
        t.penup()
        t.goto(x + (peak_x * scale), y + (60.5 * scale))
        t.pendown()
        t.begin_fill()
        t.setheading(60)
        t.forward(25 * scale)
        t.right(120)
        t.forward(25 * scale)
        t.end_fill()

    t.hideturtle()

# ... rest of the code remains unchanged ...
    
def draw_stickman(x, y, scale=1.2, winner=False):
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw head
    t.circle(24 * scale)
    
    # Draw body
    t.right(90)
    t.forward(72 * scale)
    
    # Draw legs
    t.right(30)
    t.forward(48 * scale)
    t.backward(48 * scale)
    t.left(60)
    t.forward(48 * scale)
    t.backward(48 * scale)
    t.right(30)
    
    # Draw arms
    t.backward(36 * scale)
    t.left(60)
    if winner:
        t.left(60)  # Raise the arm for the winner
    t.forward(48 * scale)
    t.backward(48 * scale)
    t.right(120)
    if winner:
        t.right(60)  # Adjust angle for the second arm
    t.forward(48 * scale)
    if winner:
        draw_crown(t, x, y, scale * 1.3)
    
    t.hideturtle()

def draw_chess_table(x, y, scale=1.2):
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    table_size = 96 * scale
    # Draw table outline
    for _ in range(4):
        t.forward(table_size)
        t.left(90)
    
    # Draw checkered pattern
    square_size = 12 * scale
    for i in range(8):
        for j in range(8):
            t.penup()
            t.goto(x + i * square_size, y + j * square_size)
            t.pendown()
            if (i + j) % 2 == 0:
                t.fillcolor("white")
            else:
                t.fillcolor("black")
            t.begin_fill()
            for _ in range(4):
                t.forward(square_size)
                t.left(90)
            t.end_fill()
    
    t.hideturtle()

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 480)
screen.title("Stickman Chess - Player 1 Wins")

# Disable animation
screen.tracer(0)

# Draw chess table
draw_chess_table(-48, -144)

# Draw stickmen
draw_stickman(-180, -60, scale=1, winner=True)
draw_stickman(180, -60, scale=1)

# Update the screen to show drawings
screen.update()

# Keep the window open
turtle.done()