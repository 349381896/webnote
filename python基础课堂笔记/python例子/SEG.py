import turtle,time

def drawGap():  #绘制数码管间隔
    turtle.pu()
    turtle.fd(5)
def drawLine(draw): #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
    
def drawDigit(dight):   #根据数字绘制七段数码管
    drawLine(True) if dight in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if dight in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.pu() #为后续数字确定位置
    turtle.fd(20)

def drawDate(date): #获取要输入的数字
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == "=":
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == "+":
            turtle.write('日',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))#通过eval()函数将数字变为整数

def main():
    turtle.setup(800,350,200,200)
    turtle.tracer(False)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    turtle.speed(10)
    drawDate(time.strftime("%Y-%M=%d+",time.gmtime()))
    turtle.hideturtle()  #隐藏画笔的turtle形状
    turtle.done()


if __name__ == "__main__":
    main()