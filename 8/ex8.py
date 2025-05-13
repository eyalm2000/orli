import turtle
import time

screen = turtle.Screen()
screen.setup(width=1000, height=500)

# orli - you dont need to download all the images manually, just clone the repo by opening a terminal and running:
# cd cd %USERPROFILE%/Downloads
# git clone https://github.com/eyalm2000/orli.git
# (make sure git is installed)
# then, run
# cd orli/8
# python ex8.py

for i in range(9):
    screen.addshape(f'images/steve{i}.gif')


turtle1 = turtle.Turtle()
turtle1.shape('images/steve0.gif')
turtle1.penup()
turtle1.imagecount = 0

turtle2 = turtle.Turtle()
turtle2.shape('images/steve0.gif')
turtle2.penup()
turtle2.imagecount = 0
turtle2.goto(500, 0)

turtle1.goto(-500, 0)

turtletext = turtle.Turtle()
turtletext.hideturtle()
turtletext.penup()

def change_image(turtlenumber):
    if turtlenumber.shape() != 'images/steve8.gif':
        turtlenumber.shape(f'images/steve{turtlenumber.imagecount}.gif')
        turtlenumber.imagecount += 1
    else:
        turtlenumber.shape('images/steve0.gif')
        turtlenumber.imagecount = 0
    x = turtlenumber.xcor() + (10 if turtlenumber == turtle1 else -10)  
    turtlenumber.goto(x, turtlenumber.ycor())
    time.sleep(0.02)

count = 0   

while True:
    change_image(turtle1)
    change_image(turtle2)
    if turtle2.xcor() == 100:
        turtletext.goto(50, 150)
        turtletext.write("hi! i'm steve!", font=("Arial", 16))
        turtletext.color('blue')
        time.sleep(3)
        turtletext.hideturtle()
        turtletext.goto(-200, 150)
        turtletext.write("hi! I'm steve too! that's cool!", font=("Arial", 16))
        turtle.done()
