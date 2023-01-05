# 开发者：Annona
# 开发时间：2023/1/3 16:58
# 题目 有四个数字：1、2、3、4，
# 能组成多少个互不相同且无重复数字的三位数？各是多少？
total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if((i!=j)and(j!=k)and(k!=i)):
                # print(i*100+j*10+k)
                total+=1
print(total)
# 使用迭代器
import itertools
sum=0
for i in itertools.permutations([1,2,3,4],3):
    # print(i)
    sum+=1
print(sum)