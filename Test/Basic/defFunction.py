# 开发者：Annona
# 开发时间：2022/12/16 14:28
# F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）
# def fib(n):
#     a,b=0,1
#     while a<n:
#         print('a=',a)
#         a,b=b,a+b
# fib(100)

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
print(fib2(100))