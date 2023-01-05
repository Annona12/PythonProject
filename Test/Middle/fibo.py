# 开发者：Annona
# 开发时间：2022/12/21 13:43
# Fibonacci numbers module
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))