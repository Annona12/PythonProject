# 开发者：Annona
# 开发时间：2023/1/11 15:46
# 合并多个单元格相同的数据
import os,pandas as pd
#获取文件夹路径下全部文件路径名字
def get_files(path):
    fs=[]
    for root,dirs,files in os.walk(path):
        for file in files:
            fs.append(os.path.join(root,file))
    return fs
#合并文件
def merge():
    files = get_files('G:/LWY_Other/testdate/python/excel')
    arr=[]
    for i in files:
        arr.append(pd.read_excel(i))
        writer=pd.ExcelWriter('G:/LWY_Other/testdate/python/excel/merge.xls')
        pd.concat(arr).to_excel(writer, 'Sheet1',engine='openpyxl',index=False)
        # pd.concat(arr).to_excel(writer,'Sheet1', index=False)
        writer.save()
if __name__=='__main__':
    merge()
# print(get_files('G:/LWY_Other/testdate/python/excel'))#注意需要使用斜杠"\"