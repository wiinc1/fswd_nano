import turtle

def draw_square(turtle_up):
    turtle_up.color("grey")
    for i in range(1,5):
        turtle_up.forward(100)
        turtle_up.right(80)

def draw_art():
    window = turtle.Screen()
    window.bgcolor ("black")
    brian = turtle.Turtle()
    brian.shape("turtle")
    brian.speed(25)
    for i in range(1,26):
        draw_square(brian)
        brian.right(10)

    window.exitonclick()

draw_art()
