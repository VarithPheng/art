import turtle

def draw_stickman(x, y, scale=1.2):
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
    t.forward(48 * scale)
    t.backward(48 * scale)
    t.right(120)
    t.forward(48 * scale)
    t.hideturtle()

def draw_chess_table(x, y, scale=1.2):
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    table_size = 96 * scale  # Increased from 80
    # Draw table outline
    for _ in range(4):
        t.forward(table_size)
        t.left(90)
    
    # Draw checkered pattern
    square_size = 12 * scale  # Increased from 10
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
screen.setup(600, 480)  # Increased from 500, 400
screen.title("Stickmen Playing Chess")

# Draw stickmen and chess table
draw_stickman(-180, -60)  # Adjusted positions
draw_stickman(180, -60)
draw_chess_table(-48, -144)  # Adjusted position

# Keep the window open
turtle.done()