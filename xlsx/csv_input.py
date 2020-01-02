# -*- coding:utf-8 -*-


import pandas as pd
import numpy as np

'''
写入CSV
'''


def write_csv1():
    csv_mat = np.empty((0, 2), float)
    csv_mat = np.append(csv_mat, [[43, 55]], axis=0)
    csv_mat = np.append(csv_mat, [[65, 67]], axis=0)
    csv_pd = pd.DataFrame(csv_mat)
    csv_pd.to_csv("test_pd.csv", sep=',', header=False, index=False)




def write_csv2():
    import unicodecsv as ucsv
    data = [[u"列1", u"列2"], [u"内容1", u"内容2"]]
    with open('test.csv', 'wb') as f:
        w = ucsv.writer(f, encoding='utf-8')
        w.writerows(data)

if __name__ == '__main__':
    write_csv2()
    print("csv写入成功")

