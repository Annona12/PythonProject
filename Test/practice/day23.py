# 开发者：Annona
# 开发时间：2023/2/10 16:00
# 题目 打印出如下图案（菱形）:
# 分析：draw(4):*
# 进入if num!=1:draw(3)-输出***返回draw(4)中的if num!=1:下面的print
# 进入if num!=1:draw(2)-输出*****返回draw(3)中的if num!=1:下面的print
# 进入if num!=1:draw(1)-输出*******返回draw(2)中的if num!=1:下面的print
def draw(num):
    print(num)
    a="*"*(2*(4-num)+1)
    # print(num)
    print(a.center(9,' '))
    if num!=1:
        draw(num-1)
        # print(num)
        print(a.center(9,' '))

draw(4)