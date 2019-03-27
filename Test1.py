import pandas as pd     #数据分析
import numpy as np      #科学计算
from pandas import Series,DataFrame

"""
pandas是常用的Python数据处理包，把csv文件读入成dataframe格式
"""
data_train = pd.read_csv("E:/Python/Titanic-data-all/train.csv")
# print(data_train)
data_train.info()
