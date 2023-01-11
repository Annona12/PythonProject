# 开发者：Annona
# 开发时间：2023/1/10 16:47
# 题目 斐波那契数列。
def Fib(n):
    return 1 if n<=2 else Fib(n-1)+Fib(n-2)
print(Fib(6))