import tkinter as tk
import turtle
import keyboard
#USE .TELEPORT

#setup
screen = turtle.Screen()
turtle.setup(800,800)
turtle.bgcolor("black")
turtle.bgcolor()
lPaddle = turtle.Turtle()
rPaddle = turtle.Turtle()


def tele(tutel, x, y):
    (tutel).penup()
    (tutel).goto(x,y)
    (tutel).pendown()


ball = turtle.Turtle()
midLine = turtle.Turtle()
midLine.ht()
rPaddle.ht()
lPaddle.ht()
ball.shape("square")
midLine.pencolor('white')
midLine.pencolor()
lPaddle.pencolor('white')
lPaddle.pencolor()
rPaddle.pencolor('white')
rPaddle.pencolor()
ball.pencolor('white')
ball.pencolor()
midLine.left(90)
rPaddle.left(90)
lPaddle.left(90)
midLine.width(10)
screen.delay(0)
screen.delay()
rPaddle.fillcolor('white')
lPaddle.fillcolor('white')
midLine.penup()
midLine.goto(0,-380)
tele(lPaddle, -370, -35)
tele(rPaddle, 370,-35)

rpX = 0
rpY = 0

win = False

def move(tutel, addY):
    tele(tutel, (tutel).xcor(), (tutel).ycor() + addY)


#midline draw'er
for i in range(20):
    midLine.pendown()
    midLine.forward(10)
    midLine.penup()
    midLine.forward(30)

#left paddle setup

def lPaddleDraw():
    lPaddle.clear()
    lPaddle.begin_fill()
    lPaddle.goto(lPaddle.xcor(), lPaddle.ycor() + 70)
    lPaddle.goto(lPaddle.xcor() - 10, lPaddle.ycor())
    lPaddle.goto(lPaddle.xcor(), lPaddle.ycor() - 70)
    lPaddle.goto(lPaddle.xcor() + 10, lPaddle.ycor())
    lPaddle.end_fill()


def rPaddleDraw():
    rPaddle.clear()
    rPaddle.begin_fill()
    rpY = rPaddle.ycor()
    print(rpX)
    print(rpY)
    rPaddle.goto(rPaddle.xcor(), rPaddle.ycor() + 70)
    rPaddle.goto(rPaddle.xcor() - 10, rPaddle.ycor())
    rPaddle.goto(rPaddle.xcor(), rPaddle.ycor() - 70)
    rPaddle.goto(rPaddle.xcor() + 10, rPaddle.ycor())
    rPaddle.end_fill()

def rPaddleUp():
    move(rPaddle, 3)

def rPaddleDown():
    move(rPaddle, -3)

def lPaddleUp():
    move(lPaddle, 3)

def lPaddleDown():
    move(lPaddle, -3)

def main():
    while win != True:
        # screen.ontimer()
        if keyboard.is_pressed('up') and (rpY + 70) < 400:
            rPaddleUp()

        if keyboard.is_pressed('down'):
            rPaddleDown()

        if keyboard.is_pressed('w'):
            lPaddleUp()

        if keyboard.is_pressed('s'):
            lPaddleDown()
        rPaddleDraw()
        lPaddleDraw()





#for i in range(10):
#    rPaddleDraw()
#    tele(rPaddle, rPaddle.xcor() + 5, rPaddle.ycor() + 5)
main()