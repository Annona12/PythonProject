# 开发者：Annona
# 开发时间：2023/2/1 17:54
# 题目 输出指定格式的日期
import datetime

print(datetime.date.today())
print(datetime.date(2333,2,3))
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.date.today().strftime('%Y/%m/%d'))
day=datetime.date(1111,2,3)
day=day.replace(year=day.year+22)
print(day)
