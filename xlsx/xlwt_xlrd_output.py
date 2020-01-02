# -*- coding:utf-8 -*-
import xlrd

'''
读取excel
'''


def read_excel():
    workbook = xlrd.open_workbook('test_xlwt.xlsx')
    print(workbook.sheet_names())  # 查看所有sheet
    booksheet = workbook.sheet_by_index(0)  # 用索引取第一个sheet
    booksheet = workbook.sheet_by_name('Sheet 1')  # 或用名称取sheet
    # 读单元格数据
    cell_11 = booksheet.cell_value(0, 0)
    cell_21 = booksheet.cell_value(1, 0)
    cell_12 = booksheet.cell_value(0, 1)
    cell_22 = booksheet.cell_value(1, 1)
    # 读一行数据
    row_3 = booksheet.row_values(2)
    print(cell_11, cell_21, cell_12, cell_22, row_3)


if __name__ == '__main__':
    read_excel()
    print("xlwt已将Excel读取完毕")
