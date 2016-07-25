import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor ("black")
    #Create the turtle Brad - Draws a square
    flower = turtle.Turtle()
    flower.shape("arrow")
    flower.color("red")
    flower.speed(10)
    draw.ellipse(flower)
    for i in range(1,37):
        draw_square(flower)
        flower.right(10)

    window.exitonclick()

draw_art()