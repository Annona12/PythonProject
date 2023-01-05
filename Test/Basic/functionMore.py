# 开发者：Annona
# 开发时间：2022/12/16 15:43
# i = 5
# def f(arg=i):
#     print(arg)
# i = 6
# f()
#
# def f(a, L=[]):
#     L.append(a)
#     return L
# print(f(1))
# print(f(2))
# print(f(3))
# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
# print(f(1))
# print(f(2))
# print(f(3))
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
