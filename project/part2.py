import turtle
import random

screen = turtle.Screen()
screen.setup(width=1000, height=500)

screen.addshape('media/paper.gif')
screen.addshape('media/rock.gif')
screen.addshape('media/scissors.gif')
screen.addshape('media/replace.gif')

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
replace = turtle.Turtle()

turtle1.penup()
turtle2.penup()
replace.penup()

replace.goto(0, -200)
replace.shape('media/replace.gif')

turtle1.goto(-200, 0)
turtle2.goto(200, 0)

def choose_shape(turtlenumber):
    turtlenumber.shapename = (random.choice(['media/paper.gif', 'media/rock.gif', 'media/scissors.gif']))
    turtlenumber.shape(turtlenumber.shapename)

def button_click(x, y):
        choose_shape(turtle1)
        choose_shape(turtle2)

choose_shape(turtle1)
choose_shape(turtle2)

replace.onclick(button_click)

turtle.done()