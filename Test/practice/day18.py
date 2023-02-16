# 开发者：Annona
# 开发时间：2023/2/3 16:38
# 题目 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
a=input('被加数：')
n=int(input('被加次数:'))
res=0
for i in range(n):
    res += int(a)
    # 因为a是字符所以是直接字符串拼接
    a += a[0]
    # print(a)
    print(a +a[0])
print('结果是：',res)