# 开发者：Annona
# 开发时间：2023/1/9 15:46
# 实例005：三数排序
# 题目 输入三个整数x,y,z，请把这三个数由小到大输出。
arr=[]
for i in range(3):
    x=int(input('int%d:'%(i)))
    arr.append(x)
print(sorted(arr))