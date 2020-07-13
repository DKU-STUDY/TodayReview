import turtle

##변수 선언##
num=0
swidth,sheight=1000,300
curX,curY=0,0

## main code part ##

turtle.title("거북이로 2진수의 비트곱 & 표현하기")
turtle.shape('turtle')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.left(90)

num1=int(input("첫 번째 숫자를 입력하세요 : "))
num2=int(input("두 번째 숫자를 입력하세요 : "))

multiply=num1&num2
binary1=bin(num1)
binary2=bin(num2)
bin_multiply=bin(multiply)

curX=swidth/2
curY=sheight/3
for i in range(len(binary1)-2) :
    turtle.goto(curX,curY)
    if num1&1 :
        turtle.color('red')
        turtle.turtlesize(2)
    else :
        turtle.color('blue')
        turtle.turtlesize(1)

    turtle.stamp()
    curX-=50
    num1>>=1

curX=swidth/2
curY=0

for i in range(len(binary2)-2) :
    turtle.goto(curX,curY)
    if num2&1 :
        turtle.color('red')
        turtle.turtlesize(2)
    else :
        turtle.color('blue')
        turtle.turtlesize(1)

    turtle.stamp()
    curX-=50
    num2>>=1

curX=swidth/2
curY=-sheight/3

for i in range(len(bin_multiply)-2) :
    turtle.goto(curX,curY)
    if multiply&1 :
        turtle.color('red')
        turtle.turtlesize(2)
    else :
        turtle.color('blue')
        turtle.turtlesize(1)

    turtle.stamp()
    curX-=50
    multiply>>=1


    

turtle.done()
