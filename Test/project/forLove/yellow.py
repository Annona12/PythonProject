# 开发者：Annona
# 开发时间：2023/1/9 10:00
### 怎么画小黄人：
import turtle
turtle.speed(4)
turtle.setup(600,600)
turtle.hideturtle()

# 身体
turtle.width(2)
turtle.up()
turtle.setx(150)
turtle.left(90)
turtle.down()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.fd(150)
turtle.circle(150,180)
turtle.fd(300)
turtle.circle(150,180)
turtle.fd(150)

turtle.end_fill()

# 眼镜
turtle.width(5)
turtle.pencolor('black')
turtle.up()
turtle.goto((0,150))
turtle.fillcolor('white')
turtle.begin_fill()
turtle.down()
turtle.circle(40)
turtle.circle(-40)
turtle.end_fill()

# 眼睛
turtle.width(1)
turtle.up()
turtle.goto((50,150))
turtle.down()

turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()

turtle.up()
turtle.goto((-30,150))
turtle.down()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()

# 眼镜架

turtle.up()
turtle.goto((80,150))
turtle.down()
turtle.width(20)
turtle.right(90)
turtle.fd(70)

turtle.up()
turtle.goto((-80,150))
turtle.down()
turtle.width(20)
turtle.left(180)
turtle.fd(70)

# 四根头发
turtle.width(3)
turtle.up()
turtle.goto((5,301))
turtle.down()
turtle.right(94)
turtle.fd(60)

turtle.up()
turtle.goto((20,298))
turtle.down()
turtle.fd(90)


turtle.up()
turtle.goto((-6,301))
turtle.down()
turtle.left(7)
turtle.fd(70)

turtle.up()
turtle.goto((-20,295))
turtle.down()
turtle.left(2)
turtle.fd(90)

# 嘴巴
turtle.up()
turtle.goto((-50,50))
turtle.down()
turtle.pencolor('red')
turtle.right(140)
turtle.circle(80,95)

# 裤子

turtle.pencolor('black')
turtle.width(2)

turtle.up()
turtle.home()       # 回到原点并恢复默认角度
turtle.goto((150,-150))
turtle.down()
turtle.fillcolor('#176185')
turtle.begin_fill()
turtle.left(180)
turtle.fd(50)
turtle.right(90)
turtle.fd(44)
turtle.left(60)
turtle.fd(12)
turtle.left(30)
turtle.fd(179.2)
turtle.left(30)
turtle.fd(12)
turtle.left(60)
turtle.fd(44)
turtle.right(90)
turtle.goto((-150,-150))
turtle.left(90)
turtle.circle(150,180)
turtle.goto((150,-150))
turtle.up()

turtle.end_fill()

turtle.up()
turtle.goto((100,-106))
turtle.down()
turtle.fillcolor('#176185')
turtle.begin_fill()
turtle.goto((150,-50))
turtle.goto((150,-35))
turtle.goto((90,-100))
turtle.end_fill()

turtle.up()
turtle.goto((-100,-106))
turtle.down()
turtle.fillcolor('#176185')
turtle.begin_fill()
turtle.goto((-150,-50))
turtle.goto((-150,-35))
turtle.goto((-90,-100))
turtle.end_fill()


# 口袋
turtle.width(5)
turtle.up()
turtle.goto((60,-140))
turtle.down()
turtle.left(90)
turtle.fd(120)
turtle.left(90)
turtle.fd(30)
turtle.circle(60,180)
turtle.fd(30)

turtle.mainloop()
