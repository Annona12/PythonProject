# 开发者：Annona
# 开发时间：2022/12/20 16:11
# 元组由多个用逗号隔开的值组成
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)
empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)