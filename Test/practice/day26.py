# 开发者：Annona
# 开发时间：2023/2/20 19:02
# 题目 利用递归方法求5!。
def factorial(n):
    return n*factorial(n-1) if n>1 else 1
print(factorial(5))
