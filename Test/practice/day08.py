# 开发者：Annona
# 开发时间：2023/1/12 15:18
# 题目 输出 9*9 乘法口诀表,i控制行，j控制列
for i in range(1,10):#1，2，3，4，5，6，7，8，9
    for j in range(1,i+1):
        print('%d*%d=%2ld '%(i,j,i*j),end='')#end，表示结尾不换行
    print()