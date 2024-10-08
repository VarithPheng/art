import turtle

def draw_stickman(x, y, scale=1.2, winner=False):
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed(0)  # Fastest drawing speed
    
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
    
    # Draw winner's crown if winner
    if winner:
        t.penup()
        t.goto(x - 24 * scale, y + 48 * scale)
        t.pendown()
        t.color("gold")
        for _ in range(3):
            t.forward(16 * scale)
            t.right(120)
    
    t.hideturtle()

def draw_chess_table(x, y, scale=1.2):
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
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

# Draw chess table
draw_chess_table(-48, -144)

# Draw stickmen
draw_stickman(-180, -60)  # First person wins with raised arm
draw_stickman(180, -60,winner=True)  # Second person loses

# Keep the window open
turtle.done()