# 开发者：Annona
# 开发时间：2023/1/31 17:53
# 题目 利用条件运算符的嵌套来完成此题：
# 学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示，
# 60分以下的用C表示。
points=int(input('请输入分数：'))
if points>=90:
    grade='A'
elif points<60:
    grade='C'
else:
    grade = 'B'
print(grade)