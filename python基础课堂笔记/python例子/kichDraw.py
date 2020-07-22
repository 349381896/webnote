#科赫雪花绘制
import turtle
def koch(size,n):
    if n == 0 :
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
        
def main():
    turtle.setup(800,800)
    turtle.pencolor("red")
    turtle.pu()
    turtle.goto(-200,100)
    turtle.pd()
    turtle.pensize(2)
    level = 3
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()  #隐藏画笔的turtle形状
    turtle.done()

if __name__ == "__main__":
    main()