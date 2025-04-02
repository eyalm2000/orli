import turtle
import time

# clone the repo
# git clone https://github.com/eyalm2000/orli.git
repoPath = r"C:\Users\user\repos\orli" # change this to your repo path

screen = turtle.Screen()
screen.setup(1000, 1000)

imageList = [f'{repoPath}/7/images/{i}.gif' for i in range(1, 9)]

for image in imageList:
    screen.addshape(image)

turtle1 = turtle.Turtle()
turtle1.shape(imageList[0])
turtle1.penup()

imageIndex = 0

def changeImage():
    global imageIndex
    turtle1.shape(imageList[imageIndex])
    imageIndex = (imageIndex + 1) % len(imageList)

def moveTurtle(x):
    if turtle1.xcor() == 500:
        turtle1.hideturtle()
        turtle1.speed(0)
        turtle1.setx(-500)
        turtle1.showturtle()
    else:
        turtle1.goto(turtle1.xcor() + x, 0)

while True:
    changeImage()
    moveTurtle(20)
    time.sleep(0.1)