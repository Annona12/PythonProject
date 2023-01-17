# 开发者：Annona
# 开发时间：2023/1/16 9:29
# 题目 暂停一秒输出，并格式化当前时间
import time

for i in range(4):
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)