import turtle
import random

swidth,sheight,psize,exitCount=300,300,3,0
r,g,b,angle,dist,curX,curY=[0]*7

turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(psize)
turtle.setup(width=swidth+30,height=sheight+30)
turtle.screensize(swidth,sheight)

while True :
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pencolor((r,g,b))

    angle=random.randrange(0,360)
    dist=random.randrange(1,100)
    turtle.left(angle)
    turtle.forward(dist)
    curX=turtle.xcor()
    curY=turtle.ycor()
    if (-swidth/2<=curX and curX<=swidth/2) and (-sheight<=curY and curY<=sheight/2) :
        pass
    else :
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        exitCount+=1
        if exitCount>=5 :
            break
turtle.done()
