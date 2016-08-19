import turtle

def draw_square(turtle):
    turtle.color("grey")
    for i in range(1,5):
        turtle.forward(100)
        turtle.right(90)

def draw_stem(turtle):
    turtle.color("red")
    turtle.pensize(5)
    turtle.setheading(270)
    turtle.forward(250)

def draw_art():
    window = turtle.Screen()
    window.bgcolor ("black")
    brian = turtle.Turtle()
    brian.shape("turtle")
    brian.speed(200)
    for i in range(1,36):
        draw_square(brian)
        brian.right(10)

    draw_stem(turtle)
    window.exitonclick()

draw_art()