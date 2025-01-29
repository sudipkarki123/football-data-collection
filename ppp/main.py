import turtle
screen = turtle.Screen()
screen.title("Square by Turtle")
square_turtle = turtle.Turtle()
def draw_square(turtle, side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
draw_square(square_turtle, 100)
square_turtle.hideturtle()
turtle.done()