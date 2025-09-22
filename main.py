import tkinter as tk
import turtle
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
ball.ht()
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
tele(rPaddle, -370, 0)
tele(lPaddle, 370,-35)




def move(tutel, addX, addY):
    tele(tutel, (tutel).xcor() + 1, (tutel).ycor() + 1)


#midline draw'er
for i in range(20):
    midLine.pendown()
    midLine.forward(10)
    midLine.penup()
    midLine.forward(30)

#left paddle setup

def lPaddle_setup():
    lPaddle.begin_fill()
    for i in range(2):
        rPaddle.forward(70)
        rPaddle.left(90)
        rPaddle.forward(10)
        rPaddle.left(90)
    lPaddle.end_fill()

def rPaddle_setup():
    rPaddle.begin_fill()
    for i in range(2):
        rPaddle.forward(70)
        rPaddle.left(90)
        rPaddle.forward(10)
        rPaddle.left(90)
    rPaddle.end_fill()

def main():
    lPaddle_setup()
    rPaddle_setup()
    
for i in range(10):
    rPaddle.clear()
    tele(rPaddle, rPaddle.xcor() + 5, rPaddle.ycor() + 5)
    for i in range(2):
        rPaddle.forward(70)
        rPaddle.left(90)
        rPaddle.forward(10)
        rPaddle.left(90)
    print(rPaddle.xcor())
main()