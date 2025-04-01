import turtle

def ex6():
    turtle.speed(10000000)
    turtle.pensize(2)

    turtle.pencolor("blue")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()

    turtle.done()

ex6()
# ex6_2()