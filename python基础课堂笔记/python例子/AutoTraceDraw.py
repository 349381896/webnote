#自动绘制轨迹
import turtle as t 
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pensize(5)
t.pencolor("red")

#数据读取
detals = []
f = open("python课堂笔记/static/data.txt")
for line in f:
    line = line.replace("\n","")
    detals.append(list(map(eval,line.split(","))))
    #map函数将第一个参数的功能作用与第二个参数的每一个元素
f.close()

#自动绘制
for i in range(len(detals)):
        t.pencolor(detals[i][3],detals[i][4],detals[i][5])
        t.fd(detals[i][0])
        if detals[i][1]:
            t.right(detals[i][2])
        else:
            t.left(detals[i][2])