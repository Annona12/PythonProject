# 开发者：Annona
# 开发时间：2023/1/16 17:19
from openpyxl import Workbook
from openpyxl.drawing.image import Image

book=Workbook()
sheet=book.active
# 创建一个新的Image类。 icesid.png图像位于当前工作目录中
image=Image('G:/LWY_Other/testdate/python/excel/1.jpg')
sheet['A1']='Test'
# 使用add_image()方法添加新图像
sheet.add_image(image,'B2')

book.save('G:/LWY_Other/testdate/python/excel/sheet_image.xlsx')