##2019038010 박준용##
import turtle
import random
import math
from tkinter.simpledialog import *

inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = 0,0,20
radius, angle, radian = 100, 0, 0

turtle.title('거북이 원 모양의 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)	 
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

angle = 360 / len(inStr)

for ch in inStr :

    radian = 3.14 * angle / 180

    tX = radius * math.cos(radian)
    tY = radius * math.sin(radian)
    r = random.random(); g = random.random(); b = random.random()

    turtle.goto(tX, tY)
	 
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))

    angle += 360 / len(inStr)
    radius -= (radius/len(inStr))

turtle.done()
