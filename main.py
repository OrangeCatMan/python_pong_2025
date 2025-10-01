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
ball.turtlesize(0.5)
midLine.left(90)
rPaddle.left(90)
lPaddle.left(90)
midLine.width(10)
screen.delay(0)
screen.delay()
turtle.tracer(0)
rPaddle.fillcolor('white')
lPaddle.fillcolor('white')
midLine.penup()
midLine.goto(0,-380)
tele(lPaddle, -370, -35)
tele(rPaddle, 370,-35)
ball.fillcolor("white")

bVelX = 2
bVelY = -2


rpX = 0
rpY = 0

win = False

def move(tutel, addX, addY):
    tele(tutel, (tutel).xcor() + addX, (tutel).ycor() + addY)


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
    rPaddle.goto(rPaddle.xcor(), rPaddle.ycor() + 70)
    rPaddle.goto(rPaddle.xcor() - 10, rPaddle.ycor())
    rPaddle.goto(rPaddle.xcor(), rPaddle.ycor() - 70)
    rPaddle.goto(rPaddle.xcor() + 10, rPaddle.ycor())
    rPaddle.end_fill()

def rPaddleUp():
    move(rPaddle, 0, 0.5)

def rPaddleDown():
    move(rPaddle, 0, -0.5)

def lPaddleUp():
    move(lPaddle, 0, 0.5)

def lPaddleDown():
    move(lPaddle, 0, -0.5)

def ballUpdate(bVelX, bVelY):
    if ball.xcor() >= (rPaddle.xcor() - 20) and (ball.ycor() <= (rPaddle.ycor() + 70) and ball.ycor() >= rPaddle.ycor()):
        middle = (rPaddle.ycor() + 35)
        bVelY = (ball.ycor() - middle)/100
        bVelX *= -1
    else:
        if ball.ycor() >= 390 or ball.ycor() <= -390:
            bVelY *= -1
        if ball.xcor() >= 390 or ball.xcor() <= -390:
            bVelX *= -1
    move(ball, bVelX, bVelY)
    return(bVelX, bVelY)



def main():
    bVelX = 0.25
    bVelY = 0
    x = 0
    y = 0
    while win != True:
        x += 1
        if x == 1200:
            x = 0
            y += 1
            print(y)
        bVelX, bVelY = ballUpdate(bVelX, bVelY)

        if keyboard.is_pressed('up'):
            if (rPaddle.ycor() + 70) < 398:
                rPaddleUp()
            else:
                move(rPaddle, 0, -2)

        if keyboard.is_pressed('down'):
            if (rPaddle.ycor() ) > -398:
                rPaddleDown()
            else:
                move(rPaddle, 0, 2)

        if keyboard.is_pressed('w'):
            if (lPaddle.ycor() + 70) < 398:
                lPaddleUp()
            else:
                move(lPaddle, 0, -2)

        if keyboard.is_pressed('s'):
            if (lPaddle.ycor() ) > -398:
                lPaddleDown()
            else:
                move(lPaddle, 0, 2)
        rPaddleDraw()
        lPaddleDraw()
        turtle.update()




main()
