# 开发者：Annona
# 开发时间：2023/1/4 13:52
import turtle
import random

# 画爱心
def love(x, y):
    # 初始化turtle,创建对象Turtle并将其分配给变量
    lv = turtle.Turtle()
    # 这个方法是用来使Turtle隐身的。隐藏箭头
    lv.hideturtle()
    lv.up()
    # 定位
    lv.goto(x, y)
    # 画圆弧
    def curvemove():
        for i in range(20):
            lv.right(10)
            lv.forward(2)

    lv.color('red', 'pink')
    lv.speed(10000000)
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

# 画树
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

myWin = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.speed(3)
t.left(90)
t.up()
t.backward(200)
t.down()
t.color("brown")
t.pensize(32)
t.forward(60)
tree(100, t)
myWin.exitonclick()
# turtle.done()