import turtle
import random
import time

screen = turtle.Screen()
screen.setup(width=1000, height=500)

screen.addshape('media/paper.gif')
screen.addshape('media/rock.gif')
screen.addshape('media/scissors.gif')
screen.addshape('media/replace.gif')

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
replace = turtle.Turtle()
text = turtle.Turtle()

turtle1.hideturtle()
turtle2.hideturtle()
text.hideturtle()

turtle1.penup()
turtle2.penup()
replace.penup()
text.penup()

replace.goto(0, 0)
replace.shape('media/replace.gif')

turtle1.goto(-200, 0)
turtle2.goto(200, 0)

def choose_shape(turtlenumber):
    turtlenumber.shapename = (random.choice(['paper', 'rock', 'scissors']))
    turtlenumber.shape(f'media/{turtlenumber.shapename}.gif')
    turtlenumber.showturtle()

def choose_winner():
    if turtle1.shapename == turtle2.shapename:
        text.goto(0, 50)
        text.write("It's a tie.", font=("Comic Sans MS", 36), align="center")
    elif ((turtle1.shapename == 'rock') and (turtle2.shapename == 'scissors')) or \
         ((turtle1.shapename == 'scissors') and (turtle2.shapename == 'paper')) or \
         ((turtle1.shapename == 'paper') and (turtle2.shapename == 'rock')):
        text.goto(-200, 50)
        text.write(f'{turtle1.shapename} won!', font=("Comic Sans MS", 36), align="center")
    else:
        text.goto(200, 50)
        text.write(f'{turtle2.shapename} won!', font=("Comic Sans MS", 36), align="center")
    
    time.sleep(2)
    text.clear()


def button_click(x, y):
        choose_shape(turtle1)
        choose_shape(turtle2)
        choose_winner()


replace.onclick(button_click)

turtle.done()