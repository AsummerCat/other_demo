# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

'''
读取CSV
'''
def read_csv():
    filename = "test_pd.csv"
    csv_data = pd.read_csv(filename, header=None)
    csv_data = np.array(csv_data, dtype=float)
    for i in csv_data:
        print(i)


if __name__ == '__main__':
    read_csv()
    print("csv读取成功")
