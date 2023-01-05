# 开发者：Annona
# 开发时间：2022/12/20 16:04
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
#del 也可以用来删除整个变量
del a
print(a)