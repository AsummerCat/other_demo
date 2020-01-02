# -*- coding:utf-8 -*-
import xlwt

'''
写入excel
'''


def write_excel():
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    # 存第一行cell(1,1)和cell(1,2)
    booksheet.write(0, 0, 'Python开发')
    booksheet.write(0, 1, 'Web前端')
    # 存第二行cell(2,1)和cell(2,2)
    booksheet.write(1, 0, '100人')
    booksheet.write(1, 1, '200人')
    # 存一行数据
    rowdata = [43, 56]
    for i in range(len(rowdata)):
        booksheet.write(2, i, rowdata[i])
    workbook.save('test_xlwt.xlsx')


if __name__ == '__main__':
    write_excel()
    print("xlwt已将数据写入Excel")
