# 开发者：Annona
# 开发时间：2023/1/16 15:18
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
data = [
    ['Item', 'Colour'],
    ['pen', 'brown'],
    ['book', 'black'],
    ['plate', 'white'],
    ['chair', 'brown'],
    ['coin', 'gold'],
    ['bed', 'brown'],
    ['notebook', 'white'],
]
for r in data:
    sheet.append(r)
sheet.auto_filter.ref = 'A1:B8'
sheet.auto_filter.add_filter_column(0, ['brown', 'white'])
sheet.auto_filter.add_sort_condition('B2:B8')
wb.save('G:/LWY_Other/testdate/python/excel/filtered.xlsx')

