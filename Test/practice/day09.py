# 开发者：Annona
# 开发时间：2023/1/13 16:59
# 暂停一秒输出。使用 time 模块的 sleep() 函数
import time
for i in range(4):
    print(str(int(time.time()))[-2:])#获取时间戳的最后两位
    time.sleep(1)
# localtime = time.localtime()
# print(localtime)
# import time
# localtime = time.ctime()
# print ("本地时间为 :", localtime)