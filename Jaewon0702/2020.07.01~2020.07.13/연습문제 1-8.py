import turtle
import random


##함수 선언##
def screenMC(x,y) :
    global r,g,b
    turtle.penup()
    turtle.goto(x,y)
    tsize=random.randrange(1,10)
    turtle.shapesize(tsize)
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.color(r,g,b)
    turtle.stamp()


##변수 선언##
r,g,b=0.0,0.0,0.0

##main code##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')

turtle.onscreenclick(screenMC,1)

turtle.done()
