import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

fig = plt.figure()
fig.set(alpha = 0.2)    #设定图标颜色alpha参数

data_train = pd.read_csv("E:/Python/Titanic-data-all/train.csv")
Survived_cabin = data_train.Survived[pd.notnull(data_train.Cabin)].value_counts()