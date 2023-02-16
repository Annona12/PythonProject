# 开发者：Annona
# 开发时间：2023/1/18 16:01
# 题目 判断101-200之间有多少个素数，并输出所有素数。
# 素数的判断方法：数字X的因数可以分成两大部分，小于X的平方根和大于X的平方根，这两部分是相互对应的
# 所以只需要判断从2-平方根的数是否都能被整除就可以。
import math
for i in range(100,200):
    flag=0
    for j in range(2,round(math.sqrt(i)+1)):
        if i % j == 0:
            flag=1
            break
    if flag:
        continue
    print(i)

# print(round(math.sqrt(101)+1))