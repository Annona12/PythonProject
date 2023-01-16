# 开发者：Annona
# 开发时间：2023/1/6 17:10
import turtle
import random
def love(x,y):
    lv=turtle.Turtle()
    lv.hideturtle()
    lv.up()
    lv.goto(x,y)
    #画圆弧
    def curvemove():
        for i in range(20):
            lv.right(10)
            lv.forward(2)
    lv.color('red','pink')
    lv.speed(100)
    lv.pensize(1)
    lv.down()
    lv.begin_fill()
    lv.left(140)
    lv.forward(22)
    curvemove()
    lv.left(120)
    curvemove()
    lv.forward(22)
    # 画完复位
    lv.left(140)
    lv.end_fill()


def tree(branchLen, t):
    # 剩余树枝太少要结束递归
    if branchLen > 5:
        # 如果树枝剩余长度较短则变绿
        if branchLen < 20:
            t.color("green")
            t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
            t.down()
            t.forward(branchLen)
            love(t.xcor(), t.ycor())
            t.up()
            t.backward(branchLen)
            t.color("brown")
            return
        t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
        t.down()
        t.forward(branchLen)
        # 以下递归
        ang = random.uniform(15, 45)
        t.right(ang)
        # 随机决定减小长度
        tree(branchLen - random.uniform(12, 16), t)
        t.left(2 * ang)
        # 随机决定减小长度
        tree(branchLen - random.uniform(12, 16), t)
        t.right(ang)
        t.up()
        t.backward(branchLen)

t=turtle.Turtle()
t.hideturtle()
t.speed(1000)#设置速度
t.left(90)#原始是水平画线，向左就是向上画
t.up()#将线从屏幕上面拉起
t.backward(250)#将起点直接往后移动
t.down()#笔拉回屏幕上的。它在移动到另一个位置或方向时提供绘图。
t.color('brown')
t.pensize(32)
t.forward(60)
tree(100,t)
turtle.done()