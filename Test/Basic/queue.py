# 开发者：Annona
# 开发时间：2022/12/20 15:02
from collections import deque
from math import pi
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

# 例如，创建平方值的列表
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]

#以下列表推导式将两个列表中不相等的元素组合起来
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print([(x, x**2) for x in range(6)])
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
# 列表推导式可以使用复杂的表达式和嵌套函数
print([str(round(pi, i)) for i in range(1, 6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([row[0] for row in matrix])
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
# 实际应用中，最好用内置函数替代复杂的流程语句。此时，zip() 函数更好用：
print(list(zip(*matrix)))