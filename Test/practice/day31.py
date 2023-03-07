# 开发者：Annona
# 开发时间：2023/3/6 17:53
# 题目
# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
weekT={'h':'thursday',
       'u':'tuesday'
}
weekS={'a':'saturday',
       'u':'sunday'
}
week={'t':weekT,
      's':weekS,
      'm':'monday',
      'w':'wensday',
      'f':'friday'
}
a=week.get(str(input('请输入第一位字母：')).lower())

if a==None:
    print('请输入正确的首字母！')
else:
    if a == weekT or a == weekS:
        print(a[str(input('请输入第二个字母：')).lower()])
    else:
        print(a)
