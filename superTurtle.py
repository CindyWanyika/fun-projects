import turtle

# Create the screen
screen = turtle.Screen()
screen.title("Turtle Grid Environment")
screen.bgcolor("white")

# Create a turtle for drawing the grid
grid_turtle = turtle.Turtle()
grid_turtle.speed(0)
grid_turtle.penup()
grid_turtle.hideturtle()

# Draw the grid
cell_size = 50  # Size of each cell in the grid
grid_size = 10  # Number of cells (10x10 grid)

for x in range(-grid_size * cell_size // 2, grid_size * cell_size // 2 + 1, cell_size):
    grid_turtle.goto(x, -grid_size * cell_size // 2)
    grid_turtle.pendown()
    grid_turtle.goto(x, grid_size * cell_size // 2)
    grid_turtle.penup()

for y in range(-grid_size * cell_size // 2, grid_size * cell_size // 2 + 1, cell_size):
    grid_turtle.goto(-grid_size * cell_size // 2, y)
    grid_turtle.pendown()
    grid_turtle.goto(grid_size * cell_size // 2, y)
    grid_turtle.penup()

# Create the main turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# Move the turtle within the grid
t.penup()
t.goto(0, 0)  # Start at the center of the grid

# Control the turtle's movement within the grid
def move_up():
    t.setheading(90)  # Face upward
    t.forward(cell_size)

def move_down():
    t.setheading(270)  # Face downward
    t.forward(cell_size)

def move_left():
    t.setheading(180)  # Face left
    t.forward(cell_size)

def move_right():
    t.setheading(0)  # Face right
    t.forward(cell_size)

# Bind keys to control the turtle
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

turtle.done()
