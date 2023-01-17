# 开发者：Annona
# 开发时间：2023/1/16 17:38
from openpyxl import Workbook
from openpyxl.chart import (Reference,Series,BarChart)
book=Workbook()
sheet=book.active
rows = [
    ("USA", 46),
    ("China", 38),
    ("UK", 29),
    ("Russia", 22),
    ("South Korea", 13),
    ("Germany", 11)
]
for row in rows:
    sheet.append(row)
# 对于Reference类，我们引用表中代表数据的行,获取金牌数
data=Reference(sheet,min_col=2,max_col=2,min_row=1,max_row=6)
# 获取国家文本标签名
categs=Reference(sheet,min_col=1,max_col=1,min_row=1,max_row=6)
# 创建一个条形图并为其设置数据和类别
chart=BarChart()
chart.add_data(data=data)
chart.set_categories(categs)
# 使用legend和majorGridlines属性，可以关闭图例和主要网格线
chart.legend = None
chart.y_axis.majorGridlines = None
# 将varyColors设置为True，每个条形都有不同的颜色
chart.varyColors = True
# 为图表设置标题。
chart.title = "Olympic Gold medals in London"
# 使用add_chart()方法将创建的图表添加到工作表中
sheet.add_chart(chart, "A8")
book.save('G:/LWY_Other/testdate/python/excel/bar_chart.xlsx')