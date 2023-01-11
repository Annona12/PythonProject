# 开发者：Annona
# 开发时间：2023/1/6 17:10
import turtle
def love(x,y):
    lv=turtle.Turtle()
    lv.hideturtle()
    lv.up()
    lv.goto(x,y)
    #画圆弧
    # def curvemove():


def tree(a,b):
    print('tree')

t=turtle.Turtle()
t.hideturtle()
t.speed(100)
t.left(90)
t.up()#将线从屏幕上面拉起
t.backward(200)#将起点直接往后移动
t.down()#笔拉回屏幕上的。它在移动到另一个位置或方向时提供绘图。
t.color('brown')
t.pensize(32)
t.forward(60)
# tree(100, t)
turtle.done()