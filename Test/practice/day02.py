# 开发者：Annona
# 开发时间：2023/1/4 9:56
# 题目
# 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# way1
profit=int(input("please input you money:"))
bonus=0
# if(profit<=100000):
#     bonus=profit*0.1
# elif((profit>100000)and(profit<200000)):
#     bonus = 100000*0.1+(profit-100000) * 0.075
# elif((profit>=200000)and(profit<400000)):
#     bonus = 100000 * 0.1 + 100000 * 0.075+(profit-200000)*0.05
# elif((profit>=400000)and(profit<600000)):
#     bonus = 100000 * 0.1 + 100000 * 0.075+200000*0.05+(profit-400000)*0.03
# elif((profit>=600000)and(profit<1000000)):
#     bonus = 100000 * 0.1 + 100000 * 0.075+200000*0.05+200000*0.03+(profit-600000)*0.015
# elif((profit>=1000000)):
#     bonus = 100000 * 0.1 + 100000 * 0.075+200000*0.05+200000*0.03+400000*0.015+(profit-1000000)*0.001
# print(bonus)
# way2
# 分析：break只用 break 语句，可以完全终止当前循环。
# 1、80000-i=0,退出循环
# 2、150000-i=1，退出循环
# 2、250000-i=2，退出循环
# 后续再自己按照这个思路自己单独编写这部分代码
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    print(i)
    if profit<=thresholds[i]:
        bonus+=profit*rates[i]
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)