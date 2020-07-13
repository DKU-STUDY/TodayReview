import turtle

##변수 선언##
num=0
swidth,sheight=1000,300
curX,curY=0,0

## main code part ##

turtle.title("거북이로 2진수 표현하기")
turtle.shape('turtle')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.left(90)

num=int(input("숫자를 입력하세요 : "))
binary=bin(num)
curX=swidth/2
curY=0
for i in range(len(binary)-2) :
    turtle.goto(curX,curY)
    if num&1 :
        turtle.color('red')
        turtle.turtlesize(2)
    else :
        turtle.color('blue')
        turtle.turtlesize(1)

    turtle.stamp()
    curX-=50
    num>>=1

turtle.done()
