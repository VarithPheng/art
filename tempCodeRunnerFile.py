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