# 开发者：Annona
# 开发时间：2023/1/16 16:55
from openpyxl import Workbook
from openpyxl.styles import Alignment

book=Workbook()
sheet=book.active
# 要冻结窗格，我们使用freeze_panes属性。
sheet.freeze_panes='A4'

book.save('G:/LWY_Other/testdate/python/excel/freezing.xlsx')