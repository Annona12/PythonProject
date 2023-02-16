# 开发者：Annona
# 开发时间：2023/1/11 10:18
# 题目 将一个列表的数据复制到另一个列表中。
import copy
a = [1,2,3,4,['a','b']]
b=a#浅拷贝
c=a[:]#浅拷贝
d=copy.copy(a)#浅拷贝
e=copy.deepcopy(a)#深拷贝

a.append(5)
a.append(57)
a[4].append('c')
a[4].append('d')
[1,2,3,4,['a','b','c','d'],5,57]
[1,2,3,4,['a','b','c','d']]

[1,2,3,4,['a','b']]
print('a=',a,id(a),id(a[4]))
print('b=',b,id(b),id(b[4]))
print('c=',c,id(c),id(c[4]))
print('d=',d,id(d),id(d[4]))
print('e=',e,id(e),id(e[4]))