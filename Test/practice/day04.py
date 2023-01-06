# 开发者：Annona
# 开发时间：2023/1/6 9:50
# 实例004：这天第几天
# 题目 输入某年某月某日，判断这一天是这一年的第几天？
# 满足以下两个条件的整数才可以称为闰年：
# （1）普通闰年：能被4整除但不能被100整除（如2004年就是普通闰年）；
# （2）世纪闰年：能被400整除（如2000年是世纪闰年，1900年不是世纪闰年）；
# 判断是否是闰年的函数
def isLeapYear(y):
    return (y%400==0 or (y%4==0 and (y%100!=0)))
# 这个按照月份往后推一个月
DofM=[0,31,28,31,30,31,30,31,31,30,31,30]
res=0
year=int(input("please input year:"))
month=int(input("please input month:"))
day=int(input("please input day:"))
if(isLeapYear(year)):
    DofM[2]+=1
for i in range(month):
    res+=DofM[i]
print(res+day)