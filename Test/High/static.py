# 开发者：Annona
# 开发时间：2023/1/16 14:56
import openpyxl
import statistics as stats
# 使用data_only选项，我们从单元格而不是公式中获取值。
book=openpyxl.load_workbook('G:/LWY_Other/testdate/python/excel/sample.xlsx',data_only=True)
sheet=book.active
# 我们得到所有不为空的单元格行
rows=sheet.rows
values=[]
for row in rows:
    for cell in row:
        values.append(cell.value)
        # print(cell.value)
print("Number of values: {0}".format(len(values)))
print("Sum of values: {0}".format(sum(values)))
print("Minimum value: {0}".format(min(values)))
print("Maximum value: {0}".format(max(values)))
print("Mean: {0}".format(stats.mean(values)))
print("Median: {0}".format(stats.median(values)))
print("Standard deviation: {0}".format(stats.stdev(values)))
print("Variance: {0}".format(stats.variance(values)))