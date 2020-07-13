import turtle
import random

##함수선언부분##

def screenLC(x,y) :
    global r,g,b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

    tsize=random.randrange(1,10)
    turtle.shapesize(tsize)
    r=random.random()
    g=random.random()
    b=random.random()

def screenRC(x,y) :
    turtle.penup()
    turtle.goto(x,y)

def screenMC(x,y) :
    global r,g,b
    tsize=random.randrange(1,10)
    turtle.shapesize(tsize)
    r=random.random()
    g=random.random()
    b=random.random()

##변수 선언 부분##

psize=10
r,g,b=0.0,0.0,0.0

##main code part##
turtle.title('거북이로 그림 그리기')
turtle.shape('triangle')
turtle.pensize(psize)

turtle.onscreenclick(screenLC,1)
turtle.onscreenclick(screenRC,3)

turtle.done()

